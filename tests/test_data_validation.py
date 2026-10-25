"""Test Suite for Data Validation and Schema Integrity.

Part of RISK V3 - Autonomous Business Analytics & Decision Intelligence Engine.
Tests required columns, boundary conditions, edge cases, and schema violation detections.
"""

import pytest
import pandas as pd
import numpy as np
from src.validation import (
    validate_superstore_schema,
    validate_churn_schema,
    validate_financial_schema,
)
from src.loaders import load_superstore, load_telco_churn, load_financial_sample
from src.cleaning import clean_superstore, clean_telco_churn, clean_financial_sample


class TestSuperstoreValidation:
    """Validation test suite for Retail Superstore schema."""

    def test_clean_superstore_validates_successfully(self):
        raw = load_superstore()
        clean = clean_superstore(raw)
        result = validate_superstore_schema(clean)

        assert result.is_valid is True
        assert result.total_rows == 9994
        assert len(result.errors) == 0
        assert result.metrics["total_revenue"] > 0
        assert result.metrics["total_profit"] > 0

    def test_detects_missing_required_columns(self):
        df_incomplete = pd.DataFrame({"Order ID": ["CA-101"], "Sales": [100.0]})
        result = validate_superstore_schema(df_incomplete)

        assert result.is_valid is False
        assert any("Missing required columns" in err for err in result.errors)

    def test_detects_negative_sales_anomaly(self):
        raw = load_superstore()
        clean = clean_superstore(raw).copy()
        clean.loc[0, "Sales"] = -500.0

        result = validate_superstore_schema(clean)
        assert result.is_valid is False
        assert any("negative Sales" in err for err in result.errors)

    def test_detects_discount_boundary_violations(self):
        raw = load_superstore()
        clean = clean_superstore(raw).copy()
        clean.loc[0, "Discount"] = 1.80  # 180% discount is invalid

        result = validate_superstore_schema(clean)
        assert result.is_valid is False
        assert any("Discount outside [0, 1]" in err for err in result.errors)


class TestChurnValidation:
    """Validation test suite for Telco Customer Churn schema."""

    def test_clean_churn_validates_successfully(self):
        raw = load_telco_churn()
        clean = clean_telco_churn(raw)
        result = validate_churn_schema(clean)

        assert result.is_valid is True
        assert result.total_rows == 7043
        assert len(result.errors) == 0
        assert 20.0 < result.metrics["churn_rate_pct"] < 30.0

    def test_detects_duplicate_customer_ids(self):
        raw = load_telco_churn()
        corrupted = raw.copy()
        corrupted.loc[1, "customerID"] = corrupted.loc[0, "customerID"]

        result = validate_churn_schema(corrupted)
        assert result.is_valid is False
        assert any("duplicate customerID" in err for err in result.errors)

    def test_flags_whitespace_total_charges(self):
        raw = load_telco_churn()
        result = validate_churn_schema(raw)

        # Raw file is known to have 11 empty TotalCharges for tenure 0
        assert any("whitespace TotalCharges" in w for w in result.warnings)

    def test_detects_invalid_churn_category(self):
        raw = load_telco_churn()
        clean = clean_telco_churn(raw).copy()
        clean.loc[0, "Churn"] = "Maybe"

        result = validate_churn_schema(clean)
        assert result.is_valid is False
        assert any("Unexpected Churn categories" in err for err in result.errors)


class TestFinancialValidation:
    """Validation test suite for Corporate Financial Sample schema."""

    def test_clean_financial_validates_successfully(self):
        raw = load_financial_sample()
        clean = clean_financial_sample(raw)
        result = validate_financial_schema(clean)

        assert result.is_valid is True
        assert result.total_rows == 700
        assert len(result.errors) == 0
        assert result.metrics["total_sales"] > 0
        assert result.metrics["gross_profit_margin_pct"] > 0

    def test_detects_negative_units_sold(self):
        raw = load_financial_sample()
        clean = clean_financial_sample(raw).copy()
        clean.loc[0, "Units Sold"] = -10.0

        result = validate_financial_schema(clean)
        assert result.is_valid is False
        assert any("Negative Units Sold" in err for err in result.errors)

    def test_handles_empty_dataframe(self):
        df_empty = pd.DataFrame()
        result = validate_financial_schema(df_empty)
        assert result.is_valid is False
        assert result.total_rows == 0
