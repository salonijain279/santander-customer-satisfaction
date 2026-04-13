# Business Context — Santander Customer Satisfaction

## Problem Statement

Santander Bank serves millions of retail banking customers. A proportion of these customers are dissatisfied with their banking experience. Critically, dissatisfied customers rarely communicate their concerns — they simply close their accounts and move to a competitor without warning.

Early identification of at-risk customers allows relationship managers to intervene with targeted offers or service improvements before the customer churns.

---

## Model Output and Recommended Actions

The model assigns each customer a probability score between 0 and 1. Score of 0 = very likely satisfied. Score of 1 = very likely dissatisfied.

| Score | Risk level | Recommended action |
|---|---|---|
| 0.70 and above | Critical | Direct contact within 24 hours. Assign relationship manager. Offer retention package. |
| 0.40 to 0.70 | High | Send personalised satisfaction survey. Offer product upgrade or fee waiver. |
| 0.20 to 0.40 | Moderate | Include in next outreach campaign. Monitor for changes. |
| Below 0.20 | Low | No immediate action required. |

---

## Business Sub-Questions

**Q1: Which customers are at risk right now?**
Customers with a score above 0.40 — approximately 3 to 5 percent of the total customer base.

**Q2: What are the earliest detectable signals?**
- Zero cash balance (saldo_var30 = 0)
- Zero average balance last 3 months (saldo_medio_var5_ult3 = 0)
- Low number of active products (num_var4)
- Customer age above 80

These signals appear 1 to 3 months before observable churn.

**Q3: How early can the model detect dissatisfaction?**
The model uses data from the last 1 and 3 months. Detection is possible approximately 1 to 3 months before churn.

**Q4: Why AUC-ROC and not accuracy?**
At 96:4 imbalance, predicting everyone as satisfied gives 96% accuracy but zero predictive value. AUC-ROC measures how well the model separates the two groups regardless of imbalance. A score of 0.84 means the model correctly ranks a dissatisfied customer above a satisfied one 84% of the time.

---

## Estimated Business Impact

| Metric | Value |
|---|---|
| At-risk customers identified (50% detection) | 1,500 |
| Successful retentions (40% intervention rate) | 600 |
| Estimated revenue retained at $3,000 LTV | $1,800,000 |

Conservative single-cohort estimate.
