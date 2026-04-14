# 📊 Stripe Data Pipeline & Analytics Dashboard

## 🚀 Overview

This project demonstrates an end-to-end data pipeline that extracts data from the Stripe API, processes it, loads it into a data warehouse, transforms it using dbt, and visualizes insights in a dashboard.

It simulates a real-world SaaS analytics workflow.

---

## 🧱 Architecture

Stripe API → Python → Pandas → BigQuery → dbt → Looker Studio

---

## ⚙️ Tech Stack

- Python
- Stripe API
- Pandas
- Google BigQuery
- dbt
- Looker Studio

---

## 🔄 Pipeline Steps

### 1. Data Generation & Extraction
- Created sample customers and payments using Stripe API
- Simulated both successful and failed transactions

### 2. Data Processing
- Structured data using Pandas DataFrames

### 3. Data Loading
- Uploaded data into BigQuery tables:
  - `raw_customers`
  - `raw_charges`

### 4. Data Transformation (dbt)

#### Layers:
- **Raw**: Ingested Stripe data
- **Staging**: Cleaned and standardized models (`stg_*`)
- **Marts**:
  - `fct_charges` (fact table)
  - `dim_customers` (dimension table)

---

## 📊 Dashboard

Built in Looker Studio with the following metrics:

- Total Revenue
- Total Transactions
- Unique Customers
- Average Order Value (AOV)
- Revenue Over Time
- Top Customers
- Payment Status Breakdown

---

## 💡 Key Learnings

- Building end-to-end data pipelines
- Working with APIs and cloud data warehouses
- Implementing dbt best practices
- Designing analytics-ready data models
- Creating business dashboards

---

## 👤 Author

**Marc Garcia Massaneda**

Data Engineer | Python | Google Cloud

