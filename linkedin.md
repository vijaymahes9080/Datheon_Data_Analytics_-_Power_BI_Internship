# LinkedIn Post: Autonomous Business Analytics & Decision Intelligence Platform

> **Recommended Post Attachment**: Attach the high-resolution infographic **[`image.png`](file:///d:/intership/Datheon_Data_Analytics_&_Power_BI_Internship/vj/image.png)** or **[`docs/images/linkedin_project_showcase.png`](file:///d:/intership/Datheon_Data_Analytics_&_Power_BI_Internship/vj/docs/images/linkedin_project_showcase.png)** to your LinkedIn post.

---

### Copy-Paste Post Text:

Most business dashboards fail for one simple reason: they report past symptoms instead of isolating root causes and driving future decisions.

During my **Data Analytics & Business Intelligence Internship at Datheon**, I set out to bridge the gap between diagnostic data engineering, predictive machine learning, and CFO-level decision modeling.

I engineered the **RISK Decision Intelligence Platform** — an autonomous, evidence-driven analytics engine solving 4 critical commercial challenges across Retail, Subscriber Retention, Financial Modeling, and Power BI.

Here is what happened when we applied rigorous data intelligence to real business data:

---

### 🔍 1. Retail Sales: Unmasking the "Discount Trap"
* **The Symptom**: A seemingly healthy $2.30M in top-line retail sales.
* **The Root Cause**: Products sold with discounts exceeding 20% caused an aggregate **-$135,376.06 loss** with a disastrous **-37.32% margin**.
* **The Action**: Pinpointed that the "Tables" subcategory alone leaked -$17,725.48 across 319 transactions. Implemented hard discount ceiling rules and warranty bundles to protect margin integrity.

### 🏛️ 2. Power BI: Star Schema & Zero-Dollar Variance
* Built a high-performance relational dimensional model: `FactSales` (9,994 records) connected to `DimProduct` (1,862 SKUs), `DimCustomer` (793 customers), `DimGeography` (631 postal codes), and a continuous 1,464-day `DimDate` calendar table.
* Developed a complete production DAX Time Intelligence suite (`Total Sales`, `Total Profit`, `Profit Margin %`, `YoY Growth`, `Sales YTD`).
* **The Rigor**: Reconciled every single DAX measure against Python down to the exact penny ($0.00 variance).

### 📉 3. Customer Retention: Isolating the "Toxic Triad"
* **The Discovery**: Churn is heavily tenure-dependent — new subscribers suffer an alarming **47.44% churn rate in months 0–12**, dropping to just 6.61% after year 5.
* **The Toxic Triad**: Subscribers on **Month-to-Month contracts + Fiber Optic service + Electronic Check payments** experience a staggering **60.37% churn rate**.
* **The Strategy**: Trained and calibrated predictive classifiers (0.8418 ROC-AUC) to trigger automated 90-day onboarding concierges and a $10 autopay switch credit, cutting churn hazard by over 50%.

### 💼 4. Financial Modeling: The What-If Sensitivity Simulator
* **The Problem**: The Enterprise segment generated $19.61M in gross sales but operated at a net loss of **-$614,531.20**.
* **The Solution**: Built an interactive multi-variate scenario engine. A targeted 10% discount adjustment restores **+$920,524.82 directly to EBITDA**, while Channel Partners delivered a premium 73.13% profit margin.

---

### ⚙️ How It Was Built: The 4-Stage RISK Framework
* **R — Reconnaissance**: Strict schema auditing, boundary checks, and zero-data-loss ingestion.
* **I — Intelligence**: Diagnostic slicing, cohort hazard modeling, and root cause isolation.
* **S — Solution**: Star-schema relational engineering, calibrated machine learning, and sensitivity simulators.
* **K — KPI Verification**: 21 automated pytest test suites and executive decision ledgers.

📊 **Tech Stack**: Python | Pandas | Scikit-Learn | Power BI | DAX | Pytest | Jupyter Lab | Git

Check out the full repository, code, star schema, and interactive portal:
👉 GitHub: https://github.com/vijaymahes9080/Datheon_Data_Analytics_-_Power_BI_Internship

I’d love to hear your thoughts: How does your organization enforce margin protections against runaway sales discounting?

#DataAnalytics #PowerBI #BusinessIntelligence #DataScience #MachineLearning #Python #DAX #FinancialModeling #CustomerRetention #AnalyticsEngineering #PortfolioProject #Datheon
