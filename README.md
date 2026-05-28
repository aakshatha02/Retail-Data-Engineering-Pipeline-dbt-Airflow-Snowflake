# Retail Data Engineering Pipeline (dbt + Airflow + Snowflake + Databricks)

## Project Overview

This project builds an end-to-end retail data engineering pipeline using a modern analytics stack. It demonstrates how raw retail transaction data can be ingested, orchestrated, transformed, and made analytics-ready using tools commonly used in production data platforms. The pipeline is designed around a retail dataset sourced from Kaggle ([Kaggle Retail Dataset](https://www.kaggle.com/datasets/matteo2002/retail-dataset?resource=download&select=purchases.csv)) and focuses on simulating a real-world analytics workflow where data moves through multiple layers of processing before reaching a final analytical state.

The system is structured to reflect a typical cloud data warehouse architecture where orchestration, transformation, and storage are separated into modular components, enabling scalability and maintainability.

## Architecture

The pipeline follows a layered architecture that begins with raw retail data ingestion and progresses through transformation and modeling stages before reaching analytical storage. Airflow is used to orchestrate the entire workflow, ensuring that each stage of the pipeline executes in the correct order and with proper dependencies. Once data is ingested, dbt is used to structure transformations into modular, testable SQL models that progressively clean and reshape the data into analytics-ready tables. The transformed data is then loaded into Snowflake, which serves as the primary cloud data warehouse for querying and analysis. Databricks is incorporated as an additional processing environment to explore distributed computation and potential advanced analytics workflows.

This architecture is designed to reflect real-world data platform design where orchestration, transformation, and storage are decoupled to improve scalability and maintainability.

## Tech Stack

This project uses Apache Airflow for workflow orchestration, dbt for transformation logic and data modeling, Snowflake as the cloud data warehouse, and Databricks as a distributed data processing environment. Python is used for scripting and integration, while SQL forms the core language for data transformations. GitHub is used for version control and project management, with the repository hosted at GitHub Repository.

## Dataset

The dataset used in this project is a retail transactions dataset sourced from Kaggle. It contains purchase-level data that simulates real-world retail operations, including transactional information that can be used for building customer-level and product-level analytics. This dataset is used as the foundation for building staging models, transformation logic, and analytical outputs within the pipeline.

## dbt Transformations

dbt is used to structure the transformation layer into modular models that progressively refine raw data into analytics-ready tables. The transformation design follows a layered approach where raw data is first standardized in staging models, then enriched and joined in intermediate models, and finally aggregated into business-ready models such as sales summaries or customer behavior views. This structure ensures clarity, reusability, and testability of transformation logic while maintaining a clean separation between raw ingestion and business logic.

## Airflow Orchestration

Airflow is responsible for orchestrating the entire pipeline and ensuring that each stage executes in the correct sequence. The workflow is designed as a directed acyclic graph where ingestion, transformation, and loading tasks are connected through dependencies. This allows the pipeline to be scheduled, monitored, and retried in case of failures, making the system more robust and production-like.

## Snowflake and Databricks Integration

Snowflake is used as the primary data warehouse where transformed datasets are stored and queried for analytical purposes. It provides a scalable and structured environment for running SQL-based analytics on processed retail data. Databricks is included as an additional compute layer to explore distributed processing capabilities and potential future extensions such as advanced analytics, machine learning workflows, or large-scale data transformations.

## Project Structure

The repository is organized to separate orchestration, transformation, and configuration logic into distinct components. Airflow DAG definitions manage workflow execution, dbt models define transformation logic, and configuration files handle connections to Snowflake and Databricks. This structure is designed to reflect a modular data engineering project where each tool has a clearly defined responsibility within the pipeline.

## Project Status and Future Work

This project is currently in active development. The core pipeline structure and tool integrations are being built, with ongoing work focused on improving orchestration stability, expanding dbt models, and refining data loading into Snowflake and Databricks. Future improvements include adding data quality checks within dbt, implementing incremental loading strategies, improving observability within Airflow, and potentially integrating dashboarding tools for visualization of retail analytics outputs.

## Learning Outcomes

This project demonstrates practical experience in building a modern data engineering pipeline using industry-standard tools. It explores how orchestration, transformation, and warehousing layers interact in a cloud-based architecture and provides hands-on experience with workflow scheduling, modular SQL transformations, and scalable data storage systems.