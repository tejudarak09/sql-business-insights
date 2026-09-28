"""
run_all.py — Execute every query in queries/ against sales.db.

Usage (Windows):
    python run_all.py

Writes:
    results/qNN.csv  — one CSV per query (with header row)
    results.md       — all questions + results as Markdown tables

Exits non-zero (loudly) if ANY query fails.
"""
import csv
import glob
import os
import sqlite3
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "sales.db")
QDIR = os.path.join(BASE, "queries")
RDIR = os.path.join(BASE, "results")


def main() -> None:
    os.makedirs(RDIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(QDIR, "q*.sql")))
    assert len(files) == 18, f"expected 18 query files, found {len(files)}"

    con = sqlite3.connect(DB_PATH)
    md_lines = ["# Query Results", "", "All outputs below were produced by running the queries in `queries/` against `sales.db`.", ""]

    for path in files:
        qid = os.path.splitext(os.path.basename(path))[0]  # q01
        sql = open(path, encoding="utf-8").read()
        # business question = first comment line(s) starting with --
        question = " ".join(
            line.lstrip("- ").strip() for line in sql.splitlines() if line.strip().startswith("--")
        )
        try:
            cur = con.execute(sql)
        except Exception as e:  # noqa: BLE001 — fail loudly by design
            print(f"FAILED {qid}: {e}", file=sys.stderr)
            sys.exit(1)
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()

        csv_path = os.path.join(RDIR, f"{qid}.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(cols)
            w.writerows(rows)

        md_lines.append(f"## {qid.upper()}: {question}")
        md_lines.append("")
        md_lines.append("| " + " | ".join(cols) + " |")
        md_lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
        for r in rows:
            md_lines.append("| " + " | ".join("" if v is None else str(v) for v in r) + " |")
        md_lines.append("")
        print(f"{qid}: OK ({len(rows)} rows) -> results/{qid}.csv")

    with open(os.path.join(BASE, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    con.close()
    print("\nAll 18 queries ran successfully. See results.md")


if __name__ == "__main__":
    main()
