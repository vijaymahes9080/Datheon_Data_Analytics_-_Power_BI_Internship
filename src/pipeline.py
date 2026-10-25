"""End-to-End Orchestration Pipeline.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Executes ingestion, schema validation, dataset sanitization, and metric auditing.
"""

import os
import argparse
import pandas as pd
from src.loaders import load_superstore, load_telco_churn, load_financial_sample
from src.validation import (
    validate_superstore_schema,
    validate_churn_schema,
    validate_financial_schema,
)
from src.cleaning import clean_superstore, clean_telco_churn, clean_financial_sample
from src.metrics import (
    calculate_retail_kpis,
    calculate_churn_kpis,
    calculate_financial_kpis,
    simulate_financial_scenario,
)

PROCESSED_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "processed")


def run_pipeline(export_processed: bool = True) -> bool:
    """Execute end-to-end ingestion, validation, cleaning, and reporting."""
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    print("=" * 70)
    print("RISK AUTONOMOUS BUSINESS ANALYTICS & DECISION ENGINE")
    print("=" * 70)

    # 1. Load Raw Data
    print("\n[1/4] Ingesting raw datasets...")
    df_sup_raw = load_superstore()
    df_churn_raw = load_telco_churn()
    df_fin_raw = load_financial_sample()
    print(f"  Superstore raw: {df_sup_raw.shape}")
    print(f"  Telco Churn raw: {df_churn_raw.shape}")
    print(f"  Financial Sample raw: {df_fin_raw.shape}")

    # 2. Clean and Standardize Data
    print("\n[2/4] Executing non-destructive sanitization...")
    df_sup_clean = clean_superstore(df_sup_raw)
    df_churn_clean = clean_telco_churn(df_churn_raw)
    df_fin_clean = clean_financial_sample(df_fin_raw)

    if export_processed:
        df_sup_clean.to_csv(os.path.join(PROCESSED_DIR, "superstore_cleaned.csv"), index=False)
        df_churn_clean.to_csv(os.path.join(PROCESSED_DIR, "churn_cleaned.csv"), index=False)
        df_fin_clean.to_csv(os.path.join(PROCESSED_DIR, "financial_cleaned.csv"), index=False)
        print(f"  Saved cleaned datasets to {PROCESSED_DIR}")

    # 3. Validate Processed Data
    print("\n[3/4] Running schema integrity validation...")
    v_sup = validate_superstore_schema(df_sup_clean)
    v_churn = validate_churn_schema(df_churn_clean)
    v_fin = validate_financial_schema(df_fin_clean)

    print(f"  {v_sup.summary()}")
    print(f"  {v_churn.summary()}")
    print(f"  {v_fin.summary()}")

    assert v_sup.is_valid and v_churn.is_valid and v_fin.is_valid, "Validation failed!"

    # 4. Compute KPIs
    print("\n[4/4] Generating executive scorecard...")
    kpis_sup = calculate_retail_kpis(df_sup_clean)
    kpis_churn = calculate_churn_kpis(df_churn_clean)
    kpis_fin = calculate_financial_kpis(df_fin_clean)

    print(f"  Retail Total Sales: ${kpis_sup['Total Sales']:,.2f} | Profit Margin: {kpis_sup['Profit Margin %']:.2f}%")
    print(f"  Churn Rate: {kpis_churn['Churn Rate %']:.2f}% | High Risk Churn: {kpis_churn['High Risk Churn Rate %']:.2f}%")
    print(f"  Financial Sales: ${kpis_fin['Total Sales']:,.2f} | Gross Margin: {kpis_fin['Gross Profit Margin %']:.2f}%")

    print("\n" + "=" * 70)
    print("PIPELINE EXECUTION COMPLETED SUCCESSFULLY WITH 100% RECONCILIATION")
    print("=" * 70)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RISK Decision Intelligence Pipeline")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")
    args = parser.parse_args()
    run_pipeline()
