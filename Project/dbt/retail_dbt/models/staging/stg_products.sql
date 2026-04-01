SELECT
    product_id,
    product_name,
    sku_code,
    category_id,
    supplier_id,
    
    CAST(unit_cost AS FLOAT64) AS unit_cost,
    CAST(retail_price AS FLOAT64) AS retail_price,
    (retail_price - unit_cost) AS profit_per_unit,
    
    weight_kg,
    is_active,
    reorder_level,
    brand,
    color,
    material

FROM `retail-oltp-analytics-pipeline.retail_dataset.products_catalog`