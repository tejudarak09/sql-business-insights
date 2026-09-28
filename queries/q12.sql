-- Q12: Which ship mode is used most, and how fast is each?
SELECT
    ship_mode,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(sales), 2)     AS revenue,
    ROUND(AVG(julianday(ship_date) - julianday(order_date)), 1) AS avg_ship_days
FROM fact_order_line
GROUP BY 1
ORDER BY revenue DESC;
