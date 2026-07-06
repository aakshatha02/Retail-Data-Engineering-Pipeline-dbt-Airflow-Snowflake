SELECT
    product_id,
    item,
    category,
    price
FROM {{source('raw', 'products')}}