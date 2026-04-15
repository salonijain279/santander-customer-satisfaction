# Project Status Report — Santander Customer Satisfaction
**Date:** April 14, 2026
**Sprint day:** 3–4 of 14
**Status:** In Progress — alignment needed

---

## Summary

The team has made solid analytical progress during Days 1–4, with Saloni delivering complete repo infrastructure and a thorough 3-layer EDA (shape, feature anatomy, sentinel/sparsity analysis), and Bhavisha completing an independent end-to-end pass through cleaning and feature selection in a single notebook. However, the team is currently working in parallel silos rather than as an integrated pipeline: Parul's cleaning and feature engineering work exists only locally and has not been pushed; Shiv and Madhu have not yet committed any work; and Bhavisha's notebook mixes EDA, cleaning, and feature selection in a way that is inconsistent with the agreed notebook structure. The single most critical blocker is that **no canonical master_train.pkl / master_test.pkl has been saved**, which means nobody can begin baseline modelling (Day 6) until the cleaning and feature pipeline is reconciled, agreed upon, and committed by Day 5.

---

## Accomplishments by member

### Saloni

| Task | Status | Location |
|---|---|---|
| Repo structure, .gitignore, requirements.txt | ✅ Done | Root of repo |
| All documentation (README, TEAM_WORKFLOW, data_dictionary, business_translation) | ✅ Done | Root of repo / reports/ |
| `src/config.py` — all constants, paths, CV settings, sentinel values | ✅ Done | `src/config.py` |
| `src/utils.py` — function stubs with full docstrings and rules | ✅ Done | `src/utils.py` |
| EDA Layer 1: shape (76020×369), zero nulls, all numeric | ✅ Done | `notebooks/01_eda.ipynb` |
| EDA Layer 2: feature prefix anatomy (ind, num, saldo, imp, delta counts) | ✅ Done | `notebooks/01_eda.ipynb` |
| EDA Layer 3: sparsity map, var15 rule, var38 / var3 / var36 sentinel analysis | ✅ Done | `notebooks/01_eda.ipynb` |
| EDA Layer 4 (correlation + top 50) | ❌ Not done | — |
| EDA Layer 5 (scatter + heatmap) | ❌ Not done | — |

### Bhavisha

| Task | Status | Location |
|---|---|---|
| Drop 34 constant columns (369 → 335) | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| KDE train vs test distribution plots for top 30 features | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| Drop 186 sparse columns (>99% zeros) | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| Drop 38 highly correlated column pairs | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| Sentinel imputation (var3, var36, var38) + binary flags | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| `is_young` flag (var15 < 23) | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| Top 100 feature selection by correlation with TARGET | ✅ Done | `Top100_Features_correlation.ipynb` (Kaggle) |
| Migrate work into correct notebooks (02, 03) and push | ❌ Not done | — |
| `run_cv()` implementation in `src/utils.py` | ❌ Not done | `src/utils.py` (stub) |
| `run_cv_multiseed()` implementation | ❌ Not done | `src/utils.py` (stub) |
| `log_experiment()` implementation | ❌ Not done | `src/utils.py` (stub) |
| Temporal delta features (ult1 − ult3 pairs) | ❌ Not done | — |
| `drop_high_correlation_cols()` in `src/features.py` | ❌ Not done | `src/features.py` (stub) |

### Parul

| Task | Status | Location |
|---|---|---|
| var15 deep dive — age range 5–105, zero unsatisfied under 23 confirmed | ✅ Done (local) | Local only — not pushed |
| Concat train+test, drop 34 constant + 27 duplicate cols (369 → 308) | ✅ Done (local) | Local only — not pushed |
| Rule flags with AUC lift testing (is_elderly, saldo_zero, var38_is_mode, saldo5_ult3_zero) | ✅ Done (local) | Local only — not pushed |
| Push all local work to repo | ❌ Not done | — |
| Implement functions in `src/features.py` (drop_constant, drop_duplicate, impute_sentinels, add_rule_flags) | ❌ Not done | `src/features.py` (all stubs) |
| `run_full_cleaning_pipeline()` wired together | ❌ Not done | `src/features.py` (stub) |
| `notebooks/02_cleaning.ipynb` — populated with working cleaning pipeline | ❌ Not done | `notebooks/02_cleaning.ipynb` (empty shell) |

