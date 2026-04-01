SELECT
    txn_id,
    customer_id,
    product_id,
    store_id,
    staff_id,
    quantity,
    payment_method,
    
    event_time,
    DATE(event_time) AS sale_date

FROM `retail-oltp-analytics-pipeline.retail_dataset.sales_raw_oltp`