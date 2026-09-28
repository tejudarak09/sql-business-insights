-- Q13: What is the month-over-month revenue growth? (window function LAG)
WITH monthly AS (
    SELECT substr(order_date, 1, 7) AS month, SUM(sales) AS revenue
    FROM fact_order_line
    GROUP BY 1
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
          / LAG(revenue) OVER (ORDER BY month), 2) AS mom_growth_pct
FROM monthly
ORDER BY month;
