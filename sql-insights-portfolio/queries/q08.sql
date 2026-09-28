-- Q08: What is the average order value (AOV)?
SELECT
    ROUND(SUM(sales) * 1.0 / COUNT(DISTINCT order_id), 2) AS avg_order_value,
    COUNT(DISTINCT order_id)                             AS orders,
    ROUND(SUM(sales), 2)                                 AS revenue
FROM fact_order_line;
