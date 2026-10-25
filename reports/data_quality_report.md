# Comprehensive Multi-Dataset Data Quality & Provenance Audit Report

**Framework**: RISK Methodology — Reconnaissance & Requirements  
**Audit Date**: October 2026  
**Auditor**: Vijay Maheswari  

---

## 1. Executive Summary & Quality Scorecard

This data quality audit examines the three canonical source datasets ingested by the RISK Autonomous Decision Engine. Prior to feature transformation or KPI computation, each dataset underwent automated structural auditing, null profiling, duplicate detection, and schema validation.

| Dataset | Ingested Shape | Validated Clean Shape | Missing Value Anomalies Resolved | Duplicates Identified | Quality Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Retail Superstore** | 10,800 rows $\times$ 21 cols | 9,994 rows $\times$ 12 cols | 806 empty rows + 11 missing Postal Codes | 799 redundant padding rows | **PASSED (100% Validated)** |
| **Telco Customer Churn** | 7,043 rows $\times$ 21 cols | 7,043 rows $\times$ 25 cols | 11 whitespace `TotalCharges` (tenure = 0) | 0 duplicate customer IDs | **PASSED (100% Validated)** |
| **Corporate Financial** | 700 rows $\times$ 16 cols | 700 rows $\times$ 22 cols | Header whitespace anomaly (`' Sales'`) | 0 duplicate batches | **PASSED (100% Validated)** |

---

## 2. Dataset A: Retail Superstore Sales

### Provenance & Storage
* **Canonical Remote URL**: `https://www.datheon.in/datasets/superstore_sales.csv`
* **Raw File Path**: `data/raw/superstore_sales.csv` (2,293,765 bytes)
* **Processed Fact Table**: `data/processed/FactSales.csv` (9,994 records)
* **Conforming Dimensions**: `DimProduct.csv`, `DimCustomer.csv`, `DimGeography.csv`, `DimDate.csv`

### Anomaly Profiling & Remediation Ledger
1. **Empty / Padded Row Artifacts**:
   * *Issue*: Raw CSV file contained 10,800 total rows, of which exactly 806 records contained complete nulls across `Sales`, `Profit`, `Customer ID`, and `Order Date`.
   * *Remediation*: Deterministic filtering on non-null `Order ID`, `Sales`, and `Profit` isolated the true 9,994 transactional rows.
2. **Postal Code Nulls in Burlington, VT**:
   * *Issue*: 11 records from Burlington, Vermont possessed NaN values for `Postal Code`.
   * *Remediation*: Imputed canonical zip code `5408` (Burlington VT 05408).
3. **Date Parsing & Time Horizon**:
   * *Validation*: Order Date ranges from `2014-01-03` to `2017-12-30`; Ship Date ranges from `2014-01-07` to `2018-01-05`.
   * *Check*: Asserted that `Ship Date >= Order Date` for 100% of rows (zero negative shipping times).

---

## 3. Dataset B: Telco Customer Churn

### Provenance & Storage
* **Canonical Remote URL**: `https://www.datheon.in/datasets/telco_customer_churn.csv`
* **Raw File Path**: `data/raw/telco_customer_churn.csv` (970,457 bytes)
* **Processed Path**: `data/processed/churn_cleaned.csv` (7,043 records)

### Anomaly Profiling & Remediation Ledger
1. **Whitespace Infiltration in `TotalCharges`**:
   * *Issue*: The `TotalCharges` column was typed as `object`/`string` because exactly 11 subscriber records contained blank whitespace `" "`.
   * *Root Cause Analysis*: Cross-referencing demonstrated that all 11 records have `tenure == 0` (brand-new accounts who have not yet completed their first billing cycle).
   * *Remediation*: Safely coerced `TotalCharges` to float and imputed `0.0` for new subscribers with zero tenure.
2. **Customer ID Uniqueness**:
   * *Validation*: Confirmed exactly 7,043 distinct `customerID` hashes (zero duplicates).
3. **Target Variable Validation**:
   * *Distribution*: Exactly 5,174 `"No"` (73.46%) and 1,869 `"Yes"` (26.54%). Zero missing or corrupted target labels.

---

## 4. Dataset C: Corporate Financial Sample

### Provenance & Storage
* **Canonical Remote URL**: `https://www.datheon.in/datasets/financial_sample.xlsx`
* **Raw File Path**: `data/raw/financial_sample.xlsx` (83,418 bytes)
* **Processed Path**: `data/processed/FinancialFact.csv` (700 records)

### Anomaly Profiling & Remediation Ledger
1. **Column Header Whitespace Corruption**:
   * *Issue*: Raw Excel worksheet header for sales contained a leading space (`' Sales'`).
   * *Remediation*: Applied `df.columns = [c.strip() for c in df.columns]` across all fields, ensuring standard programmatic accessibility.
2. **Accounting Formula Verification**:
   * *Gross Sales Formula*: Asserted $Gross Sales = Units Sold \times Sale Price$. Maximum deviation $< \$0.01$ across all 700 batches.
   * *Net Sales Formula*: Asserted $Net Sales = Gross Sales - Discounts$. Exact match across all 700 batches.
   * *Operating Profit Formula*: Asserted $Profit = Net Sales - COGS$. Exact match across all 700 batches.
3. **Temporal Bounds**:
   * *Coverage*: Spans September 2013 through December 2014 (16 continuous operating months).

---

## 5. Non-Destructive Data Lineage Assurance

Under the RISK methodology:
* **Raw Preservation**: Raw dataset files in `data/raw/` are treated as immutable read-only assets.
* **Separation of Concerns**: All sanitization, type conversions, and engineered features are stored independently in `data/processed/`.
* **Zero Fabrication**: Every number, ratio, and KPI reported in the platform derives from executable Python algorithms and verified formulas.
