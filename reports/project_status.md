# Project Status Report — Santander Customer Satisfaction
**Date:** April 15, 2026
**Sprint day:** 3–4 of 14 (updated)
**Status:** In Progress — good progress, alignment still needed

---

## Summary

Significant progress has been made since the initial Day 3–4 snapshot. Parul has now pushed her full exploratory, cleaning, and feature engineering work (`Parul_Day2&3&4_Exploratory.ipynb`). Madhu has pushed three commits implementing `impute_sentinels()` and `add_log_transforms()` in `src/features.py` (121 log columns, zero inf/NaN), plus a var38 deep dive. A full cleaning pipeline now exists in `notebooks/02_cleaning.ipynb` with executed outputs (train shape: 76020×116, test: 75818×116), and `notebooks/03_feature_engineering.ipynb` is partially populated. However, critical structural problems remain: the cleaning pipeline in `02_cleaning.ipynb` has a **bug in its summary cell** (shows "Features BEFORE cleaning: 116" — a copy-paste error), `notebooks/03_feature_engineering.ipynb` has **no executed outputs**, Shiv still has zero commits, `src/features.py` still has 7 stubs, and `master_train.pkl` / `master_test.pkl` / `y_train.pkl` have not been saved. The pipeline is not yet usable end-to-end.

---

## Accomplishments by member

### Saloni

| Task | Status | Location |
|---|---|---|
| Repo structure, .gitignore, requirements.txt | ✅ Done | Root of repo |
| All documentation (README, TEAM_WORKFLOW, data_dictionary, business_translation) | ✅ Done | Root of repo |
| `src/config.py` — all constants, paths, CV settings, sentinel values | ✅ Done | `src/config.py` |
| `src/utils.py` — stubs + `get_skf()` + `auc()` implemented | ✅ Done | `src/utils.py` |
| EDA Layer 1: shape (76020×369), zero nulls, all numeric | ✅ Done | `notebooks/01_eda.ipynb` |
| EDA Layer 2: prefix anatomy (ind, num, saldo, imp, delta) | ✅ Done | `notebooks/01_eda.ipynb` |
| EDA Layer 3: sparsity, var15 rule, sentinels | ✅ Done | `notebooks/01_eda.ipynb` |
| EDA Layer 4 (correlation + top 50) | ❌ Not done | — |
| EDA Layer 5 (scatter + heatmap) | ❌ Not done | — |

### Bhavisha

| Task | Status | Location |
|---|---|---|
| Drop 34 constant columns (369 → 335) | ✅ Done | Kaggle notebook (not in repo structure) |
| KDE train vs test distribution plots for top 30 features | ✅ Done | `Top100_Features_correlation.ipynb` |
| Drop 186 sparse columns (>99% zeros) | ✅ Done | Kaggle notebook |
| Drop 38 highly correlated column pairs | ✅ Done | Kaggle notebook |
| Sentinel imputation (var3, var36, var38) + binary flags | ✅ Done | Kaggle notebook |
| `is_young` flag (var15 < 23) | ✅ Done | Kaggle notebook |
| Top 100 feature selection by correlation with TARGET | ✅ Done | Kaggle notebook |
| Migrate work into `02_cleaning.ipynb` and `03_feature_engineering.ipynb` | ⚠️ Partial | Parul picked up some of this in `02_cleaning.ipynb` |
| `run_cv()` implementation in `src/utils.py` | ❌ Not done | `src/utils.py` (stub) |
| `run_cv_multiseed()` implementation | ❌ Not done | `src/utils.py` (stub) |
| `log_experiment()` implementation | ❌ Not done | `src/utils.py` (stub) |
| Temporal delta features (`add_temporal_deltas()`) | ❌ Not done | `src/features.py` (stub) |
| `drop_high_correlation_cols()` in `src/features.py` | ❌ Not done | `src/features.py` (stub) |

### Parul

