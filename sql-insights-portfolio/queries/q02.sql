-- Q02: How have revenue, profit and order volume trended year over year?
SELECT
    substr(order_date, 1, 4)      AS year,
    ROUND(SUM(sales), 2)          AS revenue,
    ROUND(SUM(profit), 2)        AS profit,
    COUNT(DISTINCT order_id)     AS orders
FROM fact_order_line
GROUP BY 1
ORDER BY 1;
