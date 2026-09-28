-- Q16: RFM-lite — for each customer: recency (days since last order),
-- frequency (order count), monetary (total revenue). Who are the top 20 by monetary?
WITH rfm AS (
    SELECT
        customer_id,
        CAST(julianday((SELECT MAX(order_date) FROM fact_order_line))
             - julianday(MAX(order_date)) AS INTEGER) AS recency_days,
        COUNT(DISTINCT order_id) AS frequency,
        ROUND(SUM(sales), 2)     AS monetary
    FROM fact_order_line
    GROUP BY 1
)
SELECT c.customer_name, c.segment, r.recency_days, r.frequency, r.monetary
FROM rfm r
JOIN dim_customer c ON r.customer_id = c.customer_id
ORDER BY r.monetary DESC
LIMIT 20;
