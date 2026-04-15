# Project Status Report — Santander Customer Satisfaction
**Date:** April 15, 2026
**Sprint day:** 4 of 14 (today)
**Status:** In Progress — pipeline bug found, notebooks need output verification

---

## Summary

The team has made meaningful progress through Days 1–4, with EDA, cleaning, and two src/ functions implemented. However, a **critical bug exists in `02_cleaning.ipynb`**: the notebook loaded already-processed data (116 features) instead of raw data (369 features), so the constant-drop and duplicate-drop steps show 0 removals — they never ran on the right input. This means `clean_train.csv` was produced from the wrong starting point and cannot be trusted yet. Additionally, `03_feature_engineering.ipynb` has zero executed outputs. Bhavisha's cleaning work exists at the **root level** (`Top100_Features_correlation.ipynb`) instead of inside `notebooks/`. Day 5 is the hard deadline for a working pipeline — baseline modelling starts Day 6.

---

## Notebook output status (verified from actual files today)

| Notebook | Cells | Code cells | With outputs | Status |
|---|---|---|---|---|
| `01_eda.ipynb` | 31 | 21 | 20 | ✅ Mostly complete — 1 new cell needs running (Madhu var38 plot) |
| `02_cleaning.ipynb` | 24 | 13 | 10 | ⚠️ **BUG** — loaded wrong data; constant + duplicate drops show 0 |
| `03_feature_engineering.ipynb` | 19 | 9 | 0 | ❌ No outputs at all — never executed |
| `04_baseline_models.ipynb` | 2 | 1 | 0 | ❌ Import shell only — not started |
| `05_hyperparameter_tuning.ipynb` | 2 | 1 | 0 | ❌ Import shell only — Day 7 |
| `06_ensemble_submission.ipynb` | 2 | 1 | 0 | ❌ Import shell only — Day 12 |
| `07_model_correlation_check.ipynb` | 2 | 1 | 0 | ❌ Import shell only — Day 9 |
| `Top100_Features_correlation.ipynb` | 23 | 22 | 14 | ⚠️ Has outputs but **at root level** (not in notebooks/) |

---

## Critical bug — `02_cleaning.ipynb`

**What happened:** The notebook loads data and runs cleaning steps, but Cell 2 output shows:
```
Train shape: (76020, 371)    ← 371 not 369 — includes ID + TARGET
Combined shape: (151838, 369)
Constant features found: 0   ← WRONG — should be 34
Features remaining: 116      ← WRONG starting point
```
The notebook somehow already received data with only 116 features as its starting shape. The constant and duplicate drops found nothing because the data was already pre-filtered. **`clean_train.csv` / `clean_test.csv` must be regenerated from raw data.**

**Fix:** Parul must re-run `02_cleaning.ipynb` from raw `train.csv` → should show 369 features at start, 34 constants dropped, 27 duplicates dropped, then sparse + correlation drops.

---

## What each member has actually done (confirmed from repo)

### Saloni ✅
- Repo structure, all docs, `src/config.py` (complete), `src/utils.py` (2 functions live)
- `01_eda.ipynb` Layers 1–3: all 20 code cells have outputs ✅

### Bhavisha ⚠️
- `Top100_Features_correlation.ipynb` — at root level, not `notebooks/` — needs to move
- Kaggle notebook: constant drop → sparse drop → correlation drop → sentinel imputation → is_young flag → top 100 by correlation — all confirmed with outputs
- `run_cv()`, `log_experiment()`, `add_temporal_deltas()`, `drop_high_correlation_cols()` — all stubs

### Parul ⚠️
- `02_cleaning.ipynb` — present with outputs but **loaded wrong input** → results invalid
- `03_feature_engineering.ipynb` — written but **zero executed outputs**
- `src/features.py` — `drop_constant_cols`, `drop_duplicate_cols`, `add_rule_flags` still stubs

### Madhu ✅
- `impute_sentinels()` in `src/features.py` — implemented and tested ✅
- `add_log_transforms()` in `src/features.py` — 121 log columns, no inf/NaN ✅
- `outputs/var38_distribution.png` — saved ✅
- `notebooks/madhu_eda` — was empty 0-byte file, now removed ✅

### Shiv ❌
- Zero commits. Row statistics, Layer 4/5 EDA — nothing done.

---

## What is complete ✅

