SELECT
  customer_id,
  email,
  TIMESTAMP_SECONDS(created) AS created_at
FROM {{ source('stripe_data', 'raw_customers') }}