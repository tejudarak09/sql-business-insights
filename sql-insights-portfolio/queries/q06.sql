-- Q06: What are the top 10 products by revenue?
SELECT
    p.product_name           AS product_name,
    p.category               AS category,
    p.sub_category           AS sub_category,
    ROUND(SUM(f.sales), 2)   AS revenue,
    ROUND(SUM(f.profit), 2) AS profit
FROM fact_order_line f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category, p.sub_category
ORDER BY revenue DESC
LIMIT 10;
