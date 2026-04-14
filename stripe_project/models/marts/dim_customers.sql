SELECT DISTINCT
  customer_id,
  email,
  created_at
FROM {{ ref('stg_customers') }}