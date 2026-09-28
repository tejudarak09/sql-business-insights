import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------------
st.set_page_config(page_title="Sales Insights Dashboard", layout="wide")

DB_PATH = Path(__file__).parent / "sales.db"
if not DB_PATH.exists():
    st.error(
        "sales.db not found next to app.py. "
        "Extract this dashboard inside your sql-insights-portfolio folder "
        "(the one containing sales.db) and re-run."
    )
    st.stop()


@st.cache_data
def run_query(sql, params=()):
    with sqlite3.connect(DB_PATH) as con:
        return pd.read_sql_query(sql, con, params=params)


def money(x):
    return f"${x:,.0f}"


def build_where(years, categories, regions):
    """WHERE clause shared by every chart/table so filters apply everywhere."""
    conds, params = [], []
    if years:
        conds.append(f"substr(f.order_date,1,4) IN ({','.join('?' * len(years))})")
        params += list(years)
    if categories:
        conds.append(f"p.category IN ({','.join('?' * len(categories))})")
        params += list(categories)
    if regions:
        conds.append(f"f.region IN ({','.join('?' * len(regions))})")
        params += list(regions)
    where = f"WHERE {' AND '.join(conds)}" if conds else ""
    return where, params


# ----------------------------------------------------------------------------
# Sidebar filters
# ----------------------------------------------------------------------------
st.sidebar.header("Filters")
years = st.sidebar.multiselect(
    "Year", ["2014", "2015", "2016", "2017"],
    default=["2014", "2015", "2016", "2017"],
)
categories = st.sidebar.multiselect(
    "Category", ["Furniture", "Office Supplies", "Technology"],
    default=["Furniture", "Office Supplies", "Technology"],
)
regions = st.sidebar.multiselect(
    "Region", ["Central", "East", "South", "West"],
    default=["Central", "East", "South", "West"],
)
# Empty selection = no filter (friendlier than an empty dashboard)
where, params = build_where(years, categories, regions)
JOIN = "FROM fact_order_line f LEFT JOIN dim_product p ON f.product_id = p.product_id"

# ----------------------------------------------------------------------------
# Title + KPIs
# ----------------------------------------------------------------------------
st.title("Sales Insights Dashboard")
st.caption("18 SQL analyses over 9,994 retail order lines (2014–2017) — every number below is a live query.")

kpi = run_query(
    f"""SELECT ROUND(SUM(f.sales),2) AS revenue,
               ROUND(SUM(f.profit),2) AS profit,
               COUNT(*) AS lines,
               COUNT(DISTINCT f.order_id) AS orders,
               COUNT(DISTINCT f.customer_id) AS customers
        {JOIN} {where}""",
    params,
).iloc[0]
revenue, profit, orders, customers = (
    kpi["revenue"] or 0, kpi["profit"] or 0, kpi["orders"] or 0, kpi["customers"] or 0,
)
aov = revenue / orders if orders else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Revenue", money(revenue))
c2.metric("Profit", money(profit))
c3.metric("Orders", f"{orders:,}")
c4.metric("Customers", f"{customers:,}")
c5.metric("Avg Order Value", money(aov))

# ----------------------------------------------------------------------------
# Monthly revenue trend
# ----------------------------------------------------------------------------
st.subheader("Monthly revenue trend")
trend = run_query(
    f"""SELECT substr(f.order_date,1,7) AS month, ROUND(SUM(f.sales),2) AS revenue
        {JOIN} {where}
        GROUP BY 1 ORDER BY 1""",
    params,
)
fig_trend = px.line(trend, x="month", y="revenue", markers=True,
                    labels={"month": "Month", "revenue": "Revenue ($)"})
fig_trend.update_layout(xaxis_tickangle=-45, height=380, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_trend, use_container_width=True)

# ----------------------------------------------------------------------------
# Category / Region bars
# ----------------------------------------------------------------------------
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Revenue by category")
    cat = run_query(
        f"""SELECT p.category, ROUND(SUM(f.sales),2) AS revenue
            {JOIN} {where}
            GROUP BY 1 ORDER BY 2 DESC""",
        params,
    )
    fig_cat = px.bar(cat, x="category", y="revenue",
                     labels={"category": "Category", "revenue": "Revenue ($)"},
                     color="revenue", color_continuous_scale="Blues")
    fig_cat.update_layout(height=380, margin=dict(l=10, r=10, t=10, b=10), coloraxis_showscale=False)
    st.plotly_chart(fig_cat, use_container_width=True)
