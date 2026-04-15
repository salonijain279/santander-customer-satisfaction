# Team Workflow — Git and Collaboration Guide

---

## Initial Setup (one time only — Day 1)

**Step 1 — Clone the repository:**
```
git clone https://github.com/salonijain279/santander-customer-satisfaction.git
cd santander-customer-satisfaction
```

**Step 2 — Install all libraries:**
```
pip install -r requirements.txt
```

**Step 3 — Create the data folder locally:**
```
mkdir -p data/raw
mkdir -p data/processed
```

**Step 4 — Download data from Kaggle:**
Download train.csv and test.csv from the competition page and place both files inside data/raw/. These files are gitignored and will never be committed.

---

## Daily Workflow (every working day)

**Morning — before touching anything:**
```
git pull
```
Downloads all changes your teammates pushed. Always do this first.

**During the day:**
Work in your assigned notebook or file as normal.

**Evening — after finishing:**
```
git add .
git commit -m "Name: what you completed today"
git push
```

**Commit message examples:**
```
Saloni: XGBoost baseline complete, CV AUC 0.821
Parul: drop_constant_cols and impute_sentinels implemented
Bhavisha: run_cv function built with leakage prevention
Shiv: sparsity map and var38 analysis done
Madhu: MLP baseline running, CV AUC 0.807
```

---

## File Ownership and Day-by-Day Plan

### Who works in which notebook each day

| Day | Saloni | Shiv | Parul | Madhu | Bhavisha |
|---|---|---|---|---|---|
| 1 | Repo setup, config.py | 01_eda.ipynb — load data, class balance | 01_eda.ipynb — prefix taxonomy | Environment setup | experiments.csv setup |
| 2 | 01_eda.ipynb — Layer 1, 2 | 01_eda.ipynb — Layer 3 sparsity | 01_eda.ipynb — var15 deep dive | 01_eda.ipynb — var38 deep dive | 01_eda.ipynb — train vs test KDE |
| 3 | 01_eda.ipynb — Layer 4 correlation + top 50 | 01_eda.ipynb — Layer 5 scatter + heatmap | 02_cleaning.ipynb — drop constants + duplicates | 02_cleaning.ipynb — sentinel imputation | 02_cleaning.ipynb — drop sparse + correlated |
| 4 | Review + verify cleaning shapes | 03_feature_engineering.ipynb — row statistics | 03_feature_engineering.ipynb — rule flags | 03_feature_engineering.ipynb — log transforms | 03_feature_engineering.ipynb — temporal deltas |
| 5 | Feature selection — save top_250 and top_50 | Save master_train.pkl, master_test.pkl, y_train.pkl | Finalise features.py | StandardScaler + PCA pipelines | Build utils.py CV harness |
| 6 | 04_baseline_models.ipynb — XGBoost | 04_baseline_models.ipynb — LightGBM | 04_baseline_models.ipynb — Random Forest | 04_baseline_models.ipynb — MLP | 04_baseline_models.ipynb — Logistic Regression |
| 7 | Compile all 5 AUC scores | 05_hyperparameter_tuning.ipynb — LGBM tuning | 05_hyperparameter_tuning.ipynb — RF tuning | 05_hyperparameter_tuning.ipynb — MLP tuning | 05_hyperparameter_tuning.ipynb — LogReg tuning |
| 8 | 05_hyperparameter_tuning.ipynb — XGB Bayesian tuning | Review LGBM results | Test XGBRFClassifier | keras_tuner Hyperband | Collect all OOF arrays |
| 9 | Finalise XGBoost — 5 seeds | Finalise LightGBM — 5 seeds | Finalise Random Forest — 5 seeds | Finalise MLP — 5 seeds | Finalise LogReg — 5 seeds |
| 10 | 06_ensemble_submission.ipynb — weighted blend | Rank-average blend | Stack Layer 1 — LogReg meta | Stack Layer 2 — XGB meta | Post-processing rules |
| 11 | Compare public LB vs CV AUC | LGBM experiments | RF + PCA experiment | SMOTE vs no-SMOTE ablation | Compile experiment summary |
| 12 | Final XGBoost — full train + 10 seeds | Final LightGBM — full train + 10 seeds | Final RF — full train + 10 seeds | Final MLP — full train + 5 seeds | Final LogReg + stacking |
| 13 | Build 3 submission files, validate all | Write README updates | Write feature engineering docs | Write model documentation | Write validation strategy doc |
| 14 | Submit to Kaggle, select final 2 | Presentation slides | Finalise notebooks | Finalise notebooks | Repo cleanup |

### File ownership (src/ files)

| Member | Files owned |
|---|---|
| Saloni | src/config.py, notebooks/06_ensemble_submission.ipynb |
| Shiv | notebooks/01_eda.ipynb |
| Parul | src/features.py, notebooks/02_cleaning.ipynb, notebooks/03_feature_engineering.ipynb |
| Madhu | notebooks/04_baseline_models.ipynb (MLP section) |
| Bhavisha | src/utils.py, notebooks/05_hyperparameter_tuning.ipynb |

---

## Shared Files — Update After Every Run

experiments.csv — one row per model run, every time without exception
outputs/submissions/submissions_log.md — before every Kaggle submission
outputs/feature_importance/feature_importance_log.md — top 5 features after every model run

---

## If Push Fails

Someone pushed while you were working. Run:
```
git pull
git push
```

If a conflict appears in the same file, contact Saloni.

---

## What Gets Committed and What Does Not

| Item | Committed | Reason |
|---|---|---|
| Notebooks | Yes | Team's actual work |
| src/ files | Yes | Shared code |
| Markdown files | Yes | Documentation |
| experiments.csv | Yes | Shared log |
| data/raw/*.csv | No | Kaggle rules + 55MB file size |
| data/processed/*.pkl | No | Large, reproducible from code |
| outputs/oof/*.npy | No | Large, reproducible |
| outputs/submissions/*.csv | No | Kaggle redistribution rules |
| .DS_Store | No | Mac system file |

---

## Rules — Never Break

1. git pull every morning before starting
2. Never commit any file from data/
3. Never change constants in src/config.py
4. StandardScaler and encoders always fit inside CV folds only
5. Log every model run in experiments.csv before moving on
