SELECT
    CAST(InvoiceID AS NUMBER)      AS invoice_id,
    CAST(Product_ID AS NUMBER)     AS product_id,
    CAST(Quantity AS NUMBER)       AS quantity,
    CAST(Price AS NUMBER(10,2))    AS price,
    CAST(Line_Total AS NUMBER(10,2)) AS line_total
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY InvoiceID, Product_ID, Quantity
               ORDER BY InvoiceID
           ) AS rn
    FROM {{ source('raw', 'invoice_items') }}
)
WHERE rn = 1