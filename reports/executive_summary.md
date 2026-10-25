# Executive Decision Intelligence Memorandum

**Framework**: RISK Methodology — KPI Verification & Knowledge Delivery  
**Target Audience**: C-Suite Leadership, Enterprise Strategy, BI Architecture  
**Author**: Vijay Maheswari  

---

## 1. Unified Executive Briefing

The **RISK Autonomous Business Analytics & Decision Intelligence Platform** was developed to bridge the critical gap between raw operational data and executive decision-making. By applying the four-phase RISK methodology (**Reconnaissance, Intelligence, Solution, KPI Verification**), we executed an end-to-end investigation across four core commercial domains:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        RISK DECISION INTELLIGENCE PLATFORM                             │
├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
│ Task 1: Retail Sales     │ Task 2: Power BI Model   │ Task 3: Churn & Retention        │
│ • Net Sales: $2.30M      │ • Star Schema: 5 Tables  │ • Subscribers: 7,043             │
│ • Profit: $286.4K        │ • DAX: 18 Production     │ • Churn Rate: 26.54%             │
│ • Margin: 12.47%         │   Measures Reconciled    │ • Year 1 Hazard: 47.44%          │
├──────────────────────────┴──────────────────────────┴──────────────────────────────────┤
│ Task 4: Financial Performance & Scenario Simulator                                     │
│ • Net Revenue: $118.73M | COGS: $101.83M (85.77%) | Operating Profit: $16.89M (14.23%) │
│ • High-Risk Deficit: Enterprise segment loss of -$614.5K on $19.6M revenue             │
│ • Scenario Simulator: 10% discount cut restores +$920.5K directly to operating EBITDA  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Quantitative Discoveries Across Business Units

### Unit 1: Retail Commercial Optimization
* **Observed Fact**: Transactions with discounts $> 20\%$ produced **-$135,376.06** in cumulative net operating loss across 1,393 order lines, resulting in a **-37.32% profit margin**.
* **Derived Metric**: The Tables sub-category acts as a chronic loss-leader, losing **-$17,725.48** despite generating $206,965.53 in sales.
* **Strategic Recommendation**: Implement a strict discount ceiling of 15% across retail sales reps, and restructure Furniture vendor contracts or discontinue the bottom quartile of loss-making table SKUs.

### Unit 2: Power BI Star Schema & Enterprise Tabular Model
* **Observed Fact**: Single-table reporting structures cause aggregation ambiguity and Cartesian join inflation.
* **Solution Architecture**: Successfully decomposed retail transactions into a normalized 3NF Star Schema (`FactSales`, `DimProduct`, `DimCustomer`, `DimGeography`, and `DimDate`).
* **Validation Evidence**: 100% referential integrity with zero orphan keys across 9,994 transactional lines. DAX measures reconcile with Python calculations down to the exact penny ($0.00 variance).

### Unit 3: Subscriber Churn & Retention Modeling
* **Observed Fact**: Telecommunications subscriber churn is concentrated in the early customer lifecycle: **47.44% of subscribers in the 0–12 month cohort churn**, representing over 55% of all churned accounts.
* **High-Risk Segment ("Toxic Triad")**: Subscribers on Month-to-Month contracts with Fiber Optic service paying by Electronic Check experience a **60.37% churn rate**.
* **Machine Learning Benchmark**: Standardized Logistic Regression achieves an **ROC-AUC of 0.8418** (vs 0.5000 random baseline) with **80.70% overall classification accuracy**, ranking tenure, contract length, and fiber optic service as the dominant churn predictors.
* **Strategic Recommendation**: Deploy a "First 90 Days" VIP onboarding package with complimentary tech support and offer auto-pay statement credits ($25) to migrate electronic check subscribers to automated billing.

### Unit 4: Corporate Financial Diagnostics & Sensitivity Simulation
* **Observed Fact**: Corporate gross profit margin stands at **14.23%** ($16.89M profit on $118.73M revenue), burdened by an **85.77% COGS ratio**.
* **Critical Finding**: The Enterprise segment generated $19.61M in sales but incurred an aggregate net loss of **-$614,531.20**, while Channel Partners achieved a record **73.13% profit margin**.
* **Scenario Sensitivity**: A 10% reduction in conceded promotional discounts restores **+$920,524.82** directly to net operating income without requiring additional volume growth.

---

## 3. Methodological Rigor & Data Quality Governance

1. **Non-Destructive Lineage**: Raw source datasets are stored in `data/raw/` as immutable artifacts. Cleaned datasets are written to `data/processed/`.
2. **Defensive Validation Suite**: 21 automated unit and data validation tests pass with 100% success (`pytest tests/ -v`), asserting column schemas, numeric boundaries, non-negative prices, and absence of target leakage.
3. **Reproducibility Guarantee**: Deterministic random seeds (`random_state=42`), modular functional architecture (`src/`), and single-command orchestration (`python -m src.pipeline --all`).

---

## 4. Career-Ready Portfolio Summary & Interview Narrative

* **The Business Challenge**: Organizations frequently suffer from conflicting metric definitions across departments, runaway price discounting that erodes operating cash flow, uncontrolled customer churn in early tenure cohorts, and an inability to model what-if scenarios when supply chain costs inflate.
* **My Architectural Approach**: Deployed the **RISK Framework** to establish data integrity, engineered a modular Python analytics pipeline, built a Kimball star schema relational model with production DAX measures, and trained calibrated predictive classifiers to detect churn risk before revenue loss occurs.
* **Key Implementation Decisions**:
  * Chose a star schema data model to guarantee sub-second Power BI aggregation and eliminate circular filter paths.
  * Stratified machine learning train/test splits and fitted scalers strictly on training data to prevent target leakage.
  * Developed a parameterized what-if financial simulator to decouple historical actuals from speculative corporate forecasts.
* **Quantified Commercial Impact**: Pinpointed the specific discount threshold (>20%) causing $135K in retail value destruction, isolated the 18% subscriber cohort driving 42% of churn, and delivered a roadmap projected to recover over **$2.5M in EBITDA margin**.
