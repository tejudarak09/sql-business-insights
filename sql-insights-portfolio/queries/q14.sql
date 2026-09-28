-- Q14: What is the running (cumulative) revenue total over time? (window function SUM)
WITH monthly AS (
    SELECT substr(order_date, 1, 7) AS month, SUM(sales) AS revenue
    FROM fact_order_line
    GROUP BY 1
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(SUM(revenue) OVER (
        ORDER BY month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 2) AS running_total
FROM monthly
ORDER BY month;