### Shiv

| Task | Status | Location |
|---|---|---|
| EDA Layer 3 — sparsity (assigned) | ❌ Not done / not pushed | — |
| EDA Layer 4 — correlation with TARGET, mutual information | ❌ Not done | — |
| EDA Layer 5 — multivariate scatter + heatmap | ❌ Not done | — |
| Row statistics features (count_zeros, count_ones, row_sum, row_mean, row_std, row_max, num_nonzero) | ❌ Not done | `src/features.py` (stub) |
| `get_lgbm_baseline()` in `src/models.py` | ❌ Not done | `src/models.py` (stub) |

### Madhu

| Task | Status | Location |
|---|---|---|
| var38 deep dive (assigned) | ❌ Not done / not pushed | — |
| Log transforms on all `saldo_*` and `imp_*` columns + var38 | ❌ Not done | `src/features.py` (stub) |
| `get_mlp_baseline()` in `src/models.py` | ❌ Not done | `src/models.py` (stub) |

---

## What is complete ✅

- **Dataset shape confirmed**: 76,020 rows × 369 features, zero nulls, all columns numeric
- **Class imbalance quantified**: 96.04% satisfied, 3.96% unsatisfied — AUC-ROC is the only valid metric
- **Feature prefix anatomy**: 75 `ind_`, 143 `num_`, 71 `saldo_`, 49 `imp_`, 26 `delta_`
- **Temporal suffix anatomy**: 80 `_ult1`, 40 `_ult3`, 15 `_hace2`, 41 `_hace3`, 46 `_medio` — ult1/ult3 pairs identified for delta features
- **Sparsity mapped**: 283 features have >95% zeros; 333 have >80% zeros
- **Constant columns drop**: exactly 34 constant columns confirmed and dropped (369 → 335)
- **Sparse columns drop**: 186 columns with >99% zeros dropped by Bhavisha
- **High-correlation drop**: 38 column pairs dropped by Bhavisha
- **Sentinel values identified and documented in config.py**:
  - `var3 = -999999`: 116 rows → replace with mode, add `var3_missing` flag
  - `var36 = 99`: 30,064 rows (39.5%) → add `var36_is_99` flag
  - `var38 = 117310.979016494`: 14,868 rows (19.6%) → replace with median, add `var38_was_mode` flag
- **var15 rule confirmed**: age range 5–105; **zero unsatisfied customers under age 23** (1,212 customers affected)
- **Sentinel imputation applied** by Bhavisha + `is_young` flag created
- **KDE train vs test plots** for top 30 features — distributions look aligned
- **Top 100 features selected** by Bhavisha via correlation with TARGET (shape: 76,020 × 100)
- **Parul's rule flags with AUC lift** (local): `saldo_zero` AUC 0.66, `saldo5_ult3_zero` AUC 0.66 (strong); `is_elderly` AUC 0.50, `var38_is_mode` AUC 0.50 (weak)
- **`src/config.py`** fully implemented with all constants, paths, CV settings
- **`src/utils.py`** — stubs with complete docstrings, rules documented, `get_skf()` and `auc()` implemented
- **`experiments.csv`** — header row created, schema in place
- **All 7 notebooks created** in correct phase order with import shells

---

## What is missing ❌

