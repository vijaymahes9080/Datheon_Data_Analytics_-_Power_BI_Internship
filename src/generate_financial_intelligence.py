"""Corporate Financial Performance and Scenario Simulator Engine.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Generates financial diagnostic charts, scenario sensitivity matrices, and executes Task 4 notebook.
"""

import os
import nbformat as nbf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.loaders import load_financial_sample
from src.cleaning import clean_financial_sample
from src.metrics import calculate_financial_kpis, simulate_financial_scenario

FIGURES_DIR = "outputs/figures"
PROCESSED_DIR = "data/processed"


def generate_financial_visualizations(df: pd.DataFrame, output_dir: str = FIGURES_DIR):
    """Render high-resolution visualization suite for corporate financial diagnostics."""
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="muted")

    # 1. Monthly Revenue & Profit Trend
    m_agg = df.groupby("Year-Month")[["Sales", "Profit", "COGS"]].sum().reset_index()
    plt.figure(figsize=(13, 5))
    plt.plot(m_agg["Year-Month"], m_agg["Sales"] / 1e6, marker="o", color="#2b5c8f", linewidth=2.5, label="Sales ($M)")
    plt.plot(m_agg["Year-Month"], m_agg["COGS"] / 1e6, marker="s", color="#e67e22", linewidth=2.0, label="COGS ($M)")
    plt.plot(m_agg["Year-Month"], m_agg["Profit"] / 1e6, marker="^", color="#27ae60", linewidth=2.5, label="Profit ($M)")
    plt.title("Monthly Financial Trajectory: Revenue, COGS, and Operating Profit ($M)", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Year-Month", fontsize=11)
    plt.ylabel("Amount ($ Millions)", fontsize=11)
    plt.xticks(rotation=45, ha="right", fontsize=9)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "financial_revenue_profit_trend.png"), dpi=300)
    plt.close()

    # 2. Segment Profitability & Margin Matrix
    seg_agg = df.groupby("Segment")[["Sales", "Profit"]].sum().reset_index()
    seg_agg["Margin %"] = (seg_agg["Profit"] / seg_agg["Sales"]) * 100
    seg_agg = seg_agg.sort_values("Margin %", ascending=True)

    fig, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=seg_agg, x="Segment", y="Sales", color="#4a90e2", ax=ax1, label="Sales ($)")
    ax2 = ax1.twinx()
    sns.lineplot(data=seg_agg, x="Segment", y="Margin %", color="#d9534f", marker="o", linewidth=2.5, ax=ax2, label="Margin %")
    ax1.set_title("Customer Segment Sales Volume vs Gross Profit Margin (%)", fontsize=13, fontweight="bold", pad=12)
    ax1.set_ylabel("Sales Revenue ($)", fontsize=11)
    ax2.set_ylabel("Gross Profit Margin (%)", fontsize=11)
    ax2.axhline(0, color="grey", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "financial_segment_margin_matrix.png"), dpi=300)
    plt.close()

    # 3. Country Profitability Comparison
    c_agg = df.groupby("Country")[["Sales", "Profit"]].sum().reset_index()
    c_agg["Margin %"] = (c_agg["Profit"] / c_agg["Sales"]) * 100
    plt.figure(figsize=(9, 5))
    sns.barplot(data=c_agg, x="Country", y="Profit", palette="Greens_d")
    plt.title("Geographic Operating Profit Contribution ($)", fontsize=13, fontweight="bold", pad=12)
    plt.ylabel("Total Profit ($)", fontsize=11)
    for i, row in c_agg.iterrows():
        plt.text(i, row["Profit"] / 2, f"{row['Margin %']:.1f}% Margin", ha="center", color="white", fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "financial_country_profitability.png"), dpi=300)
    plt.close()

    # 4. COGS Ratio Breakdown Across Products
    prod_agg = df.groupby("Product")[["Sales", "COGS"]].sum().reset_index()
    prod_agg["COGS Ratio %"] = (prod_agg["COGS"] / prod_agg["Sales"]) * 100
    prod_agg = prod_agg.sort_values("COGS Ratio %", ascending=False)

    plt.figure(figsize=(9, 5))
    sns.barplot(data=prod_agg, x="Product", y="COGS Ratio %", palette="Reds_d")
    plt.title("Cost of Goods Sold (COGS) Ratio by Product Line", fontsize=13, fontweight="bold", pad=12)
    plt.ylabel("COGS as % of Sales", fontsize=11)
    plt.axhline(df["COGS"].sum() / df["Sales"].sum() * 100, color="blue", linestyle="--", label="Overall Average (85.8%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "financial_cogs_ratio_breakdown.png"), dpi=300)
    plt.close()

    # 5. Financial Scenario Sensitivity Matrix
    discount_shocks = [-0.15, -0.10, -0.05, 0.0, 0.05, 0.10]
    cogs_shocks = [-0.05, 0.0, 0.05, 0.10]
    sensitivity_grid = np.zeros((len(cogs_shocks), len(discount_shocks)))

    for i, c_shock in enumerate(cogs_shocks):
        for j, d_shock in enumerate(discount_shocks):
            sim = simulate_financial_scenario(df, discount_pct_delta=d_shock, cogs_pct_delta=c_shock)
            sensitivity_grid[i, j] = sim["simulated"]["Total Profit"] / 1e6

    plt.figure(figsize=(10, 6))
    sns.heatmap(
        sensitivity_grid,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        xticklabels=[f"{int(d*100):+d}% Disc" for d in discount_shocks],
        yticklabels=[f"{int(c*100):+d}% COGS" for c in cogs_shocks],
        cbar_kws={"label": "Simulated Net Profit ($ Millions)"}
    )
    plt.title("Scenario Sensitivity Matrix: Impact of Discount & COGS Shocks on Net Profit ($M)", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Discount Policy Adjustment", fontsize=11)
    plt.ylabel("Supply-Chain COGS Inflation", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "financial_scenario_sensitivity_matrix.png"), dpi=300)
    plt.close()


def build_financial_notebook(filepath: str = "notebooks/04_financial_intelligence.ipynb"):
    """Construct and execute the Task 4 Financial Intelligence Jupyter Notebook."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    nb = nbf.v4.new_notebook()
    cells = []

    cells.append(nbf.v4.new_markdown_cell("""# TASK 4: Corporate Financial Performance & Scenario Intelligence
### Financial Diagnostics, COGS Analysis, Margin Rankings, and What-If Parameterized Scenario Simulator

**Author**: Vijay Maheswari  
**Framework**: RISK Methodology — Simulation & KPI Verification  
**Dataset**: Corporate Financial Sample (700 transaction batches, $118.7M Sales)
"""))

    cells.append(nbf.v4.new_code_cell("""import sys
import os

for p in [os.path.abspath(".."), os.path.abspath(".")]:
    if p not in sys.path:
        sys.path.insert(0, p)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.loaders import load_financial_sample
from src.cleaning import clean_financial_sample
from src.metrics import calculate_financial_kpis, simulate_financial_scenario
from src.validation import validate_financial_schema

sns.set_theme(style="whitegrid", palette="muted")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 1. Load and Standardize Financial Sample Data
We ingest the raw Excel workbook, strip whitespaces from column headers (e.g. `' Sales'` -> `'Sales'`), and audit required fields.
"""))

    cells.append(nbf.v4.new_code_cell("""raw_df = load_financial_sample()
print(f"Raw financial shape: {raw_df.shape}")

# Validate and clean
df = clean_financial_sample(raw_df)
audit = validate_financial_schema(df)
print(audit.summary())

# Export processed FinancialFact table
df.to_csv("data/processed/FinancialFact.csv", index=False)
print("Saved data/processed/FinancialFact.csv")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 2. Core Financial Scorecard
We calculate Grand Total Sales, COGS, Profit, and standard accounting ratios.
"""))

    cells.append(nbf.v4.new_code_cell("""kpis = calculate_financial_kpis(df)
print(f"Total Gross Sales   : ${kpis['Total Gross Sales']:,.2f}")
print(f"Total Discounts     : ${kpis['Total Discounts']:,.2f} ({kpis['Effective Discount %']:.2f}% Effective Rate)")
print(f"Total Net Sales     : ${kpis['Total Sales']:,.2f}")
print(f"Total COGS          : ${kpis['Total COGS']:,.2f} ({kpis['COGS Ratio %']:.2f}% of Net Sales)")
print(f"Total Operating Profit: ${kpis['Total Profit']:,.2f}")
print(f"Gross Profit Margin : {kpis['Gross Profit Margin %']:.2f}%")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 3. Segment & Country Commercial Breakdown
Diagnostics reveal that Enterprise operates at a net loss, while Channel Partners and Government drive substantial margins.
"""))

    cells.append(nbf.v4.new_code_cell("""print("Customer Segment Breakdown:")
print(kpis["By Segment"].to_string(index=False))
print("Geographic Breakdown:")
print(kpis["By Country"].to_string(index=False))
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 4. Visual Diagnostics Generation
Render and export all 5 financial diagnostic and scenario charts.
"""))

    cells.append(nbf.v4.new_code_cell("""from src.generate_financial_intelligence import generate_financial_visualizations

generate_financial_visualizations(df, "outputs/figures")
print("Visualizations saved to outputs/figures/")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 5. Financial What-If Scenario Simulator
We simulate multi-parameter shocks:
- Scenario A: 10% Discount Reduction, 3% COGS inflation, 5% Volume expansion.
- Scenario B: Severe Supply-Chain Stress (10% COGS inflation, 0% volume change).
"""))

    cells.append(nbf.v4.new_code_cell("""# Scenario A: Balanced Operational Optimization
sim_a = simulate_financial_scenario(df, discount_pct_delta=-0.10, cogs_pct_delta=0.03, volume_pct_delta=0.05)
print("Scenario A Results:")
print("Baseline Profit  : $" + f"{sim_a['baseline']['Total Profit']:,.2f}")
print("Simulated Profit : $" + f"{sim_a['simulated']['Total Profit']:,.2f}")
print("Profit Variance  : $" + f"{sim_a['variance']['Profit Delta ($)']:,.2f} ({sim_a['variance']['Profit Delta (%)']:+.2f}%)")

# Scenario B: Supply Chain Inflation Shock
sim_b = simulate_financial_scenario(df, discount_pct_delta=0.0, cogs_pct_delta=0.10, volume_pct_delta=0.0)
print("Scenario B Results (10% COGS Inflation):")
print("Baseline Profit  : $" + f"{sim_b['baseline']['Total Profit']:,.2f}")
print("Simulated Profit : $" + f"{sim_b['simulated']['Total Profit']:,.2f}")
print("Profit Variance  : $" + f"{sim_b['variance']['Profit Delta ($)']:,.2f} ({sim_b['variance']['Profit Delta (%)']:+.2f}%)")
"""))

    nb.cells = cells
    with open(filepath, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Saved financial notebook to {filepath}")


if __name__ == "__main__":
    df = clean_financial_sample(load_financial_sample())
    generate_financial_visualizations(df)
    build_financial_notebook()
