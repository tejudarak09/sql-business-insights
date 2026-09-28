-- Q11: What share of customers bought more than once? (repeat purchase rate, using a CTE)
WITH orders_per_customer AS (
    SELECT customer_id, COUNT(DISTINCT order_id) AS n_orders
    FROM fact_order_line
    GROUP BY 1
)
SELECT
    COUNT(*) AS customers,
    SUM(CASE WHEN n_orders > 1 THEN 1 ELSE 0 END) AS repeat_customers,
    ROUND(100.0 * SUM(CASE WHEN n_orders > 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS repeat_rate_pct
FROM orders_per_customer;
