-- Q15: What are the top 3 products in EACH category by revenue? (window function RANK)
WITH prod_rev AS (
    SELECT p.category, p.product_name, SUM(f.sales) AS revenue
    FROM fact_order_line f
    JOIN dim_product p ON f.product_id = p.product_id
    GROUP BY p.category, p.product_id, p.product_name
),
ranked AS (
    SELECT
        category,
        product_name,
        ROUND(revenue, 2) AS revenue,
        RANK() OVER (PARTITION BY category ORDER BY revenue DESC) AS rnk
    FROM prod_rev
)
SELECT category, product_name, revenue
FROM ranked
WHERE rnk <= 3
ORDER BY category, rnk;
