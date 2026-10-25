"""Predictive Customer Churn Classifier and Risk Scoring Engine.

Part of RISK Autonomous Business Analytics & Decision Intelligence Engine.
Implements calibrated machine learning models to identify churn propensity,
report ROC-AUC / PR metrics, and isolate feature importance.
"""

import os
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    roc_auc_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from src.loaders import load_telco_churn
from src.cleaning import clean_telco_churn

TABLES_DIR = "outputs/tables"


def train_and_evaluate_churn_models(export_tables: bool = True):
    """Train baseline, Logistic Regression, and Random Forest classifiers."""
    os.makedirs(TABLES_DIR, exist_ok=True)
    df = clean_telco_churn(load_telco_churn())

    feature_cols = [
        "tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen",
        "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
        "PaperlessBilling", "PaymentMethod"
    ]

    X = pd.get_dummies(df[feature_cols], drop_first=True)
    y = df["Churn_Numeric"]

    # 80/20 Stratified train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # Standardize numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 1. Baseline Dummy Classifier
    dummy = DummyClassifier(strategy="most_frequent")
    dummy.fit(X_train, y_train)
    dummy_pred = dummy.predict(X_test)
    dummy_prob = dummy.predict_proba(X_test)[:, 1]

    # 2. Logistic Regression (Primary Explanatory Model)
    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train_scaled, y_train)
    lr_pred = lr.predict(X_test_scaled)
    lr_prob = lr.predict_proba(X_test_scaled)[:, 1]

    # 3. Random Forest (Nonlinear Ensemble Model)
    rf = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    rf_prob = rf.predict_proba(X_test)[:, 1]

    metrics_ledger = [
        {
            "Model": "Baseline (Most Frequent)",
            "Accuracy": accuracy_score(y_test, dummy_pred),
            "Precision": 0.0,
            "Recall": 0.0,
            "F1-Score": 0.0,
            "ROC-AUC": roc_auc_score(y_test, dummy_prob),
        },
        {
            "Model": "Logistic Regression",
            "Accuracy": accuracy_score(y_test, lr_pred),
            "Precision": precision_score(y_test, lr_pred),
            "Recall": recall_score(y_test, lr_pred),
            "F1-Score": f1_score(y_test, lr_pred),
            "ROC-AUC": roc_auc_score(y_test, lr_prob),
        },
        {
            "Model": "Random Forest (Depth=8)",
            "Accuracy": accuracy_score(y_test, rf_pred),
            "Precision": precision_score(y_test, rf_pred),
            "Recall": recall_score(y_test, rf_pred),
            "F1-Score": f1_score(y_test, rf_pred),
            "ROC-AUC": roc_auc_score(y_test, rf_prob),
        },
    ]

    metrics_df = pd.DataFrame(metrics_ledger)

    # Feature Importance (Standardized Logistic Coefficients)
    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": lr.coef_[0],
        "Abs_Impact": np.abs(lr.coef_[0]),
        "Direction": np.where(lr.coef_[0] > 0, "Increases Churn", "Increases Retention")
    }).sort_values("Abs_Impact", ascending=False)

    if export_tables:
        metrics_df.to_csv(os.path.join(TABLES_DIR, "churn_model_metrics.csv"), index=False)
        importance_df.to_csv(os.path.join(TABLES_DIR, "churn_feature_importance.csv"), index=False)

    return {
        "metrics": metrics_df,
        "feature_importance": importance_df,
        "model": lr,
    }


if __name__ == "__main__":
    results = train_and_evaluate_churn_models()
    print("=== MODEL PERFORMANCE COMPARISON ===")
    print(results["metrics"].to_string(index=False))
    print("\n=== TOP 10 PREDICTIVE FEATURES ===")
    print(results["feature_importance"].head(10).to_string(index=False))