| Task | Status | Location |
|---|---|---|
| var15 deep dive — age range 5–105, zero unsatisfied under 23 | ✅ Done & pushed | `Parul_Day2&3&4_Exploratory.ipynb` |
| Concat train+test, drop 34 constant + 27 duplicate cols (369 → 308) | ✅ Done & pushed | `Parul_Day2&3&4_Exploratory.ipynb` Cell 11–14 |
| Sparse drop (163 cols), correlation drop (32 cols), reaching 111 features | ✅ Done & pushed | `Parul_Day2&3&4_Exploratory.ipynb` Cells 18–19 |
| Rule flags with AUC testing (is_elderly 0.50, saldo_zero 0.66, var38_is_mode 0.50, saldo5_ult3_zero 0.66) | ✅ Done & pushed | `Parul_Day2&3&4_Exploratory.ipynb` |
| Full cleaning pipeline in `02_cleaning.ipynb` with executed outputs | ✅ Done & pushed | `notebooks/02_cleaning.ipynb` — 76020×116 output confirmed |
| `notebooks/03_feature_engineering.ipynb` — structure and steps written | ⚠️ Partial — no executed outputs | `notebooks/03_feature_engineering.ipynb` |
| `drop_constant_cols()` in `src/features.py` | ❌ Not done | `src/features.py` (stub) |
| `drop_duplicate_cols()` in `src/features.py` | ❌ Not done | `src/features.py` (stub) |
| `add_rule_flags()` in `src/features.py` | ❌ Not done | `src/features.py` (stub) |
| `run_full_cleaning_pipeline()` wired together | ❌ Not done | `src/features.py` (stub) |

### Shiv

| Task | Status | Location |
|---|---|---|
| Any notebook or src work | ❌ Zero commits | — |
| Row statistics features (count_zeros, count_ones, row_sum, row_mean, etc.) | ❌ Not done | `src/features.py` (stub) |
| EDA Layer 4 + 5 | ❌ Not done | — |
| `get_lgbm_baseline()` in `src/models.py` | ❌ Not done | `src/models.py` (stub) |

### Madhu

| Task | Status | Location |
|---|---|---|
| Environment setup — TF 2.16.2 confirmed, CPU only (M-series Mac) | ✅ Done | Commit `8787f47` |
| var38 deep dive — 14,868 sentinel rows confirmed, more likely dissatisfied | ✅ Done | `outputs/var38_distribution.png`, commit `1c09130` |
| `impute_sentinels()` implemented and tested in `src/features.py` | ✅ Done | `src/features.py`, commit `50ed574` |
| `add_log_transforms()` implemented — 121 log columns, inf/NaN verified | ✅ Done | `src/features.py`, commit `8eb8a62` |
| `notebooks/madhu_eda` file | ⚠️ Empty file — 0 bytes | `notebooks/madhu_eda` |
| `get_mlp_baseline()` in `src/models.py` | ❌ Not done | `src/models.py` (stub) |

---

## What is complete ✅

- **Dataset confirmed**: 76,020 rows × 369 features, zero nulls, all numeric
- **Class imbalance**: 96.04% satisfied / 3.96% unsatisfied — AUC-ROC only
- **Feature anatomy**: 75 `ind_`, 143 `num_`, 71 `saldo_`, 49 `imp_`, 26 `delta_`; 80 `_ult1`, 40 `_ult3`, 6 pairable base features
- **Constant drop**: 34 columns confirmed (369 → 335)
- **Duplicate drop**: 27 columns confirmed by Parul with full name list: `ind_var13_medio`, `ind_var18`, `ind_var26`, `ind_var25`, + 23 others (369 → 308 on combined train+test)
- **Sparse drop**: 163–186 columns (varies by pipeline version — see discrepancies section)
- **Sentinel values confirmed and coded in `config.py`**:
  - `var3 = -999999`: 116 rows (train-only) / 236 rows (combined)
  - `var36 = 99`: 30,064 rows (train) / 60,159 rows (combined)
  - `var38 = 117310.979016494`: 14,868 rows (train) / 29,673 rows (combined)
- **`impute_sentinels()` implemented** (Madhu) — replaces sentinels, adds 3 flag columns, zero nulls verified ✅
- **`add_log_transforms()` implemented** (Madhu) — 121 log columns (`saldo_*`, `imp_*`, `var38`), zero inf/NaN ✅
- **var15 rule confirmed**: 1,212 customers under age 23, zero unsatisfied — post-processing rule locked
- **Rule flags with AUC lift**:
  - `saldo_zero`: AUC 0.6649 ✅ strong — 19,244 customers flagged
  - `saldo5_ult3_zero`: AUC 0.6650 ✅ strong — 24,664 customers flagged
  - `is_elderly`: AUC 0.4986 ❌ weak — 558 customers flagged
  - `var38_is_mode`: AUC 0.5044 ❌ weak — 14,868 customers flagged
- **`02_cleaning.ipynb`** fully executed: train 76020×116, test 75818×116, `clean_train.csv` and `clean_test.csv` saved
- **`get_skf()` and `auc()` implemented** in `src/utils.py`
- **`experiments.csv`** schema in place (header row only, no runs yet)
- **All 7 notebooks created** in phase order

