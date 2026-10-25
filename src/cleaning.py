"""Dataset Cleaning, Sanitization, and Feature Engineering Module.

Part of RISK V3 - Autonomous Business Analytics & Decision Intelligence Engine.
Implements non-destructive, deterministic transformations for all raw datasets.
"""

from typing import Tuple
import pandas as pd
import numpy as np


def clean_superstore(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich the Retail Superstore dataset.

    Preserves raw data, filters empty/padding rows, standardizes dates,
    imputes missing Postal Codes, and constructs calendar features.
    """
    df = df_raw.copy()

    # Drop blank/padding rows where Order ID or Sales is NaN
    df = df.dropna(subset=["Order ID", "Sales", "Profit"]).copy()

    # Deduplicate exact duplicate rows if any
    df = df.drop_duplicates()

    # Parse dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Calendar and time features
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Quarter"] = df["Order Date"].dt.to_period("Q").astype(str)
    df["Order Month"] = df["Order Date"].dt.month
    df["Order Month Name"] = df["Order Date"].dt.strftime("%B")
    df["Order Year-Month"] = df["Order Date"].dt.strftime("%Y-%m")
    df["Order DayOfWeek"] = df["Order Date"].dt.day_name()

    # Handle Postal Code (Burlington, VT missing values -> 5408)
    df["Postal Code"] = df["Postal Code"].fillna(5408).astype(int)

    # Core commercial metrics
    df["Sales"] = df["Sales"].astype(float)
    df["Profit"] = df["Profit"].astype(float)
    df["Quantity"] = df["Quantity"].astype(int)
    df["Discount"] = df["Discount"].astype(float)

    # Unit price & profit margin
    df["Unit Price"] = df["Sales"] / df["Quantity"]
    df["Profit Margin %"] = np.where(df["Sales"] > 0, (df["Profit"] / df["Sales"]) * 100, 0.0)

    # Discount tiers for sensitivity analysis
    bins = [-0.01, 0.0, 0.10, 0.20, 1.0]
    labels = ["None (0%)", "Low (0-10%]", "Medium (10-20%]", "High (>20%)"]
    df["Discount Band"] = pd.cut(df["Discount"], bins=bins, labels=labels)

    # Shipping duration
    df["Days to Ship"] = (df["Ship Date"] - df["Order Date"]).dt.days

    return df.reset_index(drop=True)


def clean_telco_churn(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich the Telco Customer Churn dataset.

    Converts TotalCharges, handles zero-tenure new subscribers,
    creates standardized tenure cohort groups, and binary indicators.
    """
    df = df_raw.copy()

    # Strip whitespace in column names and text values
    df.columns = [c.strip() for c in df.columns]

    # Convert TotalCharges: 11 blank entries correspond to tenure == 0
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].astype(str).str.strip(), errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0.0)

    # Tenure cohorts in 12-month increments
    tenure_bins = [-1, 12, 24, 36, 48, 60, 72]
    tenure_labels = ["0-12m", "13-24m", "25-36m", "37-48m", "49-60m", "61-72m"]
    df["Tenure Cohort"] = pd.cut(df["tenure"], bins=tenure_bins, labels=tenure_labels)

    # Binary flags for modeling & aggregation
    df["Churn_Numeric"] = (df["Churn"].str.strip().str.lower() == "yes").astype(int)
    df["SeniorCitizen"] = df["SeniorCitizen"].astype(int)

    # Service count index
    service_cols = [
        "PhoneService", "MultipleLines", "InternetService",
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies"
    ]

    def _has_service(val: str) -> int:
        val_str = str(val).lower().strip()
        return 1 if val_str in ("yes", "dsl", "fiber optic") else 0

    df["Active Service Count"] = df[service_cols].apply(
        lambda row: sum(_has_service(v) for v in row), axis=1
    )

    # High risk indicator: Month-to-month + Fiber Optic + Electronic check
    df["Is High Risk Profile"] = (
        (df["Contract"] == "Month-to-month")
        & (df["InternetService"] == "Fiber optic")
        & (df["PaymentMethod"] == "Electronic check")
    ).astype(int)

    return df.reset_index(drop=True)


def clean_financial_sample(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich the Corporate Financial Sample dataset.

    Trims whitespaces from column names, normalizes date and numeric fields,
    and calculates standard financial ratio metrics.
    """
    df = df_raw.copy()

    # Strip whitespaces from column headers (e.g. ' Sales' -> 'Sales')
    df.columns = [c.strip() for c in df.columns]

    # Ensure correct data types
    numeric_cols = [
        "Units Sold", "Manufacturing Price", "Sale Price", "Gross Sales",
        "Discounts", "Sales", "COGS", "Profit"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Date normalization
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)
    df["Year-Month"] = df["Date"].dt.strftime("%Y-%m")

    # Financial ratios
    df["Gross Profit Margin %"] = np.where(df["Sales"] > 0, (df["Profit"] / df["Sales"]) * 100, 0.0)
    df["COGS Ratio %"] = np.where(df["Sales"] > 0, (df["COGS"] / df["Sales"]) * 100, 0.0)
    df["Effective Discount %"] = np.where(df["Gross Sales"] > 0, (df["Discounts"] / df["Gross Sales"]) * 100, 0.0)

    # Standardize Discount Band
    if "Discount Band" in df.columns:
        df["Discount Band"] = df["Discount Band"].astype(str).str.strip().str.title()

    return df.reset_index(drop=True)
