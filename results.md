# Query Results

All outputs below were produced by running the queries in `queries/` against `sales.db`.

## Q01: Q01: What are the headline KPIs of the business? (total revenue, total profit, order lines, distinct orders, distinct customers)

| total_revenue | total_profit | order_lines | orders | customers |
| --- | --- | --- | --- | --- |
| 2297200.86 | 286397.02 | 9994 | 5009 | 793 |

## Q02: Q02: How have revenue, profit and order volume trended year over year?

| year | revenue | profit | orders |
| --- | --- | --- | --- |
| 2014 | 484247.5 | 49543.97 | 969 |
| 2015 | 470532.51 | 61618.6 | 1038 |
| 2016 | 609205.6 | 81795.17 | 1315 |
| 2017 | 733215.26 | 93439.27 | 1687 |

## Q03: Q03: What does the month-by-month revenue trend look like?

| month | revenue | orders |
| --- | --- | --- |
| 2014-01 | 14236.9 | 32 |
| 2014-02 | 4519.89 | 28 |
| 2014-03 | 55691.01 | 71 |
| 2014-04 | 28295.35 | 66 |
| 2014-05 | 23648.29 | 69 |
| 2014-06 | 34595.13 | 66 |
| 2014-07 | 33946.39 | 65 |
| 2014-08 | 27909.47 | 72 |
| 2014-09 | 81777.35 | 130 |
| 2014-10 | 31453.39 | 78 |
| 2014-11 | 78628.72 | 151 |
| 2014-12 | 69545.62 | 141 |
| 2015-01 | 18174.08 | 29 |
| 2015-02 | 11951.41 | 36 |
| 2015-03 | 38726.25 | 79 |
| 2015-04 | 34195.21 | 72 |
| 2015-05 | 30131.69 | 74 |
| 2015-06 | 24797.29 | 68 |
| 2015-07 | 28765.33 | 66 |
| 2015-08 | 36898.33 | 68 |
| 2015-09 | 64595.92 | 140 |
| 2015-10 | 31404.92 | 87 |
| 2015-11 | 75972.56 | 158 |
| 2015-12 | 74919.52 | 161 |
| 2016-01 | 18542.49 | 48 |
| 2016-02 | 22978.82 | 45 |
| 2016-03 | 51715.88 | 86 |
| 2016-04 | 38750.04 | 89 |
| 2016-05 | 56987.73 | 108 |
| 2016-06 | 40344.53 | 97 |
| 2016-07 | 39261.96 | 96 |
| 2016-08 | 31115.37 | 90 |
| 2016-09 | 73410.02 | 192 |
| 2016-10 | 59687.75 | 105 |
| 2016-11 | 79411.97 | 183 |
| 2016-12 | 96999.04 | 176 |
| 2017-01 | 43971.37 | 69 |
| 2017-02 | 20301.13 | 53 |
| 2017-03 | 58872.35 | 118 |
| 2017-04 | 36521.54 | 116 |
| 2017-05 | 44261.11 | 118 |
| 2017-06 | 52981.73 | 133 |
| 2017-07 | 45264.42 | 111 |
| 2017-08 | 63120.89 | 111 |
| 2017-09 | 87866.65 | 226 |
| 2017-10 | 77776.92 | 147 |
| 2017-11 | 118447.82 | 261 |
| 2017-12 | 83829.32 | 224 |

## Q04: Q04: Which product category brings in the most revenue and profit?

| category | revenue | profit | order_lines |
| --- | --- | --- | --- |
| Technology | 836154.03 | 145454.95 | 1847 |
| Furniture | 741999.8 | 18451.27 | 2121 |
| Office Supplies | 719047.03 | 122490.8 | 6026 |

## Q05: Q05: Which sales region performs best?

| region | revenue | profit | orders |
| --- | --- | --- | --- |
| West | 725457.82 | 108418.45 | 1611 |
| East | 678781.24 | 91522.78 | 1401 |
| Central | 501239.89 | 39706.36 | 1175 |
| South | 391721.91 | 46749.43 | 822 |

## Q06: Q06: What are the top 10 products by revenue?

