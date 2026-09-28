# Interview Q&A — SQL Business Insights Portfolio

Short answers grounded in this project's real queries. Fresher-tone, no jargon dumps.

**1. What is a window function? Give an example from your project.**
A window function calculates across a set of rows related to the current row, without
collapsing them like GROUP BY does. In q14 I used `SUM(revenue) OVER (ORDER BY month
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` to get a running cumulative
revenue total next to each month's own revenue.

**2. What is the difference between a CTE and a subquery?**
A CTE (`WITH ...`) is a named temporary result set you define once at the top and can
reference (even multiple times) in the main query — it makes complex queries readable.
A subquery is nested inline inside another query. I used CTEs in q11 (repeat rate),
q13/q14 (monthly totals before applying window functions), and q17 (yearly activity).

**3. How did you compute the repeat purchase rate?**
In q11 I built a CTE counting distinct orders per customer, then counted how many
customers had more than one order and divided by total customers. Result: 98.5%
ordered more than once across the four years.

**4. How would you find the top 5 customers by revenue?**
JOIN the fact table to dim_customer, GROUP BY customer, SUM(sales), ORDER BY the sum
DESC, LIMIT 5. That's exactly q07 (I did top 10) — Sean Miller came first at $25,043.

**5. What is a JOIN, and which did you use most?**
A JOIN combines rows from two tables on a matching key. I mostly used INNER JOIN to
attach dimension attributes — e.g. joining fact_order_line to dim_product for category
names (q04, q06, q15, q18). q17 uses a LEFT JOIN so years with no returning customers
still appear in the retention report.

**6. How do you handle NULLs?**
With `COALESCE` to substitute defaults, `IS NULL` / `IS NOT NULL` filters, and by
designing aggregations carefully (most aggregates ignore NULLs). In load_data.py I
converted blank postal codes to NULL instead of keeping empty strings, so the
database distinguishes "unknown" from real values.

**7. What is one insight from the data that surprised you?**
Discounts destroy profit here: order lines with more than 20% discount lost $135,376
in total (q10), and the Tables sub-category lost $17,725 overall despite $207K in
revenue (q18). Selling more isn't the same as earning more.

**8. What would you add if you had more time?**
A proper date dimension table, profit-margin % per product, a cohort heatmap of
monthly retention, and the same queries ported to PostgreSQL to show they transfer
across databases.
