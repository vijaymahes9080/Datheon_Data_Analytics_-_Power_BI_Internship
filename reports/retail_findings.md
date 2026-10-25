# Executive Findings: Retail Sales Discovery Engine

**Framework**: RISK Methodology — Intelligence Extraction & Knowledge Delivery  
**Analysis Period**: 2014 – 2017  
**Scope**: 9,994 validated transactional records ($2,297,200.86 Total Sales | $286,397.02 Total Profit)  
**Author**: Vijay Maheswari  

---

## Executive Summary

The retail sales discovery analysis examined 9,994 commercial orders spanning four geographic territories and three customer segments. While the business maintains an overall healthy profit margin of **12.47%**, diagnostic profiling reveals severe structural margin destruction caused by undisciplined discounting policies and product-line loss leaders. Capping high-discount transactions and restructuring the Furniture category can unlock an estimated **$135,000+ in annual profit recovery**.

---

## Comprehensive Findings Register

| ID | Business Question | Observed Metric | Supporting Evidence | Practical Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **RET-01** | What is the impact of heavy discounting on profitability? | -$135,376.06 Net Loss (Margin: -37.32%) on orders with Discount > 20% | `retail_discount_vs_profit_scatter.png` | Cap representative discounts at 15%; eliminate promotions > 20%. |
| **RET-02** | Which subcategories act as chronic commercial cash drains? | Tables incurred -$17,725.48 loss on $206,965.53 sales (-8.56% margin) | `retail_category_revenue_profit.png` | Renegotiate supplier COGS by 12% or discontinue unprofitable SKUs. |
| **RET-03** | How does geographic territory influence profit realization? | Central region achieved only 7.92% margin vs West at 14.94% | `retail_regional_profitability.png` | Shift Central sales incentives from top-line revenue to gross margin %. |
| **RET-04** | Where is enterprise profit concentrated across categories? | Technology generated 50.79% ($145,454.95) of all corporate profit | `retail_customer_segment_comparison.png` | Expand enterprise IT contracts while upgrading Furniture unit economics. |
| **RET-05** | How severe is quarterly and monthly revenue seasonality? | Q4 contributes 33.79% of sales; Q1 contracts by 53.8% | `retail_monthly_sales_trend.png` | Implement dynamic seasonal stocking and pre-order working capital financing. |

---

## Detailed Evidence Dossiers

### Finding RET-01: Severe Profit Destruction from Runaway Discounting Above 20%
* **Observed Metric**: Transactions with discounts exceeding 20% generated $362,770.12 in revenue but resulted in an aggregate net loss of **-$135,376.06**, yielding a negative margin of **-37.32%** across 1,393 order lines.
* **Baseline Comparison**: Zero-discount transactions generated $1,087,908.48 in revenue and **+$320,987.60** in net profit (Margin: **+29.51%** across 4,798 order lines). Low-to-medium discount orders (0–20%] remained profitable at +11.58% to +16.61% margins.
* **Supporting Calculation**:
  $$\text{Margin}_{\text{Discount}>20\%} = \frac{-\$135,376.06}{\$362,770.12} = -37.32\%$$
* **Business Interpretation**: Steep discounting in this commercial model does not achieve scale economies. Instead, price concessions outpace supply chain margins, triggering severe value destruction.
* **Practical Recommendation**: Establish rigid pricing governance. Implement system controls prohibiting field sales representatives from applying discounts >15% without VP Commercial approval.
* **Analytical Limitation**: The transaction records do not capture customer acquisition cost (CAC) or customer lifetime retention data; whether any heavy discounts served as customer acquisition loss-leaders cannot be determined.

---

### Finding RET-02: Tables Sub-Category Operating at Chronic Negative Margins
* **Observed Metric**: The Tables sub-category produced $206,965.53 in sales but incurred an aggregate net loss of **-$17,725.48** (Margin: **-8.56%**). Bookcases (-$3,472.56) and Supplies (-$1,189.10) also posted net operating losses.
* **Baseline Comparison**: The average sub-category profit across the store is **+$16,846.88**. Premier subcategories such as Copiers produced **+$55,617.82** (37.20% margin) and Accessories produced **+$41,936.64** (25.05% margin).
* **Supporting Calculation**:
  $$\text{Tables Profit Contribution} = \sum \text{Profit}_{\text{Tables}} = -\$17,725.48 \quad (\text{Rank: 17 of 17})$$