- **master_train.pkl / master_test.pkl / y_train.pkl not saved** — blocks all modelling (Owner: whole team; Due: Day 5)
- **Parul's cleaning + feature work not pushed** — 2 days of work invisible to team (Owner: Parul; Due: was Day 3)
- **Shiv: no commits at all** — row statistics (count_zeros, count_ones, row_sum, row_mean, row_std, row_max, num_nonzero) not done (Owner: Shiv; Due: Day 4)
- **Madhu: no commits at all** — log transforms on `saldo_*` and `imp_*` columns not done (Owner: Madhu; Due: Day 4)
- **Bhavisha: temporal delta features** (ult1 − ult3 / ratio pairs for 6 feature pairs) not done (Owner: Bhavisha; Due: Day 4)
- **Bhavisha: `run_cv()`, `run_cv_multiseed()`, `log_experiment()`, `save_feature_importance()`** all stubs — CV harness not built (Owner: Bhavisha; Due: Day 5)
- **All `src/features.py` functions are stubs** — nothing implemented (Owners: Parul, Shiv, Madhu, Bhavisha; Due: Day 5)
- **All `src/models.py` functions are stubs** — no model configurations exist (Owners: all; Due: Day 6)
- **`notebooks/02_cleaning.ipynb`** — empty shell, no executed cells
- **`notebooks/03_feature_engineering.ipynb`** — empty shell, no executed cells
- **Feature selection method inconsistent** — Bhavisha used correlation only; plan requires RF + XGB + MI combined (Owner: Saloni to decide; Due: Day 5)
- **Duplicate column count unresolved** — Parul found 27, Bhavisha found 0 after constant drop (needs reconciliation before pipeline is locked)

---

## Critical issues to resolve before Day 5

1. **Parul must push her local work immediately.** Two days of cleaning and feature engineering exist only on her machine. If anything happens to that machine, the work is lost. Push tonight.

2. **Reconcile the duplicate column discrepancy.** Parul dropped 27 duplicate columns (369 → 308 after constant drop); Bhavisha found 0 after constant drop. These numbers cannot both be correct. The team must sit together and agree on the exact column list before saving any `.pkl` files.

3. **Agree on a single canonical cleaning pipeline and lock it.** Currently Bhavisha ran cleaning inside a Kaggle notebook (not in `notebooks/02_cleaning.ipynb`) and Parul ran it locally. There must be exactly one version. Decision: wire Parul's logic into `src/features.py`, run through `notebooks/02_cleaning.ipynb`, and save the output.

4. **Save `master_train.pkl`, `master_test.pkl`, and `y_train.pkl` before Day 5 ends.** Without these files, every team member is blocked from starting baseline models on Day 6. This is the single hardest deadline between now and submission.

5. **Bhavisha must implement `run_cv()` and `log_experiment()` in `src/utils.py` before Day 6.** Every baseline model depends on `run_cv()`. `log_experiment()` must be called after every model run. Without these, baselines cannot be logged consistently and experiment tracking is broken.

6. **Decide the final feature selection method.** The project plan specifies RF + XGB + MI combined importance. Bhavisha used correlation only. Saloni must decide whether to keep the correlation-only top-100 or implement the combined method — this changes what goes into `master_train.pkl`.

7. **Shiv and Madhu must commit work today.** Both members have zero commits. Row statistics and log transforms are required inputs to the final feature matrix. If they are not delivered by Day 5, master_train.pkl cannot be built correctly.

---

## Revised action plan — next 48 hours

| Member | Task | Due | Priority |
|---|---|---|---|
| Parul | `git push` all local work immediately | Tonight | 🔴 CRITICAL |
| Parul | Implement `drop_constant_cols()`, `drop_duplicate_cols()`, `impute_sentinels()`, `add_rule_flags()` in `src/features.py` | Day 5 AM | 🔴 CRITICAL |
| Parul | Populate `notebooks/02_cleaning.ipynb` with working pipeline, execute all cells | Day 5 AM | 🔴 CRITICAL |
| Bhavisha | Reconcile duplicate column count with Parul (27 vs 0) | Tonight | 🔴 CRITICAL |
| Bhavisha | Implement `run_cv()`, `run_cv_multiseed()`, `log_experiment()` in `src/utils.py` | Day 5 | 🔴 CRITICAL |
| Bhavisha | Add temporal delta features (`add_temporal_deltas()`) in `src/features.py` | Day 5 | 🟠 HIGH |
| Shiv | Implement `add_row_statistics()` in `src/features.py` | Day 5 AM | 🔴 CRITICAL |
| Shiv | Commit and push | Day 5 AM | 🔴 CRITICAL |
| Madhu | Implement `add_log_transforms()` in `src/features.py` | Day 5 AM | 🔴 CRITICAL |
| Madhu | Commit and push | Day 5 AM | 🔴 CRITICAL |
| Saloni | Decide feature selection method: correlation-only vs RF+XGB+MI combined | Day 5 AM | 🟠 HIGH |
| Saloni | Wire `run_full_cleaning_pipeline()` + `run_full_feature_pipeline()`, save `master_train.pkl`, `master_test.pkl`, `y_train.pkl` | Day 5 PM | 🔴 CRITICAL |
| All | Confirm `master_train.pkl` shape and column list in group chat before Day 6 | Day 5 EOD | 🔴 CRITICAL |

