-- Q18: Which sub-categories LOSE money overall? (negative total profit)
SELECT
    p.sub_category           AS sub_category,
    p.category               AS category,
    ROUND(SUM(f.sales), 2)   AS revenue,
    ROUND(SUM(f.profit), 2)  AS profit,
    COUNT(*)                 AS order_lines
FROM fact_order_line f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.sub_category, p.category
HAVING SUM(f.profit) < 0
ORDER BY profit;