- Dataset shape, nulls, dtypes — confirmed (76,020 × 369, zero nulls)
- Class imbalance — 96.04% / 3.96%, AUC-ROC confirmed as metric
- Feature anatomy — all prefix and suffix groups mapped
- Constant columns — 34 confirmed (369 → 335)
- Duplicate columns — 27 confirmed, full name list available
- Sentinel values — all 3 identified, coded in `config.py`
- `impute_sentinels()` — implemented by Madhu ✅
- `add_log_transforms()` — 121 columns, implemented by Madhu ✅
- `var15` rule — 0 unsatisfied under age 23, confirmed post-processing rule
- `saldo_zero` AUC 0.6649, `saldo5_ult3_zero` AUC 0.6650 — strong signals confirmed
- `src/config.py` — complete ✅
- `01_eda.ipynb` — 20/21 code cells have outputs ✅
- EDA notebooks merged into one clean `01_eda.ipynb` ✅

## What is missing ❌

- `02_cleaning.ipynb` must be re-run from raw data (Parul — **TODAY**)
- `03_feature_engineering.ipynb` must be executed (Parul — **TODAY**)
- `master_train.pkl`, `master_test.pkl`, `y_train.pkl` — not saved (Saloni — Day 5)
- `run_cv()`, `run_cv_multiseed()`, `log_experiment()` in `src/utils.py` (Bhavisha — Day 5)
- `add_temporal_deltas()` in `src/features.py` (Bhavisha — Day 4, overdue)
- `drop_high_correlation_cols()` in `src/features.py` (Bhavisha — Day 5)
- `add_row_statistics()` in `src/features.py` (Shiv — Day 4, **overdue**)
- `add_rule_flags()` in `src/features.py` (Parul — Day 4, overdue)
- `drop_constant_cols()`, `drop_duplicate_cols()` in `src/features.py` (Parul)
- All 5 model stubs in `src/models.py` (All — Day 6)
- `Top100_Features_correlation.ipynb` at root — should be in `notebooks/` or content merged

---

## Day-by-day plan — starting today (April 15)

### Day 4 — Today (April 15) — Fix the pipeline

| Member | Task | Notebook / File | Done by |
|---|---|---|---|
| **Parul** | Re-run `02_cleaning.ipynb` from raw data — fix bug, get correct outputs | `notebooks/02_cleaning.ipynb` | Tonight |
| **Parul** | Execute `03_feature_engineering.ipynb` top to bottom — all cells must show outputs | `notebooks/03_feature_engineering.ipynb` | Tonight |
| **Parul** | Implement `drop_constant_cols()`, `drop_duplicate_cols()`, `add_rule_flags()` in `src/features.py` | `src/features.py` | Tonight |
| **Shiv** | Implement `add_row_statistics()` in `src/features.py` — count_zeros, row_sum, etc. | `src/features.py` | Tonight |
| **Shiv** | Add Layer 4 cells to `01_eda.ipynb` — top 30 features by correlation, ranked bar chart | `notebooks/01_eda.ipynb` | Tonight |
| **Bhavisha** | Implement `add_temporal_deltas()` in `src/features.py` | `src/features.py` | Tonight |
| **Bhavisha** | Move `Top100_Features_correlation.ipynb` into `notebooks/` folder | `notebooks/` | Tonight |
| **Madhu** | Run the Madhu var38 cell in `01_eda.ipynb` (cell 26) and push with output | `notebooks/01_eda.ipynb` | Tonight |
| **All** | Push everything before midnight | git | Tonight |

---

### Day 5 — April 16 — Lock the pipeline

| Member | Task | Notebook / File | Done by |
|---|---|---|---|
| **Saloni** | Confirm `02_cleaning.ipynb` shows correct numbers (369 → 335 → 308 → ...) | `notebooks/02_cleaning.ipynb` | Morning |
| **Saloni** | Run `run_full_cleaning_pipeline()` + `run_full_feature_pipeline()` → save `master_train.pkl`, `master_test.pkl`, `y_train.pkl` | `src/features.py` + terminal | EOD |
| **Saloni** | Decide feature selection: top 250 (trees) + top 50 (linear) by RF+XGB+MI | `src/features.py` | EOD |
| **Parul** | Wire `run_full_cleaning_pipeline()` in `src/features.py` | `src/features.py` | EOD |
| **Parul** | Wire `run_full_feature_pipeline()` in `src/features.py` | `src/features.py` | EOD |
| **Bhavisha** | Implement `run_cv()` — 5-fold stratified, returns OOF + AUC | `src/utils.py` | EOD |
| **Bhavisha** | Implement `log_experiment()` — appends row to experiments.csv | `src/utils.py` | EOD |
| **Bhavisha** | Implement `drop_high_correlation_cols()` in `src/features.py` | `src/features.py` | EOD |
| **Shiv** | Save `master_train.pkl`, `master_test.pkl`, `y_train.pkl` via StandardScaler pipeline | `src/features.py` | EOD |
| **Madhu** | Implement `get_mlp_baseline()` skeleton in `src/models.py` | `src/models.py` | EOD |
| **All** | Confirm master pkl shape in group chat — GATE for Day 6 | — | EOD |

