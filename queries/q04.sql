-- Q04: Which product category brings in the most revenue and profit?
SELECT
    p.category              AS category,
    ROUND(SUM(f.sales), 2)  AS revenue,
    ROUND(SUM(f.profit), 2) AS profit,
    COUNT(*)                AS order_lines
FROM fact_order_line f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY 1
ORDER BY revenue DESC;
