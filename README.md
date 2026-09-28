# SQL Business Insights Portfolio

18 real business questions answered in SQL against a retail sales database —
from basic aggregations to CTEs and window functions. Every number below comes
from actually running the queries in `queries/` (see `results.md` for full outputs).

## Dataset

**"Sample - Superstore"** — the classic public retail dataset (one row per order line),
covering Jan 2014 – Dec 2017: **9,994 order lines, 5,009 orders, 793 customers, 1,862 products.**

- Source file used: `Sample - Superstore.csv`
- Downloaded from (public mirror): https://raw.githubusercontent.com/Lude71/Superstore-Sales-Performance-Dashboard/main/Sample%20-%20Superstore.csv
- The dataset originates from Tableau's "Sample – Superstore" workbook and is mirrored in many public repos / Kaggle.

## Setup (Windows)

```bat
python load_data.py     :: builds sales.db (star schema) from data\superstore.csv
python run_all.py       :: runs all 18 queries, writes results\qNN.csv + results.md
```

You can also open `sales.db` in [DB Browser for SQLite](https://sqlitebrowser.org/)
and run any file in `queries/` directly.

## Schema

```
dim_customer (customer_id PK, customer_name, segment)
dim_product  (product_id PK, product_name, category, sub_category)
fact_order_line (row_id PK, order_id, order_date, ship_date, ship_mode,
                 customer_id -> dim_customer, product_id -> dim_product,
                 country, city, state, postal_code, region,
                 sales, quantity, discount, profit)
```

Cleaning done by `load_data.py`: whitespace trimmed, dates `M/D/YYYY` → ISO `YYYY-MM-DD`,
numeric casts, blank postal codes → NULL.

## The 18 questions + one-line insights (all real outputs)

| # | Business question | Insight |
|---|---|---|
| 1 | What are the headline KPIs? | $2.30M revenue, $286K profit, 5,009 orders, 793 customers |
| 2 | How did revenue trend year over year? | Grew every year: $484K (2014) → $733K (2017) |
| 3 | Best month ever? | Nov 2017 — $118,448 revenue across 261 orders |
| 4 | Top category? | Technology: $836K revenue and $145K profit |
| 5 | Top region? | West: $725K revenue; South smallest at $392K |
| 6 | Top product? | Canon imageCLASS 2200 copier — $61.6K revenue |
| 7 | Top customer? | Sean Miller (Home Office) — $25,043 across 5 orders |
| 8 | Average order value? | $458.61 |
| 9 | Best customer segment? | Consumer: $1.16M revenue (51% of total) |
| 10 | Do discounts kill profit? | Yes — orders with >20% discount lost $135K total; no-discount orders made $321K |
| 11 | Repeat purchase rate? | 98.5% of customers ordered more than once in the 4-year period |
| 12 | Most used ship mode? | Standard Class: 2,994 orders (60%); Same Day averages 0 days |
| 13 | Month-over-month growth? | Tracked for all 48 months with `LAG()`; early-2014 shows 1000%+ growth off a tiny launch base |
| 14 | Cumulative revenue? | Running total (window `SUM`) reaches $2.30M by Dec 2017 |
| 15 | Top 3 products per category? | Ranked with `RANK()` — Canon copier leads Technology |
| 16 | Best customers by RFM? | Recency/Frequency/Monetary per customer; Sean Miller tops monetary at $25,043 |
| 17 | Do customers come back next year? | Retention improved: 73.5% (2014 cohort) → 87.5% (2016 cohort) |
| 18 | Any sub-category losing money? | Tables: –$17,725 profit on $207K revenue; also Bookcases (–$3,473) |

## Project structure

```
sql-insights-portfolio/
├── data/
│   └── superstore.csv        # raw dataset (latin-1)
├── queries/
│   ├── q01.sql ... q18.sql  # 18 numbered queries, basic -> advanced
├── results/
│   └── q01.csv ... q18.csv  # real outputs of each query
├── load_data.py              # builds sales.db (star schema + cleaning)
├── run_all.py                # runs all queries, writes results/ + results.md
├── sales.db                  # SQLite database (generated)
├── results.md                # all 18 questions + full result tables
├── interview_qa.md           # 8 interview Q&As based on this project
└── README.md
```

## Skills demonstrated

SQL (JOINs, GROUP BY, CTEs, window functions, CASE, date handling), SQLite,
Python (data loading/cleaning), star-schema data modeling.