---

## Data pipeline status

```
Raw CSV
  └─ 369 features, 76,020 rows

After constant drop (34 removed)
  └─ 335 features  ✅ confirmed (Bhavisha)

After duplicate drop
  └─ ??? features  ⚠️  DISPUTED — Parul: 308 (27 dups removed), Bhavisha: 335 (0 dups found)

After delta column drop (26 columns)
  └─ ??? features  (documented in config.py, not yet run in pipeline)

After sparse drop (>99% zeros — 186 removed by Bhavisha)
  └─ ??? features  (Bhavisha's number was from pre-duplicate-drop; needs recount)

After sentinel imputation
  └─ ??? features + 3 new flag columns (var3_missing, var36_is_99, var38_was_mode)

After high-correlation drop (38 pairs removed by Bhavisha)
  └─ ??? features

After feature engineering (row stats + rule flags + log transforms + temporal deltas)
  └─ ??? features  (none implemented in src/features.py yet)

After feature selection (top 100 by correlation — Bhavisha)
  └─ 100 features  ⚠️  method may change per Day 5 decision

master_train.pkl / master_test.pkl / y_train.pkl
  └─ ❌ NOT SAVED YET
```

---

## Key numbers confirmed from EDA

| Feature | Finding | Action |
|---|---|---|
| Dataset shape | 76,020 rows × 369 features | Baseline for all pipeline tracking |
| Null values | 0 nulls across all columns | No standard imputation needed |
| Class balance | 96.04% satisfied / 3.96% unsatisfied | Use AUC-ROC only; apply class weights to all models |
| Constant columns | 34 columns with a single unique value | Drop before any modelling |
| Delta columns (`delta_*`) | 26 columns; max value = 1e10 (sentinel for missing) | Drop all 26 |
| Sparsity (>95% zeros) | 283 features | Drop most; keep a few high-signal exceptions |
| Sparsity (>99% zeros) | 186 features | Drop — Bhavisha confirmed |
| `var15` (age) | Range 5–105; 1,212 customers under 23 | `is_young` flag; post-processing zero rule |
| `var15` rule | 0 unsatisfied customers under age 23 in full training set | Hard zero in post-processing |
| `var3` sentinel | -999999 in 116 rows | Replace with mode (2); add `var3_missing` flag |
| `var36` sentinel | 99 in 30,064 rows (39.5% of data) | Add `var36_is_99` flag; keep original column |
| `var38` sentinel | 117310.979016494 in 14,868 rows (19.6%) | Replace with median; add `var38_was_mode` flag |
| `var38` dissatisfaction rate (sentinel rows) | 4.1% vs 3.9% in non-sentinel rows | Sentinel rows slightly more likely to be unsatisfied |
| `saldo_zero` flag | Single-feature AUC = 0.66 | Include as rule flag and model feature |
| `saldo5_ult3_zero` flag | Single-feature AUC = 0.66 | Include as rule flag and model feature |
| `is_elderly` flag (var15 > 80) | Single-feature AUC = 0.50 | Weak — include anyway, low cost |
| `var38_is_mode` flag | Single-feature AUC = 0.50 | Weak but free — include as flag |
| Correlated pairs | 38 pairs with correlation ≥ 0.98 | Drop one from each pair |
| Temporal pairs | 80 `_ult1` + 40 `_ult3` features → 6 pairable bases | Create `_delta` and `_ratio` features |
| `ind_` prefix | 75 features | Likely binary indicators |
| `num_` prefix | 143 features | Counts and quantities |
| `saldo_` prefix | 71 features | Balance amounts — apply log1p |
| `imp_` prefix | 49 features | Transaction amounts — apply log1p |