---

### Day 6 — April 17 — Baseline models

| Member | Task | Notebook / File | Done by |
|---|---|---|---|
| **Saloni** | XGBoost baseline — 5-fold CV, log to experiments.csv | `notebooks/04_baseline_models.ipynb` | EOD |
| **Shiv** | LightGBM baseline — 5-fold CV, log to experiments.csv | `notebooks/04_baseline_models.ipynb` | EOD |
| **Parul** | Random Forest baseline — 5-fold CV, log to experiments.csv | `notebooks/04_baseline_models.ipynb` | EOD |
| **Madhu** | MLP baseline — 5-fold CV with class_weight, log to experiments.csv | `notebooks/04_baseline_models.ipynb` | EOD |
| **Bhavisha** | Logistic Regression baseline — 5-fold CV with scaling, log to experiments.csv | `notebooks/04_baseline_models.ipynb` | EOD |
| **All** | All 5 AUC scores in experiments.csv by end of day | `experiments.csv` | EOD |

---

### Day 7 — April 18 — Compile baselines + begin tuning

| Member | Task | Notebook / File |
|---|---|---|
| **Saloni** | Compile all 5 baseline AUC scores, update report | `reports/project_status.md` |
| **Shiv** | LGBM hyperparameter tuning — Optuna, 50 trials | `notebooks/05_hyperparameter_tuning.ipynb` |
| **Parul** | RF hyperparameter tuning — Optuna | `notebooks/05_hyperparameter_tuning.ipynb` |
| **Madhu** | MLP tuning — keras_tuner Hyperband | `notebooks/05_hyperparameter_tuning.ipynb` |
| **Bhavisha** | LogReg tuning — regularisation sweep | `notebooks/05_hyperparameter_tuning.ipynb` |

---

### Day 8 — April 19 — XGB tuning + review

| Member | Task |
|---|---|
| **Saloni** | XGB Bayesian tuning via Optuna |
| **Shiv** | Review LGBM results, test `n_estimators` vs `learning_rate` trade-off |
| **Parul** | Test `XGBRFClassifier` as extra tree alternative |
| **Madhu** | keras_tuner Hyperband — second round |
| **Bhavisha** | Collect all OOF arrays — save to `outputs/oof/` |

---

### Day 9 — April 20 — Multi-seed finalisation

| Member | Task |
|---|---|
| **Saloni** | Finalise XGBoost — 5 seeds, average OOF |
| **Shiv** | Finalise LightGBM — 5 seeds |
| **Parul** | Finalise Random Forest — 5 seeds |
| **Madhu** | Finalise MLP — 5 seeds |
| **Bhavisha** | Finalise LogReg — 5 seeds; run OOF correlation check in `07_model_correlation_check.ipynb` |

---

### Day 10–11 — April 21–22 — Ensemble

| Member | Task |
|---|---|
| **Saloni** | Weighted blend ensemble in `06_ensemble_submission.ipynb` |
| **Shiv** | Rank-average blend |
| **Parul** | Stack Layer 1 — LogReg meta-learner |
| **Madhu** | Stack Layer 2 — XGB meta-learner; SMOTE vs no-SMOTE ablation |
| **Bhavisha** | Post-processing rules (`apply_post_processing()`) |
| **All** | Compare public LB vs CV AUC, compile experiment summary |

---

### Day 12–13 — April 23–24 — Final models + docs

| Member | Task |
|---|---|
| **Saloni** | Final XGBoost — full train + 10 seeds; build 3 submission files |
| **Shiv** | Final LightGBM — full train + 10 seeds; write README updates |
| **Parul** | Final RF — full train + 10 seeds; write feature engineering docs |
| **Madhu** | Final MLP — full train + 5 seeds; write model documentation |
| **Bhavisha** | Final LogReg + stacking; write validation strategy doc |

---

### Day 14 — April 25 — Submit

| Member | Task |
|---|---|
| **Saloni** | Submit to Kaggle, select final 2 submissions |
| **Shiv** | Presentation slides |
| **Parul** | Finalise notebooks |
| **Madhu** | Finalise notebooks |
| **Bhavisha** | Repo cleanup |

---

## Data pipeline status (as of April 15)

