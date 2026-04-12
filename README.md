# Santander Customer Satisfaction

Predict which bank customers are quietly dissatisfied — early
enough for Santander to step in before they leave.

> [!IMPORTANT]  
> **Team Members:** Before you start writing any code, please read the [Team Git Workflow](TEAM_WORKFLOW.md) guide carefully so everyone is on the same page!

## Business problem
Unhappy customers do not complain. They just close their account
and move to another bank. Santander wants to identify these
customers 1-3 months before they churn so relationship managers
can intervene with the right offer or support.

## Dataset
| Property | Value |
|---|---|
| Competition | Kaggle — Santander Customer Satisfaction |
| Training data | 76,020 customers, 369 features |
| Test data | 75,818 customers |
| Target | 0 = satisfied, 1 = unsatisfied |
| Class balance | 96% satisfied, 4% unsatisfied |
| Metric | AUC-ROC (accuracy is misleading at 96:4) |

## Team and file ownership
| Member | Role | Model | Files owned |
|---|---|---|---|
| Saloni | Project lead | XGBoost | src/config.py, src/models.py (XGB), notebook 06 |
| Shiv | EDA | LightGBM | notebook 01, src/models.py (LGBM), row stats features |
| Parul | Feature engineering | Random Forest | src/features.py, notebooks 02 and 03 |
| Madhu | Deep learning | Neural Network MLP | src/models.py (MLP), log transforms |
| Bhavisha | Validation | Logistic Regression | src/utils.py, notebook 07, temporal deltas |

## Sprint timeline
| Phase | What happens | Sprint days | Who leads |
|---|---|---|---|
| 0 Setup | Repo created, data downloaded, env set up | Day 1 | Saloni |
| 1 EDA | Explore data, confirm sentinel values, find patterns | Days 1-3 | Shiv |
| 2 Cleaning | Remove noise, impute sentinels, drop correlated | Days 3-4 | Parul + Bhavisha |
| 3 Feature eng | Create new features from EDA insights | Day 4-5 | Parul leads, all contribute |
| 4 Master df | Save master_train.pkl, master_test.pkl, y_train.pkl | Day 5 | Shiv |
| 5 Baselines | All 5 models run with default settings | Day 6 | One model each |
| 6 Tuning | Hyperparameter search, multi-seed averaging | Days 7-11 | All members |
| 7 Ensemble | Blend models, post-process, submit | Days 12-14 | Saloni + Bhavisha |

## How to use this repo

Step 1 — Get the data
Download from Kaggle and place train.csv and test.csv in data/raw/
Do not commit these files.

Step 2 — Install dependencies
pip install -r requirements.txt

Step 3 — Run notebooks in order
01_eda → 02_cleaning → 03_feature_engineering → 04_baseline_models
→ 05_hyperparameter_tuning → 06_ensemble_submission

Step 4 — Log every experiment
After every model run call log_experiment() from src/utils.py
This keeps experiments.csv up to date for the whole team.

Step 5 — Log every submission
Fill in outputs/submissions/submissions_log.md before every
Kaggle submission. Record public LB AUC after it scores.

## Key rules — never break these
1. Never commit data files — data/raw/ and data/processed/ are gitignored
2. y (TARGET) lives in y_train.pkl — never merge it into X
3. Clean train and test together — always concat, clean, split back
4. StandardScaler fits inside CV fold training split only
5. SMOTE inside CV folds only — never before the split
6. Post-processing rules apply to final predictions only

## Experiment results
See experiments.csv

## Submission history
See outputs/submissions/submissions_log.md
