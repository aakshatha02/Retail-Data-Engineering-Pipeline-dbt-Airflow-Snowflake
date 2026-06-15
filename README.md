## Overview

This is an end-to-end retail data pipeline built with a modern analytics stack. It automatically ingests raw transaction data from Kaggle via an Airflow DAG and moves it through ingestion, transformation, and into a cloud data warehouse ready for analysis.

The goal of this project is to simulate a production-grade data platform: raw data comes in messy, gets cleaned and structured, and ends up in an optimized format that’s easy to query.

## Architecture

* **Ingestion:** An Airflow DAG securely connects to the Kaggle API using credentials passed via Docker Compose environment variables. The DAG automatically downloads the raw retail dataset and stages it for processing.
* **Transformation:** Once ingested, the data is transformed using dbt into structured SQL models. These models clean, deduplicate, and reshape the raw data into optimized analytical tables.
* **Storage & Compute:** Snowflake is utilized as the central data warehouse for storing the final datasets, while Databricks is leveraged for distributed compute and processing.

## Tech Stack

- **Airflow** for orchestration  
- **dbt** for data modeling and transformations  
- **Snowflake** for warehousing   
- **Python** for scripting and integration  
- **SQL** for transformations  
- **GitHub** for version control  

## Dataset & Ingestion Mechanics

* **Source:** [Kaggle Retail Dataset (Dec 2014 – Dec 2015)](https://www.kaggle.com/datasets/matteo2002/retail-dataset)
* **Dataset Scale:** 436,689 rows of transactional data, where each row represents an individual product line item within a customer invoice.
* **Ingestion Method:** Automated via an Airflow DAG utilizing the Kaggle CLI/API. To keep the pipeline secure and production-ready, Kaggle API credentials (`KAGGLE_USERNAME` and `KAGGLE_PASSWORD`) are passed dynamically into the Airflow Docker containers using a `.env` file and Docker Compose, preventing any secrets from being hardcoded into source control.