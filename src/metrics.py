"""Analytical KPI Engines and Financial Scenario Simulator.

Part of RISK V3 - Autonomous Business Analytics & Decision Intelligence Engine.
Provides audited calculation functions for Retail, Churn, and Financial intelligence.
"""

from typing import Dict, Any, List
import pandas as pd
import numpy as np


# ==============================================================================
# TASK 1 & 2: RETAIL SALES KPI ENGINE
# ==============================================================================

def calculate_retail_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """Compute enterprise retail KPIs matching Power BI DAX definitions."""
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())
    total_quantity = int(df["Quantity"].sum())
    total_orders = int(df["Order ID"].nunique())
    total_customers = int(df["Customer ID"].nunique())

    profit_margin_pct = (total_profit / total_sales * 100) if total_sales > 0 else 0.0
    aov = (total_sales / total_orders) if total_orders > 0 else 0.0

    # Negative profit transactions
    neg_profit_mask = df["Profit"] < 0
    neg_profit_count = int(neg_profit_mask.sum())
    neg_profit_total = float(df.loc[neg_profit_mask, "Profit"].sum())

    # Segment breakdowns
    by_segment = df.groupby("Segment", as_index=False).agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    by_segment["Profit Margin %"] = (by_segment["Profit"] / by_segment["Sales"]) * 100

    # Category breakdowns
    by_category = df.groupby("Category", as_index=False).agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    by_category["Profit Margin %"] = (by_category["Profit"] / by_category["Sales"]) * 100

    # Region breakdowns
    by_region = df.groupby("Region", as_index=False).agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    by_region["Profit Margin %"] = (by_region["Profit"] / by_region["Sales"]) * 100

    # Discount Band profitability
    by_discount_band = df.groupby("Discount Band", observed=False, as_index=False).agg(
        Orders=("Order ID", "count"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    by_discount_band["Profit Margin %"] = np.where(
        by_discount_band["Sales"] > 0,
        (by_discount_band["Profit"] / by_discount_band["Sales"]) * 100,
        0.0
    )

    return {
        "Total Sales": round(total_sales, 2),
        "Total Profit": round(total_profit, 2),
        "Total Quantity": total_quantity,
        "Total Orders": total_orders,
        "Total Customers": total_customers,
        "Profit Margin %": round(profit_margin_pct, 2),
        "Average Order Value": round(aov, 2),
        "Negative Profit Order Lines": neg_profit_count,
        "Total Negative Profit Loss": round(neg_profit_total, 2),
        "By Segment": by_segment,
        "By Category": by_category,
        "By Region": by_region,
        "By Discount Band": by_discount_band,
    }


# ==============================================================================
# TASK 3: CUSTOMER CHURN & RETENTION KPI ENGINE
# ==============================================================================

def calculate_churn_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """Compute customer cohort, churn, and retention metrics."""
    eligible_customers = int(len(df))
    churn_mask = df["Churn"].astype(str).str.strip().str.lower() == "yes"
    churned_customers = int(churn_mask.sum())
    retained_customers = eligible_customers - churned_customers

    churn_rate_pct = (churned_customers / eligible_customers * 100) if eligible_customers > 0 else 0.0
    retention_rate_pct = (retained_customers / eligible_customers * 100) if eligible_customers > 0 else 0.0

    # Tenure Cohorts
    cohort_summary = df.groupby("Tenure Cohort", observed=False, as_index=False).agg(
        Total=("customerID", "count"),
        Churned=("Churn_Numeric", "sum")
    )
    cohort_summary["Retained"] = cohort_summary["Total"] - cohort_summary["Churned"]
    cohort_summary["Churn Rate %"] = (cohort_summary["Churned"] / cohort_summary["Total"]) * 100
    cohort_summary["Retention Rate %"] = (cohort_summary["Retained"] / cohort_summary["Total"]) * 100

    # Contract breakdown
    contract_summary = df.groupby("Contract", as_index=False).agg(
        Total=("customerID", "count"),
        Churned=("Churn_Numeric", "sum")
    )
    contract_summary["Churn Rate %"] = (contract_summary["Churned"] / contract_summary["Total"]) * 100

    # Payment Method breakdown
    payment_summary = df.groupby("PaymentMethod", as_index=False).agg(
        Total=("customerID", "count"),
        Churned=("Churn_Numeric", "sum")
    )
    payment_summary["Churn Rate %"] = (payment_summary["Churned"] / payment_summary["Total"]) * 100

    # High-Risk Segment
    high_risk_mask = df["Is High Risk Profile"] == 1
    high_risk_total = int(high_risk_mask.sum())
    high_risk_churned = int(df.loc[high_risk_mask, "Churn_Numeric"].sum())
    high_risk_rate = (high_risk_churned / high_risk_total * 100) if high_risk_total > 0 else 0.0

    return {
        "Eligible Customers": eligible_customers,
        "Churned Customers": churned_customers,
        "Retained Customers": retained_customers,
        "Churn Rate %": round(churn_rate_pct, 2),
        "Retention Rate %": round(retention_rate_pct, 2),
        "Tenure Cohorts": cohort_summary,
        "Contract Breakdown": contract_summary,
        "Payment Breakdown": payment_summary,
        "High Risk Cohort Total": high_risk_total,
        "High Risk Churn Rate %": round(high_risk_rate, 2),
    }


# ==============================================================================
# TASK 4: FINANCIAL PERFORMANCE & SCENARIO SIMULATOR
# ==============================================================================

def calculate_financial_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """Calculate baseline corporate financial performance indicators."""
    total_sales = float(df["Sales"].sum())
    total_gross_sales = float(df["Gross Sales"].sum())
    total_discounts = float(df["Discounts"].sum())
    total_cogs = float(df["COGS"].sum())
    total_profit = float(df["Profit"].sum())
    total_units = float(df["Units Sold"].sum())

    gross_profit_margin_pct = (total_profit / total_sales * 100) if total_sales > 0 else 0.0
    cogs_ratio_pct = (total_cogs / total_sales * 100) if total_sales > 0 else 0.0
    discount_ratio_pct = (total_discounts / total_gross_sales * 100) if total_gross_sales > 0 else 0.0

    # Breakdown by Segment
    by_segment = df.groupby("Segment", as_index=False).agg(
        Sales=("Sales", "sum"),
        COGS=("COGS", "sum"),
        Profit=("Profit", "sum"),
        Units=("Units Sold", "sum")
    )
    by_segment["Profit Margin %"] = (by_segment["Profit"] / by_segment["Sales"]) * 100

    # Breakdown by Country
    by_country = df.groupby("Country", as_index=False).agg(
        Sales=("Sales", "sum"),
        COGS=("COGS", "sum"),
        Profit=("Profit", "sum")
    )
    by_country["Profit Margin %"] = (by_country["Profit"] / by_country["Sales"]) * 100

    return {
        "Total Sales": round(total_sales, 2),
        "Total Gross Sales": round(total_gross_sales, 2),
        "Total Discounts": round(total_discounts, 2),
        "Total COGS": round(total_cogs, 2),
        "Total Profit": round(total_profit, 2),
        "Total Units Sold": round(total_units, 2),
        "Gross Profit Margin %": round(gross_profit_margin_pct, 2),
        "COGS Ratio %": round(cogs_ratio_pct, 2),
        "Effective Discount %": round(discount_ratio_pct, 2),
        "By Segment": by_segment,
        "By Country": by_country,
    }


def simulate_financial_scenario(
    df: pd.DataFrame,
    discount_pct_delta: float = 0.0,
    cogs_pct_delta: float = 0.0,
    volume_pct_delta: float = 0.0,
) -> Dict[str, Any]:
    """Execute what-if sensitivity simulation against corporate financial data.

    Parameters:
        discount_pct_delta: Fractional change in discount magnitude (e.g. -0.10 for 10% discount cut).
        cogs_pct_delta: Fractional change in per-unit COGS (e.g. +0.05 for 5% supply-chain inflation).
        volume_pct_delta: Fractional change in unit volume (e.g. +0.08 for 8% sales expansion).

    Returns:
        Structured scenario ledger comparing baseline vs simulated results.
    """
    baseline = calculate_financial_kpis(df)

    # Simulated unit volume
    sim_units = df["Units Sold"] * (1.0 + volume_pct_delta)
    sim_gross_sales = sim_units * df["Sale Price"]
    sim_discounts = df["Discounts"] * (1.0 + discount_pct_delta) * (1.0 + volume_pct_delta)
    sim_sales = sim_gross_sales - sim_discounts
    sim_cogs = (df["COGS"] / df["Units Sold"]) * (1.0 + cogs_pct_delta) * sim_units
    sim_profit = sim_sales - sim_cogs

    sim_total_sales = float(sim_sales.sum())
    sim_total_cogs = float(sim_cogs.sum())
    sim_total_profit = float(sim_profit.sum())
    sim_margin_pct = (sim_total_profit / sim_total_sales * 100) if sim_total_sales > 0 else 0.0

    sales_delta = sim_total_sales - baseline["Total Sales"]
    profit_delta = sim_total_profit - baseline["Total Profit"]
    margin_delta = sim_margin_pct - baseline["Gross Profit Margin %"]

    return {
        "parameters": {
            "discount_pct_delta": discount_pct_delta,
            "cogs_pct_delta": cogs_pct_delta,
            "volume_pct_delta": volume_pct_delta,
        },
        "baseline": {
            "Total Sales": baseline["Total Sales"],
            "Total COGS": baseline["Total COGS"],
            "Total Profit": baseline["Total Profit"],
            "Gross Profit Margin %": baseline["Gross Profit Margin %"],
        },
        "simulated": {
            "Total Sales": round(sim_total_sales, 2),
            "Total COGS": round(sim_total_cogs, 2),
            "Total Profit": round(sim_total_profit, 2),
            "Gross Profit Margin %": round(sim_margin_pct, 2),
        },
        "variance": {
            "Sales Delta ($)": round(sales_delta, 2),
            "Sales Delta (%)": round((sales_delta / baseline["Total Sales"]) * 100, 2),
            "Profit Delta ($)": round(profit_delta, 2),
            "Profit Delta (%)": round((profit_delta / baseline["Total Profit"]) * 100, 2),
            "Margin Delta (bps)": round(margin_delta * 100, 2),
        },
    }
