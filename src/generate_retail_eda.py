"""Retail Sales Discovery Engine and Notebook Builder.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Generates publication figures and executes Task 1 EDA notebook.
"""

import os
import nbformat as nbf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.loaders import load_superstore
from src.cleaning import clean_superstore
from src.metrics import calculate_retail_kpis


def generate_retail_visualizations(df: pd.DataFrame, output_dir: str = "outputs/figures"):
    """Generate high-resolution visualization suite for retail sales discovery."""
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="muted")

    # 1. Monthly Sales Line Chart
    df_m = df.groupby("Order Year-Month")["Sales"].sum().reset_index()
    plt.figure(figsize=(14, 5))
    plt.plot(df_m["Order Year-Month"], df_m["Sales"], marker="o", color="#1f77b4", linewidth=2.5)
    plt.title("Monthly Sales Revenue Trajectory (2014 - 2017)", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Order Year-Month", fontsize=11)
    plt.ylabel("Sales ($)", fontsize=11)
    plt.xticks(rotation=45, ha="right", fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_monthly_sales_trend.png"), dpi=300)
    plt.close()

    # 2. Subcategory Revenue and Profit Rankings
    subcat = df.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False).reset_index()
    fig, ax1 = plt.subplots(figsize=(12, 6))
    sns.barplot(data=subcat, x="Sub-Category", y="Sales", color="#4a90e2", ax=ax1, label="Sales ($)")
    ax2 = ax1.twinx()
    sns.lineplot(data=subcat, x="Sub-Category", y="Profit", color="#d9534f", marker="o", linewidth=2.5, ax=ax2, label="Profit ($)")
    ax1.set_xticks(range(len(subcat)))
    ax1.set_xticklabels(subcat["Sub-Category"], rotation=45, ha="right")
    ax1.set_title("Sub-Category Sales Volume vs Net Profit Contribution", fontsize=14, fontweight="bold", pad=12)
    ax1.set_ylabel("Total Sales ($)", fontsize=11)
    ax2.set_ylabel("Total Profit ($)", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_category_revenue_profit.png"), dpi=300)
    plt.close()

    # 3. Regional Profitability Chart
    reg = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
    reg["Margin %"] = (reg["Profit"] / reg["Sales"]) * 100
    plt.figure(figsize=(9, 5))
    sns.barplot(data=reg, x="Region", y="Profit", palette="Blues_d")
    plt.title("Regional Net Profit Contribution", fontsize=14, fontweight="bold", pad=12)
    plt.ylabel("Total Profit ($)", fontsize=11)
    for i, row in reg.iterrows():
        plt.text(i, row["Profit"] / 2, f"{row['Margin %']:.1f}% Margin", ha="center", color="white", fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_regional_profitability.png"), dpi=300)
    plt.close()

    # 4. Customer Segment Comparison
    seg = df.groupby("Segment")[["Sales", "Profit"]].sum().reset_index()
    plt.figure(figsize=(8, 5))
    bar_width = 0.35
    x = np.arange(len(seg))
    plt.bar(x - bar_width/2, seg["Sales"], width=bar_width, label="Sales ($)", color="#2b5c8f")
    plt.bar(x + bar_width/2, seg["Profit"], width=bar_width, label="Profit ($)", color="#28a745")
    plt.xticks(x, seg["Segment"])
    plt.title("Customer Segment Commercial Performance", fontsize=14, fontweight="bold", pad=12)
    plt.ylabel("Amount ($)", fontsize=11)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_customer_segment_comparison.png"), dpi=300)
    plt.close()

    # 5. Discount vs Profit Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category", alpha=0.6, s=40, palette="Set2")
    plt.axhline(0, color="red", linestyle="--", linewidth=1.5, alpha=0.8)
    plt.title("Transaction Discount Level vs Profit Realization", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Discount Rate (0.0 to 1.0)", fontsize=11)
    plt.ylabel("Profit ($)", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_discount_vs_profit_scatter.png"), dpi=300)
    plt.close()

    # 6. Profit Margin Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df["Profit Margin %"].clip(-100, 100), bins=50, kde=True, color="#6f42c1")
    plt.axvline(0, color="red", linestyle="--", linewidth=1.5)
    plt.title("Transaction Profit Margin Distribution (Clipped at +/- 100%)", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Profit Margin (%)", fontsize=11)
    plt.ylabel("Order Line Count", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_profit_margin_distribution.png"), dpi=300)
    plt.close()

    # 7. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    num_cols = ["Sales", "Quantity", "Discount", "Profit", "Unit Price", "Days to Ship"]
    corr = df[num_cols].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, linewidths=0.5)
    plt.title("Correlation Matrix of Commercial Metrics", fontsize=14, fontweight="bold", pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "retail_correlation_heatmap.png"), dpi=300)
    plt.close()


def build_retail_notebook(filepath: str = "notebooks/01_retail_sales_eda.ipynb"):
    """Construct and execute the complete Task 1 EDA Jupyter Notebook."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    nb = nbf.v4.new_notebook()

    cells = []
    # Header
    cells.append(nbf.v4.new_markdown_cell("""# TASK 1: Retail Sales Discovery Engine
### Comprehensive Commercial Diagnostics, Profitability Profiling, and Discount Sensitivity Analysis

**Author**: Vijay Maheswari  
**Framework**: RISK Methodology (Reconnaissance, Intelligence, Solution, KPI Verification)  
**Dataset**: Retail Superstore Sales (9,994 validated records)
"""))

    # Cell 1: Imports and setup
    cells.append(nbf.v4.new_code_cell("""import sys
import os

# Ensure parent directory is in sys.path
for p in [os.path.abspath(".."), os.path.abspath(".")]:
    if p not in sys.path:
        sys.path.insert(0, p)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.loaders import load_superstore
from src.cleaning import clean_superstore
from src.metrics import calculate_retail_kpis
from src.validation import validate_superstore_schema

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'Arial'
"""))

    # Cell 2: Data Loading & Validation
    cells.append(nbf.v4.new_markdown_cell("""## 1. Data Ingestion & Quality Audit
We ingest the raw dataset, perform null-value and duplicate checks, and apply deterministic cleaning rules while preserving raw provenance.
"""))

    cells.append(nbf.v4.new_code_cell("""raw_df = load_superstore()
print(f"Raw dataset shape: {raw_df.shape}")

# Validate raw structure
audit_raw = validate_superstore_schema(raw_df)
print(audit_raw.summary())

# Clean dataset
df = clean_superstore(raw_df)
print(f"Cleaned dataset shape: {df.shape}")

# Validate cleaned structure
audit_clean = validate_superstore_schema(df)
print(audit_clean.summary())
"""))

    # Cell 3: Executive Scorecard
    cells.append(nbf.v4.new_markdown_cell("""## 2. Core Commercial Scorecard
We calculate the grand totals matching Power BI DAX definitions.
"""))

    cells.append(nbf.v4.new_code_cell("""kpis = calculate_retail_kpis(df)
for k, v in kpis.items():
    if not isinstance(v, pd.DataFrame):
        print(f"{k}: {v:,}" if isinstance(v, (int, float)) else f"{k}: {v}")
"""))

    # Cell 4: Visualizations
    cells.append(nbf.v4.new_markdown_cell("""## 3. Visual Analytics & Diagnostic Charts
We examine monthly sales trajectories, category profitability, regional disparities, and discount elasticity.
"""))

    cells.append(nbf.v4.new_code_cell("""from src.generate_retail_eda import generate_retail_visualizations

generate_retail_visualizations(df, "outputs/figures")
print("Visualizations rendered to outputs/figures/")
"""))

    # Cell 5: Discount Band Analysis
    cells.append(nbf.v4.new_markdown_cell("""## 4. Discount Sensitivity Breakdown
Isolating the commercial impact of discounting reveals a severe margin collapse when discounts surpass 20%.
"""))

    cells.append(nbf.v4.new_code_cell("""disc_perf = df.groupby("Discount Band", observed=False).agg(
    Order_Lines=("Order ID", "count"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)
disc_perf["Profit_Margin_%"] = (disc_perf["Total_Profit"] / disc_perf["Total_Sales"]) * 100
disc_perf["Sales_Share_%"] = (disc_perf["Total_Sales"] / df["Sales"].sum()) * 100
disc_perf
"""))

    # Cell 6: Subcategory Ranking
    cells.append(nbf.v4.new_markdown_cell("""## 5. Sub-Category Value Destruction & Value Creation
Analyzing the bottom vs top subcategories isolates structural product line loss leaders.
"""))

    cells.append(nbf.v4.new_code_cell("""subcat_diag = df.groupby(["Category", "Sub-Category"]).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Avg_Discount=("Discount", "mean")
).reset_index()
subcat_diag["Profit_Margin_%"] = (subcat_diag["Profit"] / subcat_diag["Sales"]) * 100
subcat_diag.sort_values("Profit", ascending=True)
"""))

    nb.cells = cells
    with open(filepath, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Saved notebook template to {filepath}")


if __name__ == "__main__":
    df = clean_superstore(load_superstore())
    generate_retail_visualizations(df)
    build_retail_notebook()
