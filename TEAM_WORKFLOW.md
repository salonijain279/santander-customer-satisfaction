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

## File Ownership

Do not edit another member's files without coordinating first.

| Member | Files owned |
|---|---|
| Saloni | src/config.py, notebooks/06 |
| Shiv | notebooks/01 |
| Parul | src/features.py, notebooks/02, notebooks/03 |
| Madhu | notebooks/04 (MLP section) |
| Bhavisha | src/utils.py, notebooks/07 |
| All | src/models.py (own function each), notebooks/05, experiments.csv |

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
