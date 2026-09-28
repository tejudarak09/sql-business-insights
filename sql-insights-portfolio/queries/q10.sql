-- Q10: Do bigger discounts destroy profit? (profit by discount band, using CASE)
SELECT
    CASE
        WHEN discount = 0    THEN 'No discount'
        WHEN discount <= 0.2 THEN 'Low discount (<=20%)'
        ELSE 'High discount (>20%)'
    END                    AS discount_band,
    COUNT(*)               AS order_lines,
    ROUND(AVG(profit), 2)  AS avg_profit_per_line,
    ROUND(SUM(profit), 2)  AS total_profit
FROM fact_order_line
GROUP BY 1
ORDER BY total_profit DESC;
