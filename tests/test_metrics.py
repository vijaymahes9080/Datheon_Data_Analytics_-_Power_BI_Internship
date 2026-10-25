"""Unit Test Suite for Analytical KPI Engines and Scenario Simulation.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Tests KPI reconciliation, mathematical consistency, grouped totals reconciliation,
and scenario sensitivity mechanics.
"""

import pytest
import pandas as pd
import numpy as np
from src.loaders import load_superstore, load_telco_churn, load_financial_sample
from src.cleaning import clean_superstore, clean_telco_churn, clean_financial_sample
from src.metrics import (
    calculate_retail_kpis,
    calculate_churn_kpis,
    calculate_financial_kpis,
    simulate_financial_scenario,
)


class TestRetailMetrics:
    """Test suite for Retail Sales KPI calculations and reconciliation."""

    @pytest.fixture(scope="class")
    def clean_retail_df(self):
        raw = load_superstore()
        return clean_superstore(raw)

    def test_overall_sales_and_profit_accuracy(self, clean_retail_df):
        kpis = calculate_retail_kpis(clean_retail_df)

        expected_sales = round(float(clean_retail_df["Sales"].sum()), 2)
        expected_profit = round(float(clean_retail_df["Profit"].sum()), 2)

        assert kpis["Total Sales"] == expected_sales
        assert kpis["Total Profit"] == expected_profit
        assert kpis["Total Quantity"] == int(clean_retail_df["Quantity"].sum())
        assert kpis["Total Orders"] == int(clean_retail_df["Order ID"].nunique())

    def test_profit_margin_calculation(self, clean_retail_df):
        kpis = calculate_retail_kpis(clean_retail_df)
        expected_margin = round((kpis["Total Profit"] / kpis["Total Sales"]) * 100, 2)
        assert kpis["Profit Margin %"] == expected_margin

    def test_grouped_segments_reconcile_to_totals(self, clean_retail_df):
        kpis = calculate_retail_kpis(clean_retail_df)
        by_segment = kpis["By Segment"]

        sum_segment_sales = round(float(by_segment["Sales"].sum()), 2)
        sum_segment_profit = round(float(by_segment["Profit"].sum()), 2)

        assert pytest.approx(sum_segment_sales, rel=1e-3) == kpis["Total Sales"]
        assert pytest.approx(sum_segment_profit, rel=1e-3) == kpis["Total Profit"]

    def test_negative_profit_orders_isolation(self, clean_retail_df):
        kpis = calculate_retail_kpis(clean_retail_df)
        neg_count = kpis["Negative Profit Order Lines"]
        neg_total = kpis["Total Negative Profit Loss"]

        assert neg_count > 0
        assert neg_total < 0
        actual_neg_sum = clean_retail_df.loc[clean_retail_df["Profit"] < 0, "Profit"].sum()
        assert pytest.approx(neg_total, rel=1e-2) == round(actual_neg_sum, 2)


class TestChurnMetrics:
    """Test suite for Customer Churn and Retention KPI calculations."""

    @pytest.fixture(scope="class")
    def clean_churn_df(self):
        raw = load_telco_churn()
        return clean_telco_churn(raw)

    def test_churn_and_retention_sum_to_unity(self, clean_churn_df):
        kpis = calculate_churn_kpis(clean_churn_df)

        assert kpis["Eligible Customers"] == len(clean_churn_df)
        assert kpis["Eligible Customers"] == (kpis["Churned Customers"] + kpis["Retained Customers"])

        total_rate = kpis["Churn Rate %"] + kpis["Retention Rate %"]
        assert pytest.approx(total_rate, abs=0.05) == 100.0

    def test_tenure_cohorts_reconciliation(self, clean_churn_df):
        kpis = calculate_churn_kpis(clean_churn_df)
        cohorts = kpis["Tenure Cohorts"]

        assert cohorts["Total"].sum() == kpis["Eligible Customers"]
        assert cohorts["Churned"].sum() == kpis["Churned Customers"]
        assert cohorts["Retained"].sum() == kpis["Retained Customers"]

    def test_high_risk_profile_metrics(self, clean_churn_df):
        kpis = calculate_churn_kpis(clean_churn_df)
        assert kpis["High Risk Cohort Total"] > 0
        # High risk cohort (Month-to-month + Fiber Optic + Electronic check) churn rate is significantly higher
        assert kpis["High Risk Churn Rate %"] > kpis["Churn Rate %"]


class TestFinancialMetricsAndSimulation:
    """Test suite for Corporate Financial Sample KPIs and Scenario Simulator."""

    @pytest.fixture(scope="class")
    def clean_fin_df(self):
        raw = load_financial_sample()
        return clean_financial_sample(raw)

    def test_financial_kpi_accounting_consistency(self, clean_fin_df):
        kpis = calculate_financial_kpis(clean_fin_df)

        expected_sales = round(float(clean_fin_df["Sales"].sum()), 2)
        expected_cogs = round(float(clean_fin_df["COGS"].sum()), 2)
        expected_profit = round(float(clean_fin_df["Profit"].sum()), 2)

        assert kpis["Total Sales"] == expected_sales
        assert kpis["Total COGS"] == expected_cogs
        assert kpis["Total Profit"] == expected_profit

        # Gross Profit Margin %
        calc_margin = round((expected_profit / expected_sales) * 100, 2)
        assert kpis["Gross Profit Margin %"] == calc_margin

    def test_scenario_simulator_discount_cut_improves_profit(self, clean_fin_df):
        # 10% reduction in discount magnitude
        sim = simulate_financial_scenario(clean_fin_df, discount_pct_delta=-0.10)

        assert sim["simulated"]["Total Profit"] > sim["baseline"]["Total Profit"]
        assert sim["variance"]["Profit Delta ($)"] > 0

    def test_scenario_simulator_cogs_increase_erodes_margin(self, clean_fin_df):
        # 5% increase in supply chain costs
        sim = simulate_financial_scenario(clean_fin_df, cogs_pct_delta=0.05)

        assert sim["simulated"]["Total COGS"] > sim["baseline"]["Total COGS"]
        assert sim["simulated"]["Total Profit"] < sim["baseline"]["Total Profit"]
        assert sim["variance"]["Margin Delta (bps)"] < 0
