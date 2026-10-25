# Strategic Retention Memorandum: Customer Churn Intelligence

**Framework**: RISK Methodology — Intelligence Extraction & Knowledge Delivery  
**Cohort Scope**: 7,043 validated subscriber accounts (1,869 Churned | 5,174 Retained)  
**Baseline Churn Rate**: 26.54% | **Baseline Retention Rate**: 73.46%  
**Author**: Vijay Maheswari  

---

## Executive Summary

Customer attrition in the telecommunications subscriber base is highly concentrated rather than random. Over **88.5% of all churn occurs within Month-to-Month contracts**, and **55.5% occurs during the first 12 months of customer tenure**. Most critically, our analysis isolates a specific subscriber segment—the **"Toxic Triad"** (Month-to-Month contract + Fiber Optic internet + Electronic Check payment)—that experiences an alarming **60.37% churn rate**. 

Deploying targeted onboarding protocols, contract migration incentives, and automated payment migration is projected to reduce annualized churn by **4.2 to 6.5 percentage points**, preserving an estimated **$1.8M to $2.7M in recurring annual revenue**.

---

## Quantified Analytical Observations

| ID | Dimension | Measured Quantity | Comparison / Baseline | Business Implication |
| :--- | :--- | :--- | :--- | :--- |
| **OBS-01** | Tenure Cohort | **47.44% Churn** in 0–12m cohort (1,037 of 2,186) | 6.61% Churn in 61–72m cohort (93 of 1,407) | Year 1 represents the primary attrition cliff; long-tenured customers exhibit 93.4% loyalty. |
| **OBS-02** | Contract Type | **42.71% Churn** on Month-to-Month (1,655 of 3,875) | 2.83% Churn on Two-Year contracts (48 of 1,695) | Month-to-Month accounts represent 88.55% of all lost subscribers. |
| **OBS-03** | Payment Method | **45.29% Churn** via Electronic Check (1,071 of 2,365) | 15.24% Churn on Automatic Credit Card (232 of 1,522) | Manual electronic check payments trigger monthly re-evaluation and friction. |
| **OBS-04** | Internet Service | **41.89% Churn** on Fiber Optic (1,297 of 3,096) | 18.96% Churn on DSL (459 of 2,421) | Premium Fiber subscribers face service-quality or price-value disconnects. |
| **OBS-05** | Service Add-ons | **41.64% Churn** without Tech Support (1,446 of 3,473) | 15.17% Churn with Tech Support (310 of 2,044) | Tech Support acts as an indispensable operational retention anchor (-26.5% delta). |
| **OBS-06** | Toxic Triad | **60.37% Churn** in High-Risk Segment (789 of 1,307) | 26.54% Portfolio Average | Represents 18.56% of subscribers but 42.22% of aggregate customer loss. |

---

## Prioritized Strategic Retention Recommendations

### Recommendation 1: "First 90 Days" VIP Onboarding & Complimentary Tech Support Bundle
* **Target Segment**: All newly acquired subscribers (Tenure 0–3 months), specifically those selecting Fiber Optic internet without technical support (Tenure 0–12m churn rate: 47.44%).
* **Supporting Evidence**: Subscribers with Tech Support experience a **15.17% churn rate**, compared to **41.64%** for subscribers without support. Lack of support nearly triples subscriber departure hazard.
* **Proposed Intervention**:
  1. Bundle 6 months of complimentary Tech Support and Online Security into all new broadband activations.
  2. Implement automated day-7, day-30, and day-60 customer success check-ins via SMS and app notifications to verify router performance and Wi-Fi coverage.
* **Expected Direction of Impact**: Significant reduction in early tenure churn; increases Year 1 retention from 52.56% to approximately 68–72%.
* **Metric for Measuring Success**: 90-day and 180-day cohort retention rates; first-time tech support ticket resolution CSAT.
* **Limitations & Required Validation**: Cross-sectional data does not reveal whether customers chose not to buy tech support because they were tech-savvy or because the price was too high. Requires randomized A/B trial testing free support vs control.

---

### Recommendation 2: Auto-Pay Migration & Annual Contract Incentive Program
* **Target Segment**: Current Month-to-Month subscribers paying via Electronic Check (2,365 subscribers with 45.29% churn rate).
* **Supporting Evidence**: Subscribers paying via Electronic Check churn at **45.29%**, compared to only **15.24%** for Credit Card auto-pay and **16.71%** for Bank auto-pay. Month-to-Month contracts drive **88.55%** of all enterprise churn.
* **Proposed Intervention**:
  1. Offer an immediate $10/month bill credit for 12 months in exchange for migrating from Month-to-Month to a 12-month contract commitment.
  2. Offer a one-time $25 statement credit upon enrollment in recurring ACH bank auto-pay or credit card billing.
* **Expected Direction of Impact**: Substantial reduction in monthly payment friction and bill shock, moving subscribers from high-risk 45% churn tiers into stable 11–15% tiers.
* **Metric for Measuring Success**: Electronic check share reduction (target: <15% of subscriber base); 12-month contract renewal rate.
* **Limitations & Required Validation**: Requires financial margin modeling to ensure the $10/month credit is offset by the extended customer lifetime value (LTV).

---

### Recommendation 3: Fiber Optic Quality Assurance & Network Sentry Protocol
* **Target Segment**: Fiber Optic subscribers generating higher monthly bills ($70–$100+/mo) experiencing a 41.89% churn rate.
* **Supporting Evidence**: Fiber Optic customers pay higher monthly fees but churn at **41.89%** vs DSL at **18.96%**. Machine learning model coefficients rank Fiber Optic as the #1 single positive driver of subscriber churn (+0.7762 coefficient).
* **Proposed Intervention**:
  1. Deploy automated network speed and latency probes on subscriber routers to proactively identify micro-outages before the customer files a complaint.
  2. Create a specialized Fiber Retention Concierge team empowered to dispatch free technician visits or issue automatic outage credits.
* **Expected Direction of Impact**: Mitigates quality dissatisfaction among high-ARPU subscribers, protecting high-value recurring cash flows.
* **Metric for Measuring Success**: Net Promoter Score (NPS) among Fiber Optic customers; Fiber churn reduction (target: <25%).
* **Limitations & Required Validation**: The dataset lacks network telemetry, ticket logs, or speed speed-test data; causality between technical faults and churn must be confirmed through operational ticketing systems.

---

## Machine Learning Predictive Risk Framework

* **Algorithm**: Standardized Logistic Regression & Random Forest Classifier (80/20 train/test split, random seed = 42).
* **Model Validation Metrics**:
  * **ROC-AUC**: **0.8418** (vs 0.5000 random baseline).
  * **Precision**: **65.84%** | **Recall**: **56.68%** | **Overall Accuracy**: **80.70%**.
* **Operational Application**:
  * Score all active subscribers weekly.
  * Route accounts with predicted churn probability $> 0.65$ directly to the proactive retention queue before their contract anniversary or billing cycle.
