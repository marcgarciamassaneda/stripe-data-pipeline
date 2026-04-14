import stripe
import pandas as pd
from google.cloud import bigquery


def extract_stripe_charges():
    """Extracts all charges from Stripe and returns them as a DataFrame."""
    
    charges = stripe.Charge.list()

    data = []

    for c in charges.auto_paging_iter():
        data.append({
            "charge_id": c.id,
            "amount": c.amount,
            "currency": c.currency,
            "status": c.status,
            "created": c.created,
            "customer_id": c.customer
        })

    return pd.DataFrame(data)

def extract_stripe_customers():
    """Extracts all customers from Stripe and returns them as a DataFrame."""
    
    customers = stripe.Customer.list()

    data = []

    for c in customers.auto_paging_iter():
        data.append({
            "customer_id": c.id,
            "email": c.email,
            "created": c.created
        })

    return pd.DataFrame(data)

def upload_to_bigquery(df, project_name, dataset_name, table_name):
    """Uploads a DataFrame to BigQuery."""

    client = bigquery.Client()
    dataset_id = dataset_name
    table_id = f"{project_name}.{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)

    job.result()  # waits for upload