| product_name | category | sub_category | revenue | profit |
| --- | --- | --- | --- | --- |
| Canon imageCLASS 2200 Advanced Copier | Technology | Copiers | 61599.82 | 25199.93 |
| Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind | Office Supplies | Binders | 27453.38 | 7753.04 |
| Cisco TelePresence System EX90 Videoconferencing Unit | Technology | Machines | 22638.48 | -1811.08 |
| HON 5400 Series Task Chairs for Big and Tall | Furniture | Chairs | 21870.58 | 0.0 |
| GBC DocuBind TL300 Electric Binding System | Office Supplies | Binders | 19823.48 | 2233.51 |
| GBC Ibimaster 500 Manual ProClick Binding System | Office Supplies | Binders | 19024.5 | 760.98 |
| Hewlett Packard LaserJet 3310 Copier | Technology | Copiers | 18839.69 | 6983.88 |
| HP Designjet T520 Inkjet Large Format Printer - 24" Color | Technology | Machines | 18374.9 | 4094.98 |
| GBC DocuBind P400 Electric Binding System | Office Supplies | Binders | 17965.07 | -1878.17 |
| High Speed Automatic Electric Letter Opener | Office Supplies | Supplies | 17030.31 | -262.0 |

## Q07: Q07: Who are the top 10 customers by revenue?

| customer_name | segment | revenue | orders |
| --- | --- | --- | --- |
| Sean Miller | Home Office | 25043.05 | 5 |
| Tamara Chand | Corporate | 19052.22 | 5 |
| Raymond Buch | Consumer | 15117.34 | 6 |
| Tom Ashbrook | Home Office | 14595.62 | 4 |
| Adrian Barton | Consumer | 14473.57 | 10 |
| Ken Lonsdale | Consumer | 14175.23 | 12 |
| Sanjit Chand | Consumer | 14142.33 | 9 |
| Hunter Lopez | Consumer | 12873.3 | 6 |
| Sanjit Engle | Consumer | 12209.44 | 11 |
| Christopher Conant | Consumer | 12129.07 | 5 |

## Q08: Q08: What is the average order value (AOV)?

| avg_order_value | orders | revenue |
| --- | --- | --- |
| 458.61 | 5009 | 2297200.86 |

## Q09: Q09: How do the customer segments (Consumer / Corporate / Home Office) compare?

| segment | orders | customers | revenue | profit |
| --- | --- | --- | --- | --- |
| Consumer | 2586 | 409 | 1161401.34 | 134119.21 |
| Corporate | 1514 | 236 | 706146.37 | 91979.13 |
| Home Office | 909 | 148 | 429653.15 | 60298.68 |

## Q10: Q10: Do bigger discounts destroy profit? (profit by discount band, using CASE)

| discount_band | order_lines | avg_profit_per_line | total_profit |
| --- | --- | --- | --- |
| No discount | 4798 | 66.9 | 320987.6 |
| Low discount (<=20%) | 3803 | 26.5 | 100785.47 |
| High discount (>20%) | 1393 | -97.18 | -135376.06 |

## Q11: Q11: What share of customers bought more than once? (repeat purchase rate, using a CTE)

| customers | repeat_customers | repeat_rate_pct |
| --- | --- | --- |
| 793 | 781 | 98.49 |

## Q12: Q12: Which ship mode is used most, and how fast is each?

| ship_mode | orders | revenue | avg_ship_days |
| --- | --- | --- | --- |
| Standard Class | 2994 | 1358215.74 | 5.0 |
| Second Class | 964 | 459193.57 | 3.2 |
| First Class | 787 | 351428.42 | 2.2 |
| Same Day | 264 | 128363.13 | 0.0 |

## Q13: Q13: What is the month-over-month revenue growth? (window function LAG)