```
Raw CSV (data/raw/train.csv)
  └─ 369 features, 76,020 rows

Step 1 — Concat train + test (151,838 rows combined)
  └─ Required to prevent column mismatch

Step 2 — Drop constant columns (34)
  └─ 335 features  ✅ confirmed number

Step 3 — Drop duplicate columns (27)
  └─ 308 features  ✅ confirmed, full name list in Parul's notebook

Step 4 — Drop sparse columns (>99% zeros)
  └─ ~125 features (approx — exact number depends on combined vs train-only)
  └─ ⚠️  02_cleaning.ipynb currently shows wrong number due to bug

Step 5 — Drop highly correlated columns (>0.98)
  └─ ~86 features (approx)
  └─ ⚠️  Must be computed on TRAIN portion only (not test)

Step 6 — Sentinel imputation
  └─ Same count + 3 flags: var3_missing, var36_99_flag, var38_was_mode
  └─ ✅ impute_sentinels() implemented by Madhu

Step 7 — Feature engineering
  └─ + log transforms: +121 columns  ✅ add_log_transforms() done (Madhu)
  └─ + rule flags: +4 columns  ❌ add_rule_flags() stub (Parul)
  └─ + row statistics: +8 columns  ❌ add_row_statistics() stub (Shiv)
  └─ + temporal deltas: +12 columns  ❌ add_temporal_deltas() stub (Bhavisha)

Step 8 — Feature selection (top 250 trees, top 50 linear)
  └─ ??? (depends on steps above being complete)

master_train.pkl / master_test.pkl / y_train.pkl
  └─ ❌ NOT SAVED — GATE for Day 6 baseline models
```

---

## Known pipeline bugs to fix

| Bug | Where | Impact | Fix |
|---|---|---|---|
| `02_cleaning.ipynb` loaded pre-cleaned 116-col data | Cell 02 | Constant + duplicate drops show 0 — invalid | Re-run from raw `train.csv` — Parul today |
| Summary cell prints "Features BEFORE: 116" | Cell 20 | Misleading | Fix `cols_before` to capture pre-cleaning shape |
| `Top100_Features_correlation.ipynb` at repo root | Root dir | Messy — missed by `ls notebooks/` | Move to `notebooks/` |
| `03_feature_engineering.ipynb` reads `parul_day4_train.csv` | Cell 02 | Local hardcoded path — breaks on other machines | Change to load from `data/processed/clean_train.csv` |

---

## src/ files status today

| File | Functions implemented | Functions still stub |
|---|---|---|
| `config.py` | All constants and paths ✅ | — |
| `utils.py` | `get_skf()`, `auc()` | `run_cv()`, `run_cv_multiseed()`, `log_experiment()`, `save_feature_importance()` |
| `features.py` | `impute_sentinels()` ✅, `add_log_transforms()` ✅ | `drop_constant_cols`, `drop_duplicate_cols`, `drop_delta_cols`, `drop_high_correlation_cols`, `add_row_statistics`, `add_rule_flags`, `add_temporal_deltas`, `apply_post_processing`, `run_full_cleaning_pipeline`, `run_full_feature_pipeline` |
| `models.py` | None | `get_logreg_baseline`, `get_rf_baseline`, `get_xgb_baseline`, `get_lgbm_baseline`, `get_mlp_baseline` |

---

## EDA status — `01_eda.ipynb` (merged April 15)

| Layer | Content | Owner | Status |
|---|---|---|---|
| Layer 1 | Shape, dtypes, nulls, class balance, column match | Saloni | ✅ Complete with outputs |
| Layer 2 | Prefix anatomy, time suffixes, standalone vars, delta cols | Saloni | ✅ Complete with outputs |
| Layer 3 — Sparsity | 283 features >95% zeros | Saloni | ✅ Complete with outputs |
| Layer 3 — var15 | Age range, rule confirmed, KDE by TARGET | Saloni + Parul | ✅ Complete with outputs |
| Layer 3 — var38 | Sentinel analysis, distribution plot note | Saloni + Madhu | ⚠️ Note cell added — plot cell needs running once locally |
| Layer 3 — var3 | -999999 sentinel check | Saloni | ✅ Complete with outputs |
| Layer 4 | Top 30 correlation with TARGET, ranked bar chart | **Shiv — NOT DONE** | ❌ Missing |
| Layer 5 | Multivariate heatmap | **Shiv — NOT DONE** | ❌ Missing |
| Summary | Key findings printout | Saloni | ✅ Complete |

---

*Report updated — April 15, 2026 | Verified against actual notebook outputs and git log*
