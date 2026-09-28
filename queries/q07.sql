-- Q07: Who are the top 10 customers by revenue?
SELECT
    c.customer_name          AS customer_name,
    c.segment                AS segment,
    ROUND(SUM(f.sales), 2)   AS revenue,
    COUNT(DISTINCT f.order_id) AS orders
FROM fact_order_line f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name, c.segment
ORDER BY revenue DESC
LIMIT 10;