---

## What is missing ❌

- **`master_train.pkl` / `master_test.pkl` / `y_train.pkl` not saved** — blocks all modelling (Owner: whole team; Due: Day 5)
- **`notebooks/madhu_eda` is an empty 0-byte file** — should contain Madhu's EDA notebook or be deleted (Owner: Madhu)
- **`notebooks/03_feature_engineering.ipynb` has no executed outputs** — cells written but not run (Owner: Parul; Due: Day 4)
- **Shiv: zero commits** — row statistics (`count_zeros`, `count_ones`, `row_sum`, `row_mean`, `row_std`, `row_max`, `num_nonzero`) not done (Owner: Shiv; Due: Day 4 — overdue)
- **Bhavisha: `run_cv()`, `run_cv_multiseed()`, `log_experiment()`, `save_feature_importance()`** — all stubs, CV harness not built (Owner: Bhavisha; Due: Day 5)
- **Bhavisha: temporal delta features** (`add_temporal_deltas()`) not implemented (Owner: Bhavisha; Due: Day 4 — overdue)
- **`drop_constant_cols()`, `drop_duplicate_cols()`, `add_rule_flags()` in `src/features.py`** still stubs (Owner: Parul; Due: Day 4–5)
- **`drop_high_correlation_cols()` in `src/features.py`** still a stub (Owner: Bhavisha)
- **`run_full_cleaning_pipeline()` and `run_full_feature_pipeline()`** not wired (Owner: Parul; Due: Day 5)
- **All 5 model stubs in `src/models.py`** — nothing implemented yet (All; Due: Day 6)
- **Feature selection method inconsistent** — pipeline uses correlation only; project plan requires RF + XGB + MI combined

---

## Critical issues to resolve before Day 5

1. **`notebooks/03_feature_engineering.ipynb` must be executed.** Cells are written but produce no outputs. Run all cells and commit with outputs visible.

2. **`notebooks/madhu_eda` is a 0-byte empty file** and should not be in the repo. Either delete it and push the removal, or replace it with Madhu's actual EDA notebook.

3. **Duplicate column count has two numbers in the repo.** Parul (combined approach) finds 27 duplicates — full name list confirmed. Bhavisha (train-only approach) found 0. The canonical pipeline must use one method. Decision needed: **use Parul's combined concat approach** (correct — prevents train/test shape mismatch), which drops 27 duplicates giving 308 features.

4. **The `02_cleaning.ipynb` summary cell has a bug.** It prints "Features BEFORE cleaning: 116" — this is the output of a previous step being fed in, not the raw 369. The summary is misleading. Fix the cell to start from `cols_before = 369`.

