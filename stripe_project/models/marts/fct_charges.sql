SELECT
  charge_id,
  customer_id,
  amount_usd,
  currency,
  status,
  created_at
FROM {{ ref('stg_charges') }}