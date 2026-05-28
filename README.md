# Retail Data Engineering Pipeline (dbt + Airflow + Snowflake + Databricks)

## Project Overview

This project is an end-to-end retail data pipeline built using a modern analytics stack. It takes raw retail transaction data from Kaggle and moves it through ingestion, orchestration, transformation, and finally into an analytics-ready warehouse.

The goal is to simulate a real-world data platform where raw data is progressively cleaned, transformed, and structured for analysis using tools commonly found in production environments.

## Architecture

The pipeline follows a layered architecture that mirrors how modern data platforms are typically designed.

Airflow orchestrates the entire workflow, ensuring each step runs in the correct order. Raw data is first ingested, then transformed using dbt into structured, testable SQL models. These models progressively clean and reshape the data into meaningful datasets.

Snowflake acts as the central data warehouse where the final transformed data is stored and queried. Databricks is included as an additional processing layer to explore distributed compute and potential extensions like advanced analytics or machine learning workflows.

Overall, the design separates orchestration, transformation, and storage to keep the system modular and scalable.

## Tech Stack

Apache Airflow is used for orchestration, dbt for data modeling and transformations, Snowflake for cloud data warehousing, and Databricks for distributed processing. Python handles scripting and integration tasks, while SQL drives most of the transformation logic. GitHub is used for version control and project organization.

## Dataset

The dataset used in this project is sourced from Kaggle and represents retail transaction data at the purchase level. It contains 436,689 records of commercial transactions from a retail store/marketplace, collected between December 2014 and December 2015. Each row corresponds to a single product purchased within an invoice, making it well-suited for building customer, product, and sales analytics.

Dataset link: https://www.kaggle.com/datasets/matteo2002/retail-dataset

## dbt Transformations

dbt is used to structure all transformations into a layered model.

Raw data is first standardized in staging models, then enriched through intermediate transformations, and finally aggregated into business-focused tables such as sales summaries and customer-level insights. This approach keeps the logic clean, reusable, and easy to test.

## Airflow Orchestration

Airflow manages the entire pipeline as a directed acyclic graph (DAG), coordinating ingestion, transformation, and loading tasks.

Each stage depends on the previous one, ensuring the pipeline runs in a controlled and predictable way. It also enables scheduling, monitoring, and retries, making the workflow production-like in behavior.

## Snowflake and Databricks Integration

Snowflake serves as the main analytics warehouse where processed data is stored and queried efficiently.

Databricks complements this by providing a distributed compute environment, useful for heavier processing tasks and future extensions such as machine learning workflows and advanced analytics.

## Project Structure

The repository is organized by responsibility:

- Airflow handles orchestration logic  
- dbt contains all transformation models  
- Configuration files manage connections to Snowflake and Databricks  

This separation keeps the project modular and easy to extend without impacting other components.

## Project Status and Future Work

The project is currently in development. The core pipeline is in place, with ongoing improvements focused on stability, dbt model expansion, and refined data loading into Snowflake and Databricks.

Future improvements include adding data quality checks in dbt, implementing incremental models, improving Airflow observability, and adding a BI layer for dashboards and reporting.

## Learning Outcomes

This project demonstrates how modern data engineering systems are built in practice. It combines orchestration, transformation, and warehousing into a single pipeline and provides hands-on experience with tools used in real-world data platforms.