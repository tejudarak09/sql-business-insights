-- Q09: How do the customer segments (Consumer / Corporate / Home Office) compare?
SELECT
    c.segment                AS segment,
    COUNT(DISTINCT f.order_id)    AS orders,
    COUNT(DISTINCT f.customer_id) AS customers,
    ROUND(SUM(f.sales), 2)   AS revenue,
    ROUND(SUM(f.profit), 2) AS profit
FROM fact_order_line f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY 1
ORDER BY revenue DESC;
