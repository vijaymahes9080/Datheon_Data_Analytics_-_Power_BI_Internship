"""Power BI Star Schema Dimensional Modeler.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Builds FactSales, DimProduct, DimCustomer, DimGeography, and DimDate tables,
validates referential integrity, and compiles notebook 02.
"""

import os
import nbformat as nbf
import pandas as pd
import numpy as np
from src.loaders import load_superstore
from src.cleaning import clean_superstore

PROCESSED_DIR = "data/processed"


def build_star_schema(df: pd.DataFrame):
    """Deconstruct cleaned dataset into 3NF / Star Schema relational tables."""
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # 1. FactSales
    fact_cols = [
        "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
        "Customer ID", "Postal Code", "Product ID", "Sales", "Quantity",
        "Discount", "Profit"
    ]
    fact_sales = df[fact_cols].copy()

    # 2. DimProduct
    dim_product = df[["Product ID", "Product Name", "Category", "Sub-Category"]].drop_duplicates(subset=["Product ID"]).copy()

    # 3. DimCustomer
    dim_customer = df[["Customer ID", "Customer Name", "Segment"]].drop_duplicates(subset=["Customer ID"]).copy()

    # 4. DimGeography
    dim_geography = df[["Postal Code", "City", "State", "Region", "Country"]].drop_duplicates(subset=["Postal Code"]).copy()

    # 5. DimDate
    min_date = df["Order Date"].min()
    max_date = max(df["Order Date"].max(), df["Ship Date"].max())
    dates = pd.date_range(min_date, max_date, freq="D")
    dim_date = pd.DataFrame({"Date": dates})
    dim_date["DateKey"] = dim_date["Date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["Year"] = dim_date["Date"].dt.year
    dim_date["Quarter"] = dim_date["Date"].dt.to_period("Q").astype(str)
    dim_date["QuarterNumber"] = dim_date["Date"].dt.quarter
    dim_date["Month"] = dim_date["Date"].dt.month
    dim_date["MonthName"] = dim_date["Date"].dt.strftime("%B")
    dim_date["YearMonth"] = dim_date["Date"].dt.strftime("%Y-%m")
    dim_date["Day"] = dim_date["Date"].dt.day
    dim_date["DayOfWeek"] = dim_date["Date"].dt.day_name()
    dim_date["DayOfWeekNumber"] = dim_date["Date"].dt.dayofweek + 1
    dim_date["IsWeekend"] = dim_date["DayOfWeekNumber"].isin([6, 7]).astype(int)

    # Referential Integrity Assertions
    assert fact_sales["Product ID"].isin(dim_product["Product ID"]).all(), "Integrity Error: Orphan Product ID"
    assert fact_sales["Customer ID"].isin(dim_customer["Customer ID"]).all(), "Integrity Error: Orphan Customer ID"
    assert fact_sales["Postal Code"].isin(dim_geography["Postal Code"]).all(), "Integrity Error: Orphan Postal Code"
    assert fact_sales["Order Date"].isin(dim_date["Date"]).all(), "Integrity Error: Orphan Order Date"

    # Save to data/processed/
    fact_sales.to_csv(os.path.join(PROCESSED_DIR, "FactSales.csv"), index=False)
    dim_product.to_csv(os.path.join(PROCESSED_DIR, "DimProduct.csv"), index=False)
    dim_customer.to_csv(os.path.join(PROCESSED_DIR, "DimCustomer.csv"), index=False)
    dim_geography.to_csv(os.path.join(PROCESSED_DIR, "DimGeography.csv"), index=False)
    dim_date.to_csv(os.path.join(PROCESSED_DIR, "DimDate.csv"), index=False)

    return {
        "FactSales": fact_sales,
        "DimProduct": dim_product,
        "DimCustomer": dim_customer,
        "DimGeography": dim_geography,
        "DimDate": dim_date,
    }


def build_powerbi_prep_notebook(filepath: str = "notebooks/02_powerbi_data_preparation.ipynb"):
    """Construct and execute the Task 2 Power BI Data Preparation Notebook."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    nb = nbf.v4.new_notebook()

    cells = []
    cells.append(nbf.v4.new_markdown_cell("""# TASK 2: Power BI Data Modeling & Preparation
### Star Schema Architecture, Referential Integrity Verification, and Dimensional Normalization

**Author**: Vijay Maheswari  
**Framework**: RISK Methodology — Solution Development & Engineering  
**Output Tables**: FactSales, DimProduct, DimCustomer, DimGeography, DimDate
"""))

    cells.append(nbf.v4.new_code_cell("""import sys
import os

# Ensure parent directory is in sys.path
for p in [os.path.abspath(".."), os.path.abspath(".")]:
    if p not in sys.path:
        sys.path.insert(0, p)

import pandas as pd
import numpy as np
from src.loaders import load_superstore
from src.cleaning import clean_superstore
from src.build_powerbi_model import build_star_schema
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 1. Load Validated Retail Data
We load the validated retail sales records and inspect dimensional keys before decomposition.
"""))

    cells.append(nbf.v4.new_code_cell("""raw_df = load_superstore()
clean_df = clean_superstore(raw_df)
print(f"Cleaned source records: {clean_df.shape}")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 2. Dimensional Decomposition & Star Schema Generation
We construct `FactSales` (order line grain) and 4 conforming dimension tables (`DimProduct`, `DimCustomer`, `DimGeography`, `DimDate`).
"""))

    cells.append(nbf.v4.new_code_cell("""tables = build_star_schema(clean_df)
for name, df_tbl in tables.items():
    print(f"{name:15}: {df_tbl.shape[0]:>6} rows | {df_tbl.shape[1]:>2} columns")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 3. Referential Integrity Audit
We verify that 100% of foreign keys in `FactSales` resolve to existing dimension keys (zero orphan records).
"""))

    cells.append(nbf.v4.new_code_cell("""fact = tables["FactSales"]
dim_p = tables["DimProduct"]
dim_c = tables["DimCustomer"]
dim_g = tables["DimGeography"]
dim_d = tables["DimDate"]

print("Orphan Product IDs :", (~fact["Product ID"].isin(dim_p["Product ID"])).sum())
print("Orphan Customer IDs:", (~fact["Customer ID"].isin(dim_c["Customer ID"])).sum())
print("Orphan Postal Codes:", (~fact["Postal Code"].isin(dim_g["Postal Code"])).sum())
print("Orphan Order Dates :", (~fact["Order Date"].isin(dim_d["Date"])).sum())
print("Referential integrity test passed: 100% valid relationships!")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 4. Reconcile Star Schema Aggregates Against Cleaned Source
We confirm that aggregating `FactSales` matches the single-table source down to the exact cent.
"""))

    cells.append(nbf.v4.new_code_cell("""source_sales = clean_df["Sales"].sum()
source_profit = clean_df["Profit"].sum()
fact_sales = fact["Sales"].sum()
fact_profit = fact["Profit"].sum()

print(f"Source Sales: ${source_sales:,.2f} | Fact Sales: ${fact_sales:,.2f} | Match: {source_sales == fact_sales}")
print(f"Source Profit: ${source_profit:,.2f} | Fact Profit: ${fact_profit:,.2f} | Match: {source_profit == fact_profit}")
"""))

    nb.cells = cells
    with open(filepath, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Saved Power BI preparation notebook to {filepath}")


if __name__ == "__main__":
    df = clean_superstore(load_superstore())
    build_star_schema(df)
    build_powerbi_prep_notebook()