with col_b:
    st.subheader("Revenue by region")
    reg = run_query(
        f"""SELECT f.region, ROUND(SUM(f.sales),2) AS revenue
            {JOIN} {where}
            GROUP BY 1 ORDER BY 2 DESC""",
        params,
    )
    fig_reg = px.bar(reg, x="region", y="revenue",
                     labels={"region": "Region", "revenue": "Revenue ($)"},
                     color="revenue", color_continuous_scale="Greens")
    fig_reg.update_layout(height=380, margin=dict(l=10, r=10, t=10, b=10), coloraxis_showscale=False)
    st.plotly_chart(fig_reg, use_container_width=True)

# ----------------------------------------------------------------------------
# Discount vs profit — the money finding
# ----------------------------------------------------------------------------
st.subheader("⚠️ Do discounts destroy profit? Yes.")
disc = run_query(
    f"""SELECT CASE WHEN f.discount = 0 THEN 'No discount'
                    WHEN f.discount <= 0.2 THEN 'Low discount (1-20%)'
                    ELSE 'High discount (>20%)' END AS band,
               ROUND(SUM(f.profit),2) AS profit,
               COUNT(*) AS lines
        {JOIN} {where}
        GROUP BY 1""",
    params,
)
band_order = ["No discount", "Low discount (1-20%)", "High discount (>20%)"]
disc["band"] = pd.Categorical(disc["band"], categories=band_order, ordered=True)
disc = disc.sort_values("band")
disc["color"] = disc["profit"].apply(lambda v: "#d62728" if v < 0 else "#2ca02c")
fig_disc = px.bar(disc, x="band", y="profit", color="color",
                 color_discrete_map="identity",
                 labels={"band": "Discount band", "profit": "Total profit ($)"},
                 text="profit")
fig_disc.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
fig_disc.update_layout(height=400, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
st.plotly_chart(fig_disc, use_container_width=True)
m1, m2, m3 = st.columns(3)
for col, band in zip((m1, m2, m3), band_order):
    row = disc[disc["band"] == band]
    if not row.empty:
        col.metric(f"Profit — {band}", money(row.iloc[0]["profit"]),
                   f"{int(row.iloc[0]['lines']):,} order lines")

# ----------------------------------------------------------------------------
# Top 10 tables
# ----------------------------------------------------------------------------
t1, t2 = st.columns(2)
with t1:
    st.subheader("Top 10 products by revenue")
    prod = run_query(
        f"""SELECT p.product_name AS product, p.category,
                   ROUND(SUM(f.sales),2) AS revenue, ROUND(SUM(f.profit),2) AS profit
            {JOIN} {where}
            GROUP BY 1, 2 ORDER BY 3 DESC LIMIT 10""",
        params,
    )
    st.dataframe(prod, use_container_width=True, hide_index=True)
with t2:
    st.subheader("Top 10 customers by spend")
    cust = run_query(
        f"""SELECT c.customer_name AS customer, c.segment,
                   ROUND(SUM(f.sales),2) AS revenue,
                   COUNT(DISTINCT f.order_id) AS orders
            FROM fact_order_line f JOIN dim_customer c ON f.customer_id = c.customer_id
            LEFT JOIN dim_product p ON f.product_id = p.product_id
            {where}
            GROUP BY 1, 2 ORDER BY 3 DESC LIMIT 10""",
        params,
    )
    st.dataframe(cust, use_container_width=True, hide_index=True)

# ----------------------------------------------------------------------------
# Key insights (from results.md — full-dataset findings)
# ----------------------------------------------------------------------------
st.subheader("Key insights")
st.markdown(
    "- **Discounts above 20% lost $135,376 in profit**, while full-price orders earned $320,988 — "
    "heavy discounting destroys profit.\n"
    "- **Revenue grew every year**: $484K (2014) → $733K (2017), with orders nearly doubling.\n"
    "- **Technology is the profit engine** ($836K revenue, $145K profit); the **Tables** sub-category "
    "lost money despite $207K in revenue.\n"
    "- **Retention improved from 73.5% to 87.5%**, and 98.5% of customers bought more than once — "
    "growth came from keeping customers, not just finding new ones."
)
