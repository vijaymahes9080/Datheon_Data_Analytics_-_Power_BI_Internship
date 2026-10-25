"""Data Validation and Schema Integrity Module.

Part of RISK V3 - Autonomous Business Analytics & Decision Intelligence Engine.
Implements automated quality audits, schema enforcement, and boundary checks.
"""

from typing import Dict, Any, List, Optional
import pandas as pd
import numpy as np


class DataValidationResult:
    """Encapsulates the outcome of a dataset validation audit."""

    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name
        self.is_valid: bool = True
        self.total_rows: int = 0
        self.total_columns: int = 0
        self.missing_counts: Dict[str, int] = {}
        self.duplicate_rows: int = 0
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.metrics: Dict[str, Any] = {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert validation results to dictionary format."""
        return {
            "dataset_name": self.dataset_name,
            "is_valid": self.is_valid,
            "total_rows": self.total_rows,
            "total_columns": self.total_columns,
            "missing_counts": self.missing_counts,
            "duplicate_rows": self.duplicate_rows,
            "errors": self.errors,
            "warnings": self.warnings,
            "metrics": self.metrics,
        }

    def summary(self) -> str:
        """Return a human-readable executive summary string."""
        status = "PASSED" if self.is_valid else "FAILED"
        err_str = f" | Errors: {len(self.errors)}" if self.errors else ""
        warn_str = f" | Warnings: {len(self.warnings)}" if self.warnings else ""
        return (
            f"[{status}] {self.dataset_name}: {self.total_rows} rows, "
            f"{self.total_columns} cols{err_str}{warn_str}"
        )


def validate_superstore_schema(df: pd.DataFrame) -> DataValidationResult:
    """Audit and validate raw or cleaned Retail Superstore dataset."""
    result = DataValidationResult("Superstore Sales")
    result.total_rows = len(df)
    result.total_columns = len(df.columns)

    required_cols = [
        "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
        "Customer ID", "Customer Name", "Segment", "Country", "City",
        "State", "Postal Code", "Region", "Product ID", "Category",
        "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit"
    ]

    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        result.errors.append(f"Missing required columns: {missing_cols}")
        result.is_valid = False
        return result

    # Missing values check
    null_counts = df.isnull().sum()
    result.missing_counts = null_counts[null_counts > 0].to_dict()

    # Duplicate check on Row ID
    if "Row ID" in df.columns:
        dups = df["Row ID"].duplicated().sum()
        result.duplicate_rows = int(dups)
        if dups > 0:
            result.warnings.append(f"Found {dups} duplicate Row ID values.")

    # Numeric boundary checks
    if "Sales" in df.columns and df["Sales"].dropna().any():
        neg_sales = (df["Sales"] < 0).sum()
        if neg_sales > 0:
            result.errors.append(f"Found {neg_sales} records with negative Sales.")
            result.is_valid = False

    if "Discount" in df.columns and df["Discount"].dropna().any():
        invalid_disc = ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()
        if invalid_disc > 0:
            result.errors.append(f"Found {invalid_disc} records with Discount outside [0, 1].")
            result.is_valid = False

    if "Quantity" in df.columns and df["Quantity"].dropna().any():
        invalid_qty = (df["Quantity"] <= 0).sum()
        if invalid_qty > 0:
            result.errors.append(f"Found {invalid_qty} records with non-positive Quantity.")
            result.is_valid = False

    result.metrics = {
        "valid_rows": int(df["Sales"].notnull().sum()) if "Sales" in df.columns else len(df),
        "total_revenue": float(df["Sales"].sum()) if "Sales" in df.columns else 0.0,
        "total_profit": float(df["Profit"].sum()) if "Profit" in df.columns else 0.0,
    }
    return result


def validate_churn_schema(df: pd.DataFrame) -> DataValidationResult:
    """Audit and validate raw or cleaned Telco Customer Churn dataset."""
    result = DataValidationResult("Telco Customer Churn")
    result.total_rows = len(df)
    result.total_columns = len(df.columns)

    required_cols = [
        "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
        "tenure", "PhoneService", "MultipleLines", "InternetService",
        "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
        "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
        "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"
    ]

    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        result.errors.append(f"Missing required columns: {missing_cols}")
        result.is_valid = False
        return result

    # Check customer ID uniqueness
    dup_customers = df["customerID"].duplicated().sum()
    if dup_customers > 0:
        result.errors.append(f"Found {dup_customers} duplicate customerID entries.")
        result.is_valid = False

    # Check TotalCharges whitespace issue
    if "TotalCharges" in df.columns:
        whitespace_count = (df["TotalCharges"].astype(str).str.strip() == "").sum()
        if whitespace_count > 0:
            result.warnings.append(
                f"Found {whitespace_count} records with empty/whitespace TotalCharges (tenure 0 cohort)."
            )

    # Churn label check
    if "Churn" in df.columns:
        unique_churn = set(df["Churn"].dropna().unique())
        if not unique_churn.issubset({"Yes", "No", 0, 1}):
            result.errors.append(f"Unexpected Churn categories: {unique_churn}")
            result.is_valid = False

    # Tenure range
    if "tenure" in df.columns:
        if (df["tenure"] < 0).any():
            result.errors.append("Negative tenure values detected.")
            result.is_valid = False

    result.metrics = {
        "churn_rate_pct": float((df["Churn"] == "Yes").mean() * 100) if "Churn" in df.columns else 0.0,
        "mean_monthly_charges": float(df["MonthlyCharges"].mean()) if "MonthlyCharges" in df.columns else 0.0,
    }
    return result


def validate_financial_schema(df: pd.DataFrame) -> DataValidationResult:
    """Audit and validate Corporate Financial Sample dataset."""
    result = DataValidationResult("Corporate Financial Sample")
    result.total_rows = len(df)
    result.total_columns = len(df.columns)

    # Cleaned standard column names expected
    cols_clean = [c.strip() for c in df.columns]
    required_cols = [
        "Segment", "Country", "Product", "Discount Band", "Units Sold",
        "Manufacturing Price", "Sale Price", "Gross Sales", "Discounts",
        "Sales", "COGS", "Profit", "Date"
    ]

    missing_cols = [c for c in required_cols if c not in cols_clean]
    if missing_cols:
        result.errors.append(f"Missing required financial columns: {missing_cols}")
        result.is_valid = False
        return result

    # Standardize copy for checking calculations
    std_df = df.copy()
    std_df.columns = [c.strip() for c in std_df.columns]

    # Check non-negative costs and prices
    if (std_df["Units Sold"] < 0).any():
        result.errors.append("Negative Units Sold detected.")
        result.is_valid = False

    if (std_df["COGS"] < 0).any():
        result.errors.append("Negative COGS detected.")
        result.is_valid = False

    # Check Gross Sales formula consistency: Units Sold * Sale Price
    expected_gross = std_df["Units Sold"] * std_df["Sale Price"]
    variance = (std_df["Gross Sales"] - expected_gross).abs().max()
    if variance > 1.0:
        result.warnings.append(f"Gross Sales diverges from Units * Sale Price by up to {variance:.2f}")

    result.metrics = {
        "total_sales": float(std_df["Sales"].sum()),
        "total_cogs": float(std_df["COGS"].sum()),
        "total_profit": float(std_df["Profit"].sum()),
        "gross_profit_margin_pct": float((std_df["Profit"].sum() / std_df["Sales"].sum()) * 100),
    }
    return result