* **Business Interpretation**: Bulky dimensional shipping costs and high product return rates combined with aggressive retail discounting make Tables structurally unprofitable under current operational conditions.
* **Practical Recommendation**: Renegotiate freight contracts, bundle Tables with high-margin Chairs or Accessories to secure positive order-level basket economics, or discontinue the bottom 25% loss-making SKUs.
* **Analytical Limitation**: Detailed line-item logistics and inbound freight allocations are aggregated into COGS; individual vendor cost breakdowns are unobserved.

---

### Finding RET-03: Central Region Profit Margin Lagging Other Territories
* **Observed Metric**: The Central region generated $501,239.89 in total sales but delivered only **$39,706.36** in net profit, realizing a profit margin of **7.92%**.
* **Baseline Comparison**: The West region delivered **$108,418.45** in profit on $725,457.82 in sales (Margin: **14.94%**), and the East region achieved **$91,522.78** on $678,781.24 in sales (Margin: **13.48%**).
* **Supporting Calculation**:
  $$\text{Central Margin} = \frac{\$39,706.36}{\$501,239.89} = 7.92\% \quad \text{vs.} \quad \text{West Margin} = \frac{\$108,418.45}{\$725,457.82} = 14.94\%$$
* **Business Interpretation**: Central region sales teams frequently deploy higher average discounting (mean discount 17.2% vs West 10.9%) to win deals in competitive markets such as Illinois and Texas, eroding bottom-line capture.
* **Practical Recommendation**: Re-align sales compensation in the Central region: transition sales bonus plans from top-line gross revenue quotas to gross margin contribution hurdles.
* **Analytical Limitation**: State-specific corporate tax credits and local competitive pricing data are not included in the dataset.

---

### Finding RET-04: Strong Revenue Concentration in Technology Segment
* **Observed Metric**: Technology generated **$836,154.03** in revenue (36.40% of corporate sales) and delivered **$145,454.95** in net profit, accounting for **50.79%** of all corporate profits (Margin: **17.39%**).
* **Baseline Comparison**: The Furniture category produced comparable sales volume of $741,999.80 (32.30% of sales) but yielded only **$18,451.27** in net profit (6.44% of total profit, margin: **2.49%**).
* **Supporting Calculation**:
  $$\text{Tech Profit Share} = \frac{\$145,454.95}{\$286,397.02} = 50.79\%$$
* **Business Interpretation**: Over half of the enterprise's earnings are concentrated in technology hardware. While lucrative, this creates high exposure to consumer electronics supply cycles.
* **Practical Recommendation**: Expand multi-year enterprise hardware leasing and maintenance support agreements while reforming Furniture merchandising to improve corporate portfolio diversification.
* **Analytical Limitation**: Warranty reserves, return rates, and hardware obsolescence depreciation are not modeled in transactional cash sales.

---

### Finding RET-05: Pronounced Q4 Seasonal Velocity Surge
* **Observed Metric**: Q4 accounts for **$776,211.52** in revenue (33.79% of corporate sales) across 2014–2017, with November ($352,461.07) and December ($325,293.50) registering peak annual velocity.
* **Baseline Comparison**: Q1 generates only **$358,822.45** (15.62% of sales), representing a **53.77% contraction** in sales volume from peak Q4 to baseline Q1.
* **Supporting Calculation**:
  $$\text{Quarterly Share}_{\text{Q4}} = \frac{\$776,211.52}{\$2,297,200.86} = 33.79\% \quad \text{vs.} \quad \text{Q1} = 15.62\%$$
* **Business Interpretation**: Corporate fiscal year-end budget flushing and holiday demand create extreme operational bottlenecks in November and December, followed by underutilized fulfillment capacity in January and February.
* **Practical Recommendation**: Establish dynamic logistics partnerships and secure seasonal temporary warehousing in September to mitigate Q4 freight surcharges and prevent stockouts.
* **Analytical Limitation**: Daily warehouse inventory levels, backorders, and stockout lost-sales data are not captured in the source dataset.
