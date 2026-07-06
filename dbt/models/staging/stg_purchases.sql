SELECT
    CAST(InvoiceID AS NUMBER) AS invoice_id,
    CAST(date AS DATE) AS purchase_date,
    CAST(CustomerID AS NUMBER) AS customer_id,
    CAST(product_id AS NUMBER) AS product_id,
    CAST(quantity AS NUMBER) AS quantity
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY InvoiceID, CustomerID, product_id, quantity
               ORDER BY InvoiceID
           ) AS rn
    FROM {{ source('raw', 'purchases') }}
)
WHERE rn = 1