5. **Shiv must commit row statistics today.** `add_row_statistics()` is the most analytically important missing feature (count_zeros is likely the #1 engineered feature). Without it, `master_train.pkl` will be incomplete.

6. **Bhavisha must implement `run_cv()` and `log_experiment()` before Day 6.** Every baseline model depends on these. Day 6 is baseline modelling day — this is a hard dependency.

7. **Save `master_train.pkl`, `master_test.pkl`, `y_train.pkl` by end of Day 5.** Nothing in notebooks 04–07 can run without them.

---

## Revised action plan — next 48 hours

| Member | Task | Due | Priority |
|---|---|---|---|
| Madhu | Delete or replace 0-byte `notebooks/madhu_eda` file | Today | 🟠 HIGH |
| Madhu | Implement `get_mlp_baseline()` in `src/models.py` | Day 6 | 🟠 HIGH |
| Parul | Execute all cells in `notebooks/03_feature_engineering.ipynb` and push with outputs | Today | 🔴 CRITICAL |
| Parul | Implement `drop_constant_cols()`, `drop_duplicate_cols()`, `add_rule_flags()` in `src/features.py` | Day 5 | 🔴 CRITICAL |
| Parul | Fix summary cell bug in `02_cleaning.ipynb` (shows 116, should be 369) | Today | 🟠 HIGH |
| Parul | Wire `run_full_cleaning_pipeline()` in `src/features.py` | Day 5 | 🔴 CRITICAL |
| Shiv | Implement `add_row_statistics()` in `src/features.py` and push | Today | 🔴 CRITICAL |
| Shiv | Commit first notebook showing work done | Today | 🔴 CRITICAL |
| Bhavisha | Implement `run_cv()`, `run_cv_multiseed()`, `log_experiment()` in `src/utils.py` | Day 5 | 🔴 CRITICAL |
| Bhavisha | Implement `add_temporal_deltas()` in `src/features.py` | Day 5 | 🟠 HIGH |
| Bhavisha | Implement `drop_high_correlation_cols()` in `src/features.py` | Day 5 | 🟠 HIGH |
| Saloni | Confirm duplicate drop method (27 vs 0) and lock canonical pipeline | Today | 🔴 CRITICAL |
| Saloni | Run `run_full_cleaning_pipeline()` → save `master_train.pkl`, `master_test.pkl`, `y_train.pkl` | Day 5 EOD | 🔴 CRITICAL |
| All | Confirm master pkl shape in group chat before Day 6 | Day 5 EOD | 🔴 CRITICAL |

---

## Data pipeline status

```
Raw CSV
  └─ 369 features, 76,020 rows (train) / 75,818 rows (test)

After constant drop (34 removed)
  └─ 335 features  ✅ confirmed (Parul + Bhavisha agree)

After duplicate drop
  └─ 308 features  ✅ confirmed by Parul — 27 duplicates, full name list available
                   ⚠️  Bhavisha's Kaggle notebook found 0 (different method — train-only)
                   → Use Parul's combined concat approach as canonical

After sparse drop (>99% zeros)
  └─ 02_cleaning.ipynb: 152 features (183 sparse dropped from combined)
     Parul exploratory: 143 features (163 sparse dropped from train-only)
     ⚠️  Numbers differ — needs reconciliation when pipeline is unified

After correlation drop (corr > 0.98)
  └─ 02_cleaning.ipynb: 113 features (39 correlated dropped)
     Parul exploratory: 111 features (32 correlated dropped)
     ⚠️  Computed on train portion of combined — correct approach

After sentinel imputation
  └─ Same column count + 3 new flags (var3_missing, var36_99_flag, var38_flag) ✅ Madhu

After feature engineering (log transforms + rule flags + row stats + temporal deltas)
  └─ log transforms: +121 columns ✅ Madhu implemented
     rule flags: +4 columns (saldo_zero, etc.) ✅ Parul confirmed AUC
     row statistics: ??? ❌ Shiv not done
     temporal deltas: ??? ❌ Bhavisha not done

master_train.pkl / master_test.pkl / y_train.pkl
  └─ ❌ NOT SAVED YET — clean_train.csv exists on Parul's local machine only
```

---

## Key numbers confirmed from EDA

| Feature | Finding | Action |
|---|---|---|
| Dataset shape | 76,020 rows × 369 features | Baseline for pipeline tracking |
| Null values | 0 nulls | No standard imputation needed |
| Class balance | 96.04% / 3.96% | Use AUC-ROC; apply class weights everywhere |
| Constant columns | 34 | Drop |
| Duplicate columns | 27 (full name list confirmed by Parul) | Drop — use Parul's list as canonical |
| Sparse columns (>99% zeros) | 183 (combined) / 163 (train-only) | Drop |
| Correlated pairs (>0.98) | 39 (combined) / 32 (train-only) | Drop one from each pair |
| `var15` range | 5–105 | Normal — no outlier treatment |
| `var15` age-23 rule | 0 unsatisfied customers under 23 (1,212 affected) | Hard zero in post-processing |
| `var15` (satisfied median) | 27 years old | — |
| `var15` (unsatisfied median) | 38 years old | Dissatisfied customers are older |
| `var3` sentinel | -999999 in 116 rows (train) | Replace with mode=2, add `var3_missing` |
| `var36` sentinel | 99 in 30,064 rows (39.5% train) | Add `var36_is_99` flag |
| `var38` sentinel | 117310.979016494 in 14,868 rows (19.6%) | Replace with median, add `var38_was_mode` |
| `var38` (sentinel rows) | 4.1% dissatisfied vs 3.9% non-sentinel | Sentinel rows slightly more dissatisfied |
| `saldo_zero` flag | AUC 0.6649 — 19,244 customers | ✅ Include — strong signal |
| `saldo5_ult3_zero` flag | AUC 0.6650 — 24,664 customers | ✅ Include — strong signal |
| `is_elderly` flag | AUC 0.4986 — 558 customers | ⚠️ Weak — include anyway |
| `var38_is_mode` flag | AUC 0.5044 — 14,868 customers | ⚠️ Weak — include anyway |
| Log transform columns | 121 new columns (`log1p_saldo_*`, `log1p_imp_*`, `log1p_var38`) | ✅ Implemented and verified |
| `saldo_` columns after cleaning | 20 columns remain | All get log transforms |

---

## Rules confirmed for post-processing

Applied **only** to the final ensemble output, just before Kaggle submission. Never inside CV.

1. **`var15 < 23` → prediction = 0.0** — Zero unsatisfied customers under 23 in all 76,020 training rows. Certainty rule.
2. **`saldo_var30 > 500,000` → prediction = 0.0** — High-balance customers confirmed satisfied. Coded in `config.py` as `SALDO_VAR30_CUTOFF`.

Both implemented as stubs in `apply_post_processing()` in `src/features.py` (Bhavisha to implement Day 10).

---

## Notebooks currently in repo

| Notebook | Owner | What is inside | Status |
|---|---|---|---|
| `01_eda.ipynb` | Saloni | Full 3-layer EDA: shape, dtypes, class balance, prefix anatomy, temporal suffixes, var3/var15/var36/var38 deep dives, sparsity map, delta column analysis, key findings summary | ✅ Fully executed — all cell outputs present |
| `02_cleaning.ipynb` | Parul + Bhavisha | Full cleaning pipeline on concat train+test: constant drop (34), duplicate drop (27), sparse drop (183), correlation drop (39), sentinel imputation (3 flags), train/test split → 76020×116 / 75818×116. `clean_train.csv` saved locally. | ✅ Executed — outputs present. ⚠️ Summary cell bug (shows 116 not 369) |
| `03_feature_engineering.ipynb` | Parul | Rule flags (is_elderly, saldo_zero, var38_is_mode, saldo5_ult3_zero), one-hot encode var36, feature type documentation, AUC summary table, save output | ⚠️ Cells written, zero executed outputs — not run yet |
| `04_baseline_models.ipynb` | All | Import shell only | ❌ Empty — awaiting CV harness + master pkl |
| `05_hyperparameter_tuning.ipynb` | All | Import shell only | ❌ Empty — awaiting Day 7 |
| `06_ensemble_submission.ipynb` | Saloni + Bhavisha | Import shell only | ❌ Empty — awaiting Day 12 |
| `07_model_correlation_check.ipynb` | Bhavisha | Import shell only — OOF correlation heatmap | ❌ Empty — awaiting Day 9 |
| `Parul_Day2&3&4_Exploratory.ipynb` | Parul | Days 2–4 exploratory work: var15 deep dive, concat cleaning (369→308→143→111), rule flags with AUC testing (all executed), saved `parul_day4_train.csv` (76020×116) | ✅ Fully executed — all outputs present |
| `Top100_Features_correlation.ipynb` | Bhavisha | Kaggle notebook: constant drop, KDE plots, sparse drop, correlation drop, sentinel imputation, is_young flag, top 100 by correlation → 76020×100 | ✅ Executed on Kaggle — outputs present |
| `madhu_eda` | Madhu | **0-byte empty file** | ❌ Must be deleted or replaced |

---

## src/ files status

| File | Owner | What is implemented | What is still a stub |
|---|---|---|---|
| `src/config.py` | Saloni | Everything: all paths, CV constants (5-fold, seed=42, seeds=[42,7,13,99,21]), sentinel values, post-processing thresholds, feature sizes | Nothing — fully complete ✅ |
| `src/utils.py` | Bhavisha | `get_skf()` — standard StratifiedKFold; `auc()` — roc_auc_score wrapper; complete docstrings with rules | `run_cv()`, `run_cv_multiseed()`, `log_experiment()`, `save_feature_importance()` — all `pass` |
| `src/features.py` | Parul (lead) / Madhu / Bhavisha | `impute_sentinels()` ✅ Madhu — full implementation, var3/var36/var38 handled, 3 flags added, null check; `add_log_transforms()` ✅ Madhu — 121 log columns, clip(lower=0), inf/NaN verified | `drop_constant_cols()`, `drop_duplicate_cols()`, `drop_delta_cols()`, `drop_high_correlation_cols()`, `add_row_statistics()`, `add_rule_flags()`, `add_temporal_deltas()`, `apply_post_processing()`, `run_full_cleaning_pipeline()`, `run_full_feature_pipeline()` — all `pass` |
| `src/models.py` | Saloni (structure) | Full docstrings with imbalance handling strategy per model | `get_logreg_baseline()`, `get_rf_baseline()`, `get_xgb_baseline()`, `get_lgbm_baseline()`, `get_mlp_baseline()` — all `pass` |
| `src/__init__.py` | Saloni | Empty package marker | N/A |

---

*Report updated by automated repo inspection — April 15, 2026*
