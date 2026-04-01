SELECT
    customer_id,
    CONCAT(first_name, ' ', last_name) AS customer_name,
    email,
    phone,
    date_of_birth,
    gender,
    city,
    country,
    loyalty_tier,
    registration_date

FROM `retail-oltp-analytics-pipeline.retail_dataset.customers_master`