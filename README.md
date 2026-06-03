## Overview

This is an end-to-end retail data pipeline built with a modern analytics stack. It takes raw transaction data from Kaggle and moves it through ingestion, transformation, and into a warehouse ready for analysis.

The idea is to simulate how a real data platform works: raw data comes in messy, gets cleaned and structured, and ends up in a format that’s easy to query.

## Architecture

Airflow runs the pipeline and controls the order of execution.

Data is first ingested, then transformed using dbt into structured SQL models. These models clean and reshape the raw data into usable tables.

Snowflake is used as the main warehouse for storing the final datasets. Databricks is included for distributed processing.

## Tech Stack

- Airflow for orchestration  
- dbt for data modeling and transformations  
- Snowflake for warehousing  
- Databricks for distributed compute  
- Python for scripting and integration  
- SQL for transformations  
- GitHub for version control  

## Dataset

The dataset comes from Kaggle and contains retail transaction data from December 2014 to December 2015. It has 436,689 rows, where each row represents a product in a customer invoice.

Dataset: https://www.kaggle.com/datasets/matteo2002/retail-dataset
