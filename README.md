# Santander Customer Satisfaction — Predictive Analytics Project

## Overview

This repository contains the complete machine learning pipeline for predicting customer dissatisfaction at Santander Bank. The project is based on the Kaggle Santander Customer Satisfaction competition dataset.

Dissatisfied customers rarely communicate their concerns before leaving. This model identifies at-risk customers early, enabling proactive intervention before churn occurs.

**Competition:** Kaggle — Santander Customer Satisfaction
**Evaluation metric:** AUC-ROC
**Target variable:** 0 = satisfied, 1 = unsatisfied

---

## Dataset

| Property | Value |
|---|---|
| Training set | 76,020 customers × 371 columns |
| Test set | 75,818 customers × 370 columns |
| Features | 369 anonymized numeric features |
| Class distribution | 96.04% satisfied, 3.96% unsatisfied |
| Class ratio | approximately 24:1 |
| Missing values | encoded as sentinel integers/floats, not NaN |

---

## Team

| Member | Model | Primary files |
|---|---|---|
| Saloni | XGBoost | src/config.py, notebooks/06_ensemble_submission.ipynb |
| Shiv | LightGBM | notebooks/01_eda.ipynb |
| Parul | Random Forest | src/features.py, notebooks/02_cleaning.ipynb, notebooks/03_feature_engineering.ipynb |
| Madhu | Neural Network (MLP) | notebooks/04_baseline_models.ipynb |
| Bhavisha | Logistic Regression | src/utils.py, notebooks/07_model_correlation_check.ipynb |

---

## Repository Structure

```
santander-customer-satisfaction/
├── data/                          # local only — never committed
│   ├── raw/                       # place train.csv and test.csv here
│   └── processed/                 # generated pickle files go here
├── notebooks/                     # one notebook per project phase
│   ├── 01_eda.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_baseline_models.ipynb
│   ├── 05_hyperparameter_tuning.ipynb
│   ├── 06_ensemble_submission.ipynb
│   └── 07_model_correlation_check.ipynb
├── src/                           # shared Python modules
│   ├── config.py                  # all project constants and paths
│   ├── features.py                # cleaning and feature engineering functions
│   ├── utils.py                   # CV harness, scoring, experiment logging
│   └── models.py                  # baseline model configurations
├── outputs/
│   ├── oof/                       # out-of-fold arrays (local only)
│   ├── submissions/               # Kaggle submission log
│   └── feature_importance/        # per-model importance logs
├── reports/
│   └── business_translation.md    # business context and recommendations
├── data_dictionary.md             # complete feature reference
├── experiments.csv                # experiment tracking log
├── requirements.txt               # Python dependencies
└── .gitignore
```

---

## Project Phases

| Phase | Description | Days |
|---|---|---|
| 1 | Exploratory data analysis | Days 1–3 |
| 2 | Data cleaning | Days 3–4 |
| 3 | Feature engineering | Days 4–5 |
| 4 | Master dataframe | Day 5 |
| 5 | Baseline models | Day 6 |
| 6 | Hyperparameter tuning | Days 7–11 |
| 7 | Ensemble and submission | Days 12–14 |

---

## Key EDA Findings

- No customer under age 23 is dissatisfied (confirmed across 1,212 customers)
- Zero cash balance is the strongest balance-based predictor
- 65% of unsatisfied customers have zero average balance in last 3 months
- var36 = 99 appears in 40% of the data — treated as a valid category
- 34 constant columns confirmed and removed
- 26 delta columns contain 1e10 sentinel — all dropped

---

## Models

| Model | Category | Imbalance handling |
|---|---|---|
| Logistic Regression | Linear | class_weight=balanced |
| Random Forest | Bagging ensemble | class_weight=balanced |
| XGBoost | Gradient boosting | scale_pos_weight=20 |
| LightGBM | Leaf-wise boosting | is_unbalance=True |
| Neural Network (MLP) | Deep learning | class_weight={0:1, 1:24} |

---

## Data Integrity Rules

1. Never commit any file from data/ — gitignored automatically
2. y_train.pkl is always separate from X — never merge until model.fit()
3. Cleaning always on concat(train + test) — split back after
4. StandardScaler fit on fold training split only
5. SMOTE inside CV folds only — never before splitting
6. Post-processing on final predictions only — never during training

---

## Experiment Tracking

All model runs logged in experiments.csv
All Kaggle submissions logged in outputs/submissions/submissions_log.md
