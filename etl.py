import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """ Read song data json file and insert values to songs table, artists table

    Arguments:
            cur {object}: Allows Python code to execute PostgreSQL command in a database session
            filepath {str}: specify the path of the song data json files

    Returns:
            No return values
    """
       
    # open song file
    df =  pd.read_json(filepath,lines=True)

    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """ Read log data json file and insert values to users table, time table and songplays table

    Arguments:
            cur {object}: Allows Python code to execute PostgreSQL command in a database session
            filepath {str}: specify the path of the log data json files

    Returns:
            No return values
    """
    
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df.page.str.contains("NextSong")]

    # convert timestamp column to datetime
    start_time=df["ts"]
    timestamp=start_time.apply(lambda x: pd.Timestamp(x, unit="ms"))
    hour = timestamp.dt.hour
    day = timestamp.dt.day
    week = timestamp.dt.week
    month = timestamp.dt.month
    year = timestamp.dt.year
    weekday = timestamp.dt.weekday
    
    time_values = pd.concat([start_time, hour, day, week, month, year, weekday], axis=1)
    time_values.columns = ["start_time",  "hour", "day", "week","month", "year", "weekday"]
     
    # insert time data records
    #time_data = 
    #column_labels = 
    time_df = pd.DataFrame.from_dict( dict(time_values) )

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df =  df[['userId','firstName', 'lastName', 'gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.length, row.artist, ))
        
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = ([str(row.ts),row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent])
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """ Processing song/log data json files 

    Arguments:
            cur {object}: Allows Python code to execute PostgreSQL command in a database session
            conn {object}: the sparkifydb database connection object
            filepath {str}: the path of the song/log data
            func (function): the data processing function

    Returns:
            No return values
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """Connecting to database sparkifydb"""
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    """Processing the data files"""
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()

if __name__ == "__main__":
    main()