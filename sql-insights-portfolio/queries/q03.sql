-- Q03: What does the month-by-month revenue trend look like?
SELECT
    substr(order_date, 1, 7) AS month,
    ROUND(SUM(sales), 2)     AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM fact_order_line
GROUP BY 1
ORDER BY 1;
