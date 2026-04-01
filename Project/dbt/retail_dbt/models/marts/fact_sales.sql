{{ config(
    materialized='table',
    partition_by={
      "field": "sale_date",
      "data_type": "date"
    },
    cluster_by=["product_id", "store_id"]
) }}


SELECT
    -- primary key
    s.txn_id,

    -- time
    s.sale_date,
    s.event_time,

    -- customer
    s.customer_id,
    c.customer_name,
    c.loyalty_tier,

    -- product
    s.product_id,
    p.product_name,
    p.category_id,
    pc.category_name,
    pc.department,

    -- store
    s.store_id,
    st.store_name,
    st.region,

    -- metrics 🔥
    s.quantity,
    p.retail_price,
    p.unit_cost,
    
    (p.retail_price - p.unit_cost) AS profit_per_unit,
    (s.quantity * p.retail_price) AS revenue,

    -- payment
    s.payment_method

FROM {{ ref('stg_sales') }} s

LEFT JOIN {{ ref('stg_customers') }} c
    ON s.customer_id = c.customer_id

LEFT JOIN {{ ref('stg_products') }} p
    ON s.product_id = p.product_id

LEFT JOIN {{ ref('stg_categories') }} pc
    ON p.category_id = pc.category_id

LEFT JOIN {{ ref('stg_stores') }} st
    ON s.store_id = st.store_id