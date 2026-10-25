"""Customer Churn, Cohort & Retention Intelligence Engine.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Produces diagnostic visualizations, predictive modeling, and executes Task 3 notebook.
"""

import os
import nbformat as nbf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve, precision_score, recall_score, f1_score
from src.loaders import load_telco_churn
from src.cleaning import clean_telco_churn
from src.metrics import calculate_churn_kpis

FIGURES_DIR = "outputs/figures"


def generate_churn_visualizations(df: pd.DataFrame, output_dir: str = FIGURES_DIR):
    """Generate high-resolution visualization suite for customer churn analysis."""
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="muted")

    # 1. Tenure Cohort Churn & Retention Rates
    kpis = calculate_churn_kpis(df)
    cohorts = kpis["Tenure Cohorts"]

    plt.figure(figsize=(10, 5))
    x = np.arange(len(cohorts))
    width = 0.35
    plt.bar(x - width/2, cohorts["Churn Rate %"], width, label="Churn Rate %", color="#d9534f")
    plt.bar(x + width/2, cohorts["Retention Rate %"], width, label="Retention Rate %", color="#5cb85c")
    plt.xticks(x, cohorts["Tenure Cohort"], fontsize=10)
    plt.ylabel("Percentage (%)", fontsize=11)
    plt.title("Customer Churn vs Retention Rates Across 12-Month Tenure Cohorts", fontsize=13, fontweight="bold", pad=12)
    plt.legend()
    for i, row in cohorts.iterrows():
        plt.text(i - width/2, row["Churn Rate %"] + 1, f"{row['Churn Rate %']:.1f}%", ha="center", fontsize=9, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "churn_tenure_cohort_curve.png"), dpi=300)
    plt.close()

    # 2. Contract vs Payment Method Churn Heatmap
    pivot_cp = df.pivot_table(index="Contract", columns="PaymentMethod", values="Churn_Numeric", aggfunc="mean") * 100
    plt.figure(figsize=(11, 5))
    sns.heatmap(pivot_cp, annot=True, fmt=".1f", cmap="YlOrRd", cbar_kws={"label": "Churn Rate (%)"}, linewidths=0.5)
    plt.title("Cross-Segment Churn Heatmap: Contract Type vs Payment Method", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Payment Method", fontsize=11)
    plt.ylabel("Contract Commitment", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "churn_contract_payment_heatmap.png"), dpi=300)
    plt.close()

    # 3. Service Combination Churn Rates
    svc_agg = pd.DataFrame([
        {"Service": "Fiber Optic", "Churn Rate %": df.loc[df["InternetService"] == "Fiber optic", "Churn_Numeric"].mean() * 100},
        {"Service": "DSL Internet", "Churn Rate %": df.loc[df["InternetService"] == "DSL", "Churn_Numeric"].mean() * 100},
        {"Service": "No Tech Support", "Churn Rate %": df.loc[df["TechSupport"] == "No", "Churn_Numeric"].mean() * 100},
        {"Service": "With Tech Support", "Churn Rate %": df.loc[df["TechSupport"] == "Yes", "Churn_Numeric"].mean() * 100},
        {"Service": "No Online Security", "Churn Rate %": df.loc[df["OnlineSecurity"] == "No", "Churn_Numeric"].mean() * 100},
        {"Service": "With Online Security", "Churn Rate %": df.loc[df["OnlineSecurity"] == "Yes", "Churn_Numeric"].mean() * 100},
        {"Service": "Electronic Check", "Churn Rate %": df.loc[df["PaymentMethod"] == "Electronic check", "Churn_Numeric"].mean() * 100},
        {"Service": "Bank Auto-Pay", "Churn Rate %": df.loc[df["PaymentMethod"] == "Bank transfer (automatic)", "Churn_Numeric"].mean() * 100},
    ]).sort_values("Churn Rate %", ascending=True)

    plt.figure(figsize=(10, 6))
    colors = ["#5cb85c" if r < 20 else "#f0ad4e" if r < 35 else "#d9534f" for r in svc_agg["Churn Rate %"]]
    plt.barh(svc_agg["Service"], svc_agg["Churn Rate %"], color=colors)
    plt.axvline(kpis["Churn Rate %"], color="black", linestyle="--", label=f"Baseline Churn ({kpis['Churn Rate %']}%)")
    plt.xlabel("Observed Churn Rate (%)", fontsize=11)
    plt.title("Churn Rate Disparities Across Key Service & Support Combinations", fontsize=13, fontweight="bold", pad=12)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "churn_service_combination_rates.png"), dpi=300)
    plt.close()

    # 4. Monthly Charges Distribution by Churn Status
    plt.figure(figsize=(9, 5))
    sns.kdeplot(data=df, x="MonthlyCharges", hue="Churn", common_norm=False, fill=True, palette={"No": "#5cb85c", "Yes": "#d9534f"}, alpha=0.4)
    plt.title("Distribution of Monthly Charges: Churned vs Retained Subscribers", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Monthly Charges ($)", fontsize=11)
    plt.ylabel("Density", fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "churn_monthly_charges_distribution.png"), dpi=300)
    plt.close()

    # 5. ROC-AUC Curve for Logistic Regression
    feature_cols = [
        "tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen",
        "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
        "PaperlessBilling", "PaymentMethod"
    ]
    X = pd.get_dummies(df[feature_cols], drop_first=True)
    y = df["Churn_Numeric"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train_scaled, y_train)
    y_prob = lr.predict_proba(X_test_scaled)[:, 1]
    auc_score = roc_auc_score(y_test, y_prob)

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.figure(figsize=(7, 6))
    plt.plot(fpr, tpr, color="#0275d8", linewidth=2.5, label=f"Logistic Regression (AUC = {auc_score:.3f})")
    plt.plot([0, 1], [0, 1], color="grey", linestyle="--", label="Random Baseline (AUC = 0.500)")
    plt.title("Receiver Operating Characteristic (ROC) Curve", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("False Positive Rate", fontsize=11)
    plt.ylabel("True Positive Rate", fontsize=11)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "churn_roc_auc_curve.png"), dpi=300)
    plt.close()


