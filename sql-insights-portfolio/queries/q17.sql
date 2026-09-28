-- Q17: Of the customers active in a year, what % come back the next year?
-- (year-over-year retention, using a CTE + self join)
WITH yearly AS (
    SELECT DISTINCT customer_id, substr(order_date, 1, 4) AS yr
    FROM fact_order_line
)
SELECT
    a.yr AS year,
    COUNT(DISTINCT a.customer_id) AS customers,
    COUNT(DISTINCT b.customer_id) AS retained_next_year,
    ROUND(100.0 * COUNT(DISTINCT b.customer_id) / COUNT(DISTINCT a.customer_id), 2) AS retention_pct
FROM yearly a
LEFT JOIN yearly b
    ON a.customer_id = b.customer_id
    AND CAST(b.yr AS INTEGER) = CAST(a.yr AS INTEGER) + 1
GROUP BY 1
ORDER BY 1;
