SELECT
  charge_id,
  customer_id,
  SAFE_CAST(amount AS FLOAT64) / 100 AS amount_usd,
  currency,
  status,
  TIMESTAMP_SECONDS(created) AS created_at
FROM {{ source('stripe_data', 'raw_charges') }}