| month | revenue | mom_growth_pct |
| --- | --- | --- |
| 2014-01 | 14236.9 |  |
| 2014-02 | 4519.89 | -68.25 |
| 2014-03 | 55691.01 | 1132.13 |
| 2014-04 | 28295.35 | -49.19 |
| 2014-05 | 23648.29 | -16.42 |
| 2014-06 | 34595.13 | 46.29 |
| 2014-07 | 33946.39 | -1.88 |
| 2014-08 | 27909.47 | -17.78 |
| 2014-09 | 81777.35 | 193.01 |
| 2014-10 | 31453.39 | -61.54 |
| 2014-11 | 78628.72 | 149.98 |
| 2014-12 | 69545.62 | -11.55 |
| 2015-01 | 18174.08 | -73.87 |
| 2015-02 | 11951.41 | -34.24 |
| 2015-03 | 38726.25 | 224.03 |
| 2015-04 | 34195.21 | -11.7 |
| 2015-05 | 30131.69 | -11.88 |
| 2015-06 | 24797.29 | -17.7 |
| 2015-07 | 28765.33 | 16.0 |
| 2015-08 | 36898.33 | 28.27 |
| 2015-09 | 64595.92 | 75.06 |
| 2015-10 | 31404.92 | -51.38 |
| 2015-11 | 75972.56 | 141.91 |
| 2015-12 | 74919.52 | -1.39 |
| 2016-01 | 18542.49 | -75.25 |
| 2016-02 | 22978.82 | 23.93 |
| 2016-03 | 51715.88 | 125.06 |
| 2016-04 | 38750.04 | -25.07 |
| 2016-05 | 56987.73 | 47.06 |
| 2016-06 | 40344.53 | -29.2 |
| 2016-07 | 39261.96 | -2.68 |
| 2016-08 | 31115.37 | -20.75 |
| 2016-09 | 73410.02 | 135.93 |
| 2016-10 | 59687.75 | -18.69 |
| 2016-11 | 79411.97 | 33.05 |
| 2016-12 | 96999.04 | 22.15 |
| 2017-01 | 43971.37 | -54.67 |
| 2017-02 | 20301.13 | -53.83 |
| 2017-03 | 58872.35 | 190.0 |
| 2017-04 | 36521.54 | -37.96 |
| 2017-05 | 44261.11 | 21.19 |
| 2017-06 | 52981.73 | 19.7 |
| 2017-07 | 45264.42 | -14.57 |
| 2017-08 | 63120.89 | 39.45 |
| 2017-09 | 87866.65 | 39.2 |
| 2017-10 | 77776.92 | -11.48 |
| 2017-11 | 118447.82 | 52.29 |
| 2017-12 | 83829.32 | -29.23 |

## Q14: Q14: What is the running (cumulative) revenue total over time? (window function SUM)

| month | revenue | running_total |
| --- | --- | --- |
| 2014-01 | 14236.9 | 14236.9 |
| 2014-02 | 4519.89 | 18756.79 |
| 2014-03 | 55691.01 | 74447.8 |
| 2014-04 | 28295.35 | 102743.14 |
| 2014-05 | 23648.29 | 126391.43 |
| 2014-06 | 34595.13 | 160986.56 |
| 2014-07 | 33946.39 | 194932.95 |
| 2014-08 | 27909.47 | 222842.42 |
| 2014-09 | 81777.35 | 304619.77 |
| 2014-10 | 31453.39 | 336073.16 |
| 2014-11 | 78628.72 | 414701.88 |
| 2014-12 | 69545.62 | 484247.5 |
| 2015-01 | 18174.08 | 502421.57 |
| 2015-02 | 11951.41 | 514372.98 |
| 2015-03 | 38726.25 | 553099.24 |
| 2015-04 | 34195.21 | 587294.45 |
| 2015-05 | 30131.69 | 617426.13 |
| 2015-06 | 24797.29 | 642223.42 |
| 2015-07 | 28765.33 | 670988.75 |
| 2015-08 | 36898.33 | 707887.08 |
| 2015-09 | 64595.92 | 772483.0 |
| 2015-10 | 31404.92 | 803887.92 |
| 2015-11 | 75972.56 | 879860.49 |
| 2015-12 | 74919.52 | 954780.01 |
| 2016-01 | 18542.49 | 973322.5 |
| 2016-02 | 22978.82 | 996301.31 |
| 2016-03 | 51715.88 | 1048017.19 |
| 2016-04 | 38750.04 | 1086767.23 |
| 2016-05 | 56987.73 | 1143754.96 |
| 2016-06 | 40344.53 | 1184099.49 |
| 2016-07 | 39261.96 | 1223361.45 |
| 2016-08 | 31115.37 | 1254476.83 |
| 2016-09 | 73410.02 | 1327886.85 |
| 2016-10 | 59687.75 | 1387574.6 |
| 2016-11 | 79411.97 | 1466986.56 |
| 2016-12 | 96999.04 | 1563985.61 |
| 2017-01 | 43971.37 | 1607956.98 |
| 2017-02 | 20301.13 | 1628258.11 |
| 2017-03 | 58872.35 | 1687130.47 |
| 2017-04 | 36521.54 | 1723652.0 |
| 2017-05 | 44261.11 | 1767913.11 |
| 2017-06 | 52981.73 | 1820894.84 |
| 2017-07 | 45264.42 | 1866159.25 |
| 2017-08 | 63120.89 | 1929280.14 |
| 2017-09 | 87866.65 | 2017146.79 |
| 2017-10 | 77776.92 | 2094923.72 |
| 2017-11 | 118447.82 | 2213371.54 |
| 2017-12 | 83829.32 | 2297200.86 |

## Q15: Q15: What are the top 3 products in EACH category by revenue? (window function RANK)

| category | product_name | revenue |
| --- | --- | --- |
| Furniture | HON 5400 Series Task Chairs for Big and Tall | 21870.58 |
| Furniture | Riverside Palais Royal Lawyers Bookcase, Royale Cherry Finish | 15610.97 |
| Furniture | Bretford Rectangular Conference Table Tops | 12995.29 |
| Office Supplies | Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind | 27453.38 |
| Office Supplies | GBC DocuBind TL300 Electric Binding System | 19823.48 |
| Office Supplies | GBC Ibimaster 500 Manual ProClick Binding System | 19024.5 |
| Technology | Canon imageCLASS 2200 Advanced Copier | 61599.82 |
| Technology | Cisco TelePresence System EX90 Videoconferencing Unit | 22638.48 |
| Technology | Hewlett Packard LaserJet 3310 Copier | 18839.69 |

## Q16: Q16: RFM-lite — for each customer: recency (days since last order), frequency (order count), monetary (total revenue). Who are the top 20 by monetary?

| customer_name | segment | recency_days | frequency | monetary |
| --- | --- | --- | --- | --- |
| Sean Miller | Home Office | 79 | 5 | 25043.05 |
| Tamara Chand | Corporate | 399 | 5 | 19052.22 |
| Raymond Buch | Consumer | 96 | 6 | 15117.34 |
| Tom Ashbrook | Home Office | 69 | 4 | 14595.62 |
| Adrian Barton | Consumer | 41 | 10 | 14473.57 |
| Ken Lonsdale | Consumer | 47 | 12 | 14175.23 |
| Sanjit Chand | Consumer | 349 | 9 | 14142.33 |
| Hunter Lopez | Consumer | 43 | 6 | 12873.3 |
| Sanjit Engle | Consumer | 9 | 11 | 12209.44 |
| Christopher Conant | Consumer | 43 | 5 | 12129.07 |
| Todd Sumrall | Corporate | 36 | 6 | 11891.75 |
| Greg Tran | Consumer | 36 | 11 | 11820.12 |
| Becky Martin | Consumer | 307 | 4 | 11789.63 |
| Seth Vernon | Consumer | 101 | 10 | 11470.95 |
| Caroline Jumper | Consumer | 189 | 8 | 11164.97 |
| Clay Ludtke | Consumer | 284 | 12 | 10880.55 |
| Maria Etezadi | Home Office | 42 | 10 | 10663.73 |
| Karen Ferguson | Home Office | 97 | 7 | 10604.27 |
| Bill Shonely | Corporate | 558 | 5 | 10501.65 |
| Edward Hooks | Corporate | 135 | 12 | 10310.88 |

## Q17: Q17: Of the customers active in a year, what % come back the next year? (year-over-year retention, using a CTE + self join)

| year | customers | retained_next_year | retention_pct |
| --- | --- | --- | --- |
| 2014 | 595 | 437 | 73.45 |
| 2015 | 573 | 452 | 78.88 |
| 2016 | 638 | 558 | 87.46 |
| 2017 | 693 | 0 | 0.0 |

## Q18: Q18: Which sub-categories LOSE money overall? (negative total profit)

| sub_category | category | revenue | profit | order_lines |
| --- | --- | --- | --- | --- |
| Tables | Furniture | 206965.53 | -17725.48 | 319 |
| Bookcases | Furniture | 114880.0 | -3472.56 | 228 |
| Supplies | Office Supplies | 46673.54 | -1189.1 | 190 |