---

## Rules confirmed for post-processing

These deterministic rules will be applied **only** to the final ensemble predictions, just before submission. They must **never** be applied inside CV folds.

1. **var15 < 23 → prediction = 0.0**
   Zero unsatisfied customers under age 23 in the entire 76,020-row training set. Certainty rule.

2. **saldo_var30 > 500,000 → prediction = 0.0**
   Documented in `config.py` as `SALDO_VAR30_CUTOFF`. High-balance customers confirmed satisfied.

3. Both rules are encoded in `apply_post_processing()` stub in `src/features.py` (Bhavisha to implement Day 10).

---

## Notebooks currently in repo

| Notebook | Owner | What is inside | Status |
|---|---|---|---|
| `01_eda.ipynb` | Saloni (lead) | Full 3-layer EDA: shape, dtypes, class balance, feature prefix anatomy, temporal suffix groups, standalone var analysis (var3, var15, var36, var38), sparsity map, sentinel detection, key findings summary | ✅ Complete and executed — all cell outputs present |
| `02_cleaning.ipynb` | Parul + Bhavisha | Import shell only — `from src.features import run_full_cleaning_pipeline` | ❌ Empty — no cleaning code in repo |
| `03_feature_engineering.ipynb` | Parul (lead) | Import shell only — `from src.features import run_full_feature_pipeline` | ❌ Empty — no feature engineering code in repo |
| `04_baseline_models.ipynb` | All (one model each) | Import shell only — references `run_cv`, `log_experiment` | ❌ Empty — awaiting CV harness and master pkl |
| `05_hyperparameter_tuning.ipynb` | All | Import shell only — references `optuna`, `run_cv`, `run_cv_multiseed` | ❌ Empty — awaiting Day 7 |
| `06_ensemble_submission.ipynb` | Saloni + Bhavisha | Import shell only — references `log_experiment`, `apply_post_processing` | ❌ Empty — awaiting Day 12 |
| `07_model_correlation_check.ipynb` | Bhavisha | Import shell only — OOF correlation heatmap | ❌ Empty — awaiting Day 9 |

**Note:** Bhavisha's actual cleaning + feature selection work is in a separate Kaggle notebook (`Top100_Features_correlation.ipynb`) that exists outside this repo structure. It must be migrated into `02_cleaning.ipynb` and `03_feature_engineering.ipynb`.

---

## src/ files status

| File | Owner | What is implemented | What is still a stub |
|---|---|---|---|
| `src/config.py` | Saloni | All paths (`RAW_DATA_PATH`, `PROCESSED_PATH`, `OOF_PATH`, etc.), CV constants (`CV_N_SPLITS=5`, `CV_RANDOM_STATE=42`, `SEEDS=[42,7,13,99,21]`), column names, all sentinel values, post-processing thresholds, feature selection sizes | Nothing — fully implemented ✅ |
| `src/utils.py` | Bhavisha | `get_skf()` — returns standard StratifiedKFold; `auc()` — wraps roc_auc_score; complete docstrings and critical rules for all functions | `run_cv()`, `run_cv_multiseed()`, `log_experiment()`, `save_feature_importance()` — all `pass` |
| `src/features.py` | Parul (lead) | Full docstrings with rules, expected shapes, and reason comments for all functions | `drop_constant_cols()`, `drop_duplicate_cols()`, `drop_delta_cols()`, `impute_sentinels()`, `drop_high_correlation_cols()`, `add_row_statistics()`, `add_rule_flags()`, `add_log_transforms()`, `add_temporal_deltas()`, `apply_post_processing()`, `run_full_cleaning_pipeline()`, `run_full_feature_pipeline()` — all `pass` |
| `src/models.py` | Saloni (structure) | Full docstrings with imbalance handling strategy per model | `get_logreg_baseline()`, `get_rf_baseline()`, `get_xgb_baseline()`, `get_lgbm_baseline()`, `get_mlp_baseline()` — all `pass` |
| `src/__init__.py` | Saloni | Empty (package marker) | N/A |

---

*Report generated by automated repo inspection — April 14, 2026*