def build_churn_notebook(filepath: str = "notebooks/03_customer_churn_intelligence.ipynb"):
    """Construct and execute the Task 3 Customer Churn Jupyter Notebook."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    nb = nbf.v4.new_notebook()

    cells = []
    cells.append(nbf.v4.new_markdown_cell("""# TASK 3: Customer Cohort, Churn & Retention Intelligence
### Diagnostic Cross-Sectional Cohort Analysis, High-Risk Segmentation, and Predictive Retention Modeling

**Author**: Vijay Maheswari  
**Framework**: RISK Methodology — Intelligence Extraction & Solution Development  
**Dataset**: Telco Customer Churn (7,043 validated subscriber profiles)
"""))

    cells.append(nbf.v4.new_code_cell("""import sys
import os

for p in [os.path.abspath(".."), os.path.abspath(".")]:
    if p not in sys.path:
        sys.path.insert(0, p)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from src.loaders import load_telco_churn
from src.cleaning import clean_telco_churn
from src.metrics import calculate_churn_kpis
from src.validation import validate_churn_schema

sns.set_theme(style="whitegrid", palette="muted")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 1. Dataset Ingestion & Quality Audit
We validate customer identifiers, resolve blank TotalCharges for tenure=0 new subscribers, and create standardized 12-month tenure cohorts.
"""))

    cells.append(nbf.v4.new_code_cell("""raw_df = load_telco_churn()
print(f"Raw churn records: {raw_df.shape}")

# Quality audit
audit = validate_churn_schema(raw_df)
print(audit.summary())

# Clean and transform
df = clean_telco_churn(raw_df)
print(f"Cleaned churn records: {df.shape}")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 2. Core Churn & Retention Scorecard
We calculate benchmark churn rate, retention rate, and cohort breakdown.
"""))

    cells.append(nbf.v4.new_code_cell("""kpis = calculate_churn_kpis(df)
print(f"Eligible Customers : {kpis['Eligible Customers']:,}")
print(f"Churned Customers  : {kpis['Churned Customers']:,} ({kpis['Churn Rate %']}%)")
print(f"Retained Customers : {kpis['Retained Customers']:,} ({kpis['Retention Rate %']}%)")
print(f"High-Risk Segment  : {kpis['High Risk Cohort Total']:,} customers with {kpis['High Risk Churn Rate %']}% Churn Rate")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 3. Tenure Cohort Retention Table
Analyzing churn across 12-month tenure bins highlights Year 1 vulnerability.
"""))

    cells.append(nbf.v4.new_code_cell("""kpis["Tenure Cohorts"]
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 4. Contract & Payment Breakdown
Evaluating contract stability and payment friction.
"""))

    cells.append(nbf.v4.new_code_cell("""print("Contract Breakdown:")
print(kpis["Contract Breakdown"])
print("Payment Method Breakdown:")
print(kpis["Payment Breakdown"])
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 5. Visual Diagnostics Generation
Render and export all 5 churn diagnostic and predictive figures.
"""))

    cells.append(nbf.v4.new_code_cell("""from src.generate_churn_intelligence import generate_churn_visualizations

generate_churn_visualizations(df, "outputs/figures")
print("Visualizations saved to outputs/figures/")
"""))

    cells.append(nbf.v4.new_markdown_cell("""## 6. Predictive Classification Modeling & Feature Attribution
We train a calibrated Logistic Regression classifier to predict subscriber churn likelihood and prevent target leakage.
"""))

    cells.append(nbf.v4.new_code_cell("""feature_cols = [
    "tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen",
    "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod"
]

X = pd.get_dummies(df[feature_cols], drop_first=True)
y = df["Churn_Numeric"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)

y_pred = lr.predict(X_test_scaled)
y_prob = lr.predict_proba(X_test_scaled)[:, 1]

print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Retained', 'Churned']))

# Top Risk & Retention Drivers
coefs = pd.Series(lr.coef_[0], index=X.columns).sort_values()
top_drivers = pd.concat([coefs.head(5), coefs.tail(5)])
print("Top 5 Retention Drivers (Negative) and Top 5 Churn Drivers (Positive):")
print(top_drivers)
"""))

    nb.cells = cells
    with open(filepath, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Saved churn notebook to {filepath}")


if __name__ == "__main__":
    df = clean_telco_churn(load_telco_churn())
    generate_churn_visualizations(df)
    build_churn_notebook()
