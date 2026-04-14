from main_functions import extract_stripe_charges, extract_stripe_customers, upload_to_bigquery
from credentials import STRIPE_API_KEY
import stripe
import os

stripe.api_key = STRIPE_API_KEY
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_credentials.json"

def main():

    df_charges = extract_stripe_charges()
    #print(df_charges)
    print('Charges extracted!')
    upload_to_bigquery(df_charges, project_name='weather-project-geocoding-api', dataset_name="stripe_data", table_name="raw_charges")
    print('Charges uploaded to BigQuery!')

    df_customers = extract_stripe_customers()
    print('Customers extracted!')
    upload_to_bigquery(df_customers, project_name='weather-project-geocoding-api', dataset_name="stripe_data", table_name="raw_customers")
    print('Customers uploaded to BigQuery!')





if __name__ == "__main__":
    main()