# 🛒 Elite Retail Analytics: End-to-End ELT Pipeline

## 📖 Project Overview
In the fast-paced retail industry, the ability to transform raw operational data into actionable insights is a competitive necessity. <b>Elite Retail Store - UK</b> operates using an <b>OLTP (Online Transactional Processing)</b> system that generates daily sales, customer, and inventory data across multiple sources.

#### The Problem :
Operational data is often "siloed" and not optimized for analytical queries. Direct reporting on OLTP databases can lead to performance degradation and high costs. This project solves these issues by building a robust <b>Data Pipeline</b> that offloads data to a Cloud Data Warehouse, transforms it into an optimized <b>Analytical Schema (OLAP)</b>, and visualizes it for executive decision-making.

#### The Goal of this project: 
1. Ingests raw operational data into <b>Google Cloud Storage (Data Lake)</b>.
2. Loads and optimizes the data in <b>Google BigQuery (Data Warehouse)</b>.
3. Transforms raw transactions into a refined Star Schema using <b>dbt</b>.
4. Visualizes key KPIs via an interactive <b>Looker Studio Dashboard</b>.

## 🏗️ Architecture
The pipeline leverages the Google Cloud Platform (GCP) ecosystem:
- <b>Orchestration</b>: Apache Airflow (Dockerized)
- <b>Data Lake</b>: Google Cloud Storage (GCS)
- <b>Data Warehouse</b>: Google BigQuery
- <b>Transformation</b>: dbt (Data Build Tool)
- <b>Visualization</b>: Looker Studio

<img width="1792" height="584" alt="image" src="https://github.com/user-attachments/assets/b5c0c85e-c6d0-429b-b7f3-143c68cbe34c" />

## 📊 Dataset Detail
We use the Elite Retail Transaction Dataset - UK, consisting of:


1. `customers_master.csv` : Contains customer demographic and profile information.

2. `products_catalog.csv` : Detailed product-level data including pricing, supplier, and attributes.

3. `product_categories.csv` : Hierarchical classification of products into categories and departments.

4. `store_locations.csv` : Information about store branches including size, region, and management.

5. `staff_records.csv` : Employee data associated with stores and roles.

6. `sales_raw_oltp.csv` : Transactional dataset capturing sales events including customer purchases, products, stores, and timestamps.

#### Data Relationships
- `customers_master.customer_id` → `sales_raw_oltp.customer_id`
- `products_catalog.product_id` → `sales_raw_oltp.product_id`
- `store_locations.store_id` → `sales_raw_oltp.store_id`
- `staff_records.staff_id` → `sales_raw_oltp.staff_id`
- `product_categories.category_id` → `products_catalog.category_id`


## 🛠️ Data Modeling with dbt
 implemented a Modular Data Modeling approach using dbt. This ensures that the transformation logic is easy to maintain, test, and document.
  ####  1. Staging Layer (models/staging):
 The staging layer acts as the entry point for our data into the warehouse. Each staging model corresponds to a raw source table, where we perform "light" transformations such as renaming columns for consistency, casting data types, and basic deduplication.
 Key Staging Models:
 - `stg_sales.sql`: Cleans the core transactional data, ensuring sale_date is properly cast as a DATE type.
 - `stg_customers.sql`: Standardizes customer profiles and loyalty tier naming.
 - `stg_products.sql`: Standardizes product descriptions and retail pricing formats.
 - `stg_categories.sql`: Maps product categories to their respective departments.
 - `stg_stores.sql`: Cleans store metadata including location and region names.
 - `stg_staff.sql`: Manages employee records associated with transactions.
 - `stg_suppliers.sql`: Cleans supplier-level attributes for supply chain analysis.
 - Command: `dbt run --select staging`
 
 #### 2. Marts Layer (models/marts):
 The marts layer represents our "Business Logic." It consumes the staging models to create high-value, de-normalized tables optimized for reporting.
 - Model: `fact_sales.sql`
 - Logic: This model performs a series of `LEFT JOINs` starting from `stg_sales` and enriching it with dimensions from `stg_customers`, `stg_products`, and `stg_stores`.
 - Calculations: calculate business metrics like `revenue` (quantity * retail_price) and `profit_per_unit`.
 - Command: `dbt run --select marts`

## ⚙️ Data Warehouse Optimization (BigQuery)
To maximize query performance and minimize costs (Slot time/Bytes scanned) in BigQuery, the final fact_sales table implements:
1. Partitioning: By `sale_date` (Daily). 
2. Clustering: By `region` and `category_name`. This physically reorders the data in storage, significantly speeding up "Group By" and "Filter" operations used in the Revenue Distribution charts.


## 🤖 Workflow Orchestration (Airflow)
The entire transformation process is automated using a Python-based DAG.
- DAG ID: `retail_pipeline.py`
- Schedule: Runs every 2 minutes (configured for demo purposes) or @daily for production.
- Task Flow:
  1.  `dbt_staging`: Validates and cleans raw data.
  2.  `dbt_marts`: Builds the final analytical fact tables.

  - Dependency: `dbt_staging` >> `dbt_marts`
 
## 📊 Business Intelligence (Looker Studio)
The final dashboard provides an executive-level overview of retail health:
- `KPI Scorecards`: Total Revenue ($8.6B), Quantity (10.5M), and Profit ($6.4B).
- `Market Share`: Treemap visualization showing Revenue distribution across UK regions (Central, West, North, etc.).
- `Product Performance`: Horizontal bar chart identifying the Top 5 Departments by Sales.
- `Temporal Filters`: Drop-down controls for Year, Month, and Day for granular drill-downs.
- Link : [https://lookerstudio.google.com/reporting/b44fa890-0e52-4179-9e4b-fa98d5cc2ef5]
<img width="1437" height="1070" alt="image" src="https://github.com/user-attachments/assets/3de286b7-576a-4aa5-af26-f95b2ba93c1a" />

