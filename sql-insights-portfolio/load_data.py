"""
load_data.py — Build a clean SQLite star schema from the Sample Superstore CSV.

Usage (Windows):
    python load_data.py

Reads  data/superstore.csv  (latin-1 encoded) and creates  sales.db  with:
    dim_customer  (customer_id PK, customer_name, segment)
    dim_product   (product_id PK, product_name, category, sub_category)
    fact_order_line (one row per order line, FKs to the dimensions)

Cleaning applied:
  - strip whitespace from all text fields
  - Order/Ship dates M/D/YYYY -> ISO YYYY-MM-DD (TEXT, SQLite-friendly)
  - Sales / Quantity / Discount / Profit cast to numeric
  - blank Postal Code -> NULL (11 rows in the source have no postal code)
"""
import csv
import os
import sqlite3
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "data", "superstore.csv")
DB_PATH = os.path.join(BASE, "sales.db")


def iso_date(s: str) -> str | None:
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Unparseable date: {s!r}")


def num(s: str, kind=float):
    s = (s or "").strip()
    if s == "":
        return None
    return kind(s)


def main() -> None:
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    customers: dict[str, tuple] = {}
    products: dict[str, tuple] = {}
    facts: list[tuple] = []

    with open(CSV_PATH, newline="", encoding="latin-1") as f:
        reader = csv.DictReader(f)
        for r in reader:
            cid = r["Customer ID"].strip()
            customers.setdefault(cid, (cid, r["Customer Name"].strip(), r["Segment"].strip()))

            pid = r["Product ID"].strip()
            products.setdefault(
                pid,
                (pid, r["Product Name"].strip(), r["Category"].strip(), r["Sub-Category"].strip()),
            )

            postal = r["Postal Code"].strip() or None
            facts.append(
                (
                    int(r["Row ID"]),
                    r["Order ID"].strip(),
                    iso_date(r["Order Date"]),
                    iso_date(r["Ship Date"]),
                    r["Ship Mode"].strip(),
                    cid,
                    pid,
                    r["Country"].strip(),
                    r["City"].strip(),
                    r["State"].strip(),
                    postal,
                    r["Region"].strip(),
                    num(r["Sales"]),
                    num(r["Quantity"], int),
                    num(r["Discount"]),
                    num(r["Profit"]),
                )
            )

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    cur.execute(
        """CREATE TABLE dim_customer (
               customer_id   TEXT PRIMARY KEY,
               customer_name TEXT NOT NULL,
               segment       TEXT NOT NULL)"""
    )
    cur.execute(
        """CREATE TABLE dim_product (
               product_id   TEXT PRIMARY KEY,
               product_name TEXT NOT NULL,
               category     TEXT NOT NULL,
               sub_category TEXT NOT NULL)"""
    )
    cur.execute(
        """CREATE TABLE fact_order_line (
               row_id      INTEGER PRIMARY KEY,
               order_id    TEXT NOT NULL,
               order_date  TEXT NOT NULL,   -- ISO YYYY-MM-DD
               ship_date   TEXT,
               ship_mode   TEXT,
               customer_id TEXT NOT NULL REFERENCES dim_customer(customer_id),
               product_id  TEXT NOT NULL REFERENCES dim_product(product_id),
               country     TEXT,
               city        TEXT,
               state       TEXT,
               postal_code TEXT,            -- NULL where missing in source
               region      TEXT,
               sales       REAL NOT NULL,
               quantity    INTEGER NOT NULL,
               discount    REAL,
               profit      REAL)"""
    )

    cur.executemany("INSERT INTO dim_customer VALUES (?,?,?)", customers.values())
    cur.executemany("INSERT INTO dim_product VALUES (?,?,?,?)", products.values())
    cur.executemany(
        """INSERT INTO fact_order_line
           (row_id, order_id, order_date, ship_date, ship_mode, customer_id, product_id,
            country, city, state, postal_code, region, sales, quantity, discount, profit)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        facts,
    )
    con.commit()

    # ---- verification ----
    for tbl in ("dim_customer", "dim_product", "fact_order_line"):
        n = cur.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        print(f"{tbl:16s}: {n:,} rows")
    n_orders = cur.execute("SELECT COUNT(DISTINCT order_id) FROM fact_order_line").fetchone()[0]
    rev = cur.execute("SELECT ROUND(SUM(sales), 2) FROM fact_order_line").fetchone()[0]
    dmin, dmax = cur.execute("SELECT MIN(order_date), MAX(order_date) FROM fact_order_line").fetchone()
    n_null_postal = cur.execute("SELECT COUNT(*) FROM fact_order_line WHERE postal_code IS NULL").fetchone()[0]
    print(f"distinct orders : {n_orders:,}")
    print(f"total revenue   : ${rev:,.2f}")
    print(f"date range      : {dmin} -> {dmax}")
    print(f"NULL postal_code: {n_null_postal}")
    con.close()
    print("\nWrote", DB_PATH)


if __name__ == "__main__":
    main()
