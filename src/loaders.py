"""Resilient Data Ingestion and Source Loader Module.

Part of RISK V3 - Autonomous Business Analytics & Decision Intelligence Engine.
Provides robust local-first, HTTP-fallback ingestion pipelines for all datasets.
"""

import os
from typing import Optional
import urllib.request
import pandas as pd

SUPERSTORE_URL = "https://www.datheon.in/datasets/superstore_sales.csv"
CHURN_URL = "https://www.datheon.in/datasets/telco_customer_churn.csv"
FINANCIAL_URL = "https://www.datheon.in/datasets/financial_sample.xlsx"

DEFAULT_RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")


def _ensure_file(local_path: str, remote_url: str) -> str:
    """Ensure a dataset exists locally; download if absent."""
    if not os.path.exists(local_path):
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        req = urllib.request.Request(remote_url, headers={"User-Agent": "Mozilla/5.0 (RISK-V3-Engine)"})
        with urllib.request.urlopen(req) as resp, open(local_path, "wb") as f_out:
            f_out.write(resp.read())
    return local_path


def load_superstore(filepath: Optional[str] = None) -> pd.DataFrame:
    """Load the raw Superstore Sales dataset.

    Attempts UTF-8 first, falls back to Latin-1/ISO-8859-1.
    """
    path = filepath or os.path.join(DEFAULT_RAW_DIR, "superstore_sales.csv")
    _ensure_file(path, SUPERSTORE_URL)

    try:
        df = pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="latin1")
    return df


def load_telco_churn(filepath: Optional[str] = None) -> pd.DataFrame:
    """Load the raw Telco Customer Churn dataset."""
    path = filepath or os.path.join(DEFAULT_RAW_DIR, "telco_customer_churn.csv")
    _ensure_file(path, CHURN_URL)
    return pd.read_csv(path, encoding="utf-8")


def load_financial_sample(filepath: Optional[str] = None) -> pd.DataFrame:
    """Load the raw Corporate Financial Sample Excel workbook."""
    path = filepath or os.path.join(DEFAULT_RAW_DIR, "financial_sample.xlsx")
    _ensure_file(path, FINANCIAL_URL)
    return pd.read_excel(path, engine="openpyxl")
