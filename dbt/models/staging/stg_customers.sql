SELECT
    CAST(customerid AS NUMBER) AS customer_id,
    customer_type
FROM {{ source('raw', 'customer')}}