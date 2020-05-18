# Project: Data Modeling with Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Datasets

### Song Dataset

The first dataset is a subset of real data from the [Million Song Dataset](http://millionsongdataset.com/).
Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

### Log Dataset

## Data Modeling with Star Schema

![Star Schema for Song Play Analysis!](./song_play_analysis_with_star_schema.png "Star Schema for Song Play Analysis")


## Project Files

In addition to the data files, the project workspace includes six files:

**test.ipynb**  displays the first few rows of each table to check the database.
**create_tables.py**  drops and creates tables. Run this file to reset  tables before each time you run your ETL scripts.
**etl.ipynb**  reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
**etl.py**  reads and processes files from song_data and log_data and loads them into your tables. 
**sql_queries.py**  contains all sql queries, and is imported into the last three files above.
**run.ipynb**  run **create_tables.py** and **etl.py** from notebook
**README.md** provides project info

## Build ETL Processes

**etl.ipynb** notebook is used to develop ETL processes for each table. 

Remember to rerun create_tables.py to reset tables before each time yrun this notebook.
run test.ipynb to confirm that records were successfully inserted into each table. 

## Build ETL Pipeline

**etl.py** will process the entire datasets.
Remember to run create_tables.py before running etl.py to reset tables. 
Run test.ipynb to confirm your records were successfully inserted into each table.

## Instruction

1. use following command to create tables
    python create_tables.py
    
2. Insert data to each table (ETL pipeline)
    python etl.py
    
3. Chect the database
    test.ipynb
    
## Author

**Xingya Zhou**
    



