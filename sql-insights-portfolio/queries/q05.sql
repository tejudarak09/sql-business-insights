-- Q05: Which sales region performs best?
SELECT
    region,
    ROUND(SUM(sales), 2)      AS revenue,
    ROUND(SUM(profit), 2)     AS profit,
    COUNT(DISTINCT order_id) AS orders
FROM fact_order_line
GROUP BY 1
ORDER BY revenue DESC;
