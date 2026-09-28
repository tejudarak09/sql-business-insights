-- Q01: What are the headline KPIs of the business?
-- (total revenue, total profit, order lines, distinct orders, distinct customers)
SELECT
    ROUND(SUM(sales), 2)       AS total_revenue,
    ROUND(SUM(profit), 2)      AS total_profit,
    COUNT(*)                   AS order_lines,
    COUNT(DISTINCT order_id)   AS orders,
    COUNT(DISTINCT customer_id) AS customers
FROM fact_order_line;
