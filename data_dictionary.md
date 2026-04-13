# Data Dictionary — Santander Customer Satisfaction

## Purpose

This document is the primary reference for all features in the Santander Customer Satisfaction dataset. All column names are anonymized. Decoded meanings are based on naming patterns and confirmed through exploratory data analysis.

---

## Dataset Summary

| Property | Value |
|---|---|
| Training rows | 76,020 |
| Test rows | 75,818 |
| Raw features | 369 anonymized numeric columns |
| Class distribution | 96.04% satisfied (0), 3.96% unsatisfied (1) |
| Class ratio | approximately 24:1 |
| Evaluation metric | AUC-ROC |
| Missing value encoding | sentinel integers/floats — not NaN |

---

## Column Prefix Reference

| Prefix | Spanish term | Meaning | Type |
|---|---|---|---|
| ind_ | Indicador | Binary flag — has product or status | 0 or 1 |
| num_ | Número | Count of transactions or products | Integer |
| saldo_ | Saldo | Account balance | Float |
| imp_ | Importe | Transaction amount | Float |
| delta_ | Delta | Year-over-year change — dropped | Float |
| var_ | Variable | Standalone feature | Mixed |

---

## Time Window Suffix Reference

| Suffix | Meaning |
|---|---|
| _ult1 | Last 1 month |
| _ult3 | Last 3 months |
| _hace2 | 2 months ago |
| _hace3 | 3 months ago |
| _medio | Average over period |

---

## Product Group Reference

| Code | Product group |
|---|---|
| var30 | Cash products — current accounts |
| var01 | Card products |
| var31 | Loan products |
| var13 | Short-term savings |
| var17 | Long-term savings |
| var44 | Investment products |
| var5 | Core banking — primary account |

---

## Key Decoded Features

| Column | Interpretation | EDA finding |
|---|---|---|
| var3 | Nationality or region code | Sentinel -999999 = unknown — 116 rows |
| var15 | Customer age | Range 5–105. Zero unsatisfied customers under 23 (1,212 confirmed) |
| var36 | Unknown categorical | Values 0,1,2,3,99. Value 99 in 30,064 rows (40% of data) |
| var38 | Mortgage or net worth estimate | Sentinel 117310.979 in 14,868 rows (20% of data) |
| saldo_var30 | Cash account balance | Second most important feature. Zero = strong dissatisfaction signal |
| saldo_medio_var5_ult3 | Average core balance last 3 months | 65% of unsatisfied customers = 0 |
| num_var4 | Number of products held | Low count correlates with dissatisfaction |
| num_var22_ult3 | Transaction count last 3 months | Low activity = disengaged customer |

---

## Sentinel Values — Treatment Applied

| Column | Sentinel | Rows | Treatment |
|---|---|---|---|
| var3 | -999999 | 116 | Replaced with mode. Flag var3_missing created. |
| var36 | 99 | 30,064 | Retained as valid category. Flag var36_is_99 created. |
| var38 | 117310.979016494 | 14,868 | Replaced with NaN then median. Flag var38_was_mode created. |
| All delta_ columns | 1e10 | Multiple | All 26 delta columns dropped. |

---

## Constant Columns Dropped (34 total)

All 34 columns below contain identical values for every customer and were removed during cleaning.

ind_var2_0, ind_var2, ind_var27_0, ind_var28_0, ind_var28, ind_var27, ind_var41, ind_var46_0, ind_var46, num_var27_0, num_var28_0, num_var28, num_var27, num_var41, num_var46_0, num_var46, saldo_var28, saldo_var27, saldo_var41, saldo_var46, imp_amort_var18_hace3, imp_amort_var34_hace3, imp_reemb_var13_hace3, imp_reemb_var33_hace3, imp_trasp_var17_out_hace3, imp_trasp_var33_out_hace3, num_var2_0_ult1, num_var2_ult1, num_reemb_var13_hace3, num_reemb_var33_hace3, num_trasp_var17_out_hace3, num_trasp_var33_out_hace3, saldo_var2_ult1, saldo_medio_var13_medio_hace3

---

## Engineered Features

| Feature | Calculation | Rationale |
|---|---|---|
| count_zeros | Zero-valued features per row | Primary engineered predictor. High count = low engagement = dissatisfaction |
| count_ones | Features equal to one per row | Sparsity signal across binary indicators |
| count_neg | Negative features per row | Negative balances = financial stress |
| num_nonzero | Non-zero features per row | Engagement proxy |
| row_sum | Sum across all features | Total activity level |
| row_mean | Mean across all features | Average activity |
| row_std | Std deviation across features | Spread of activity |
| row_max | Max feature value | Peak activity |
| is_young | 1 if var15 < 23 | No unsatisfied customer under 23 — deterministic rule |
| is_elderly | 1 if var15 > 80 | Elevated dissatisfaction rate |
| saldo_var30_zero | 1 if saldo_var30 = 0 | 50%+ unsatisfied customers have zero cash balance |
| saldo5_ult3_zero | 1 if saldo_medio_var5_ult3 = 0 | 65% unsatisfied customers have zero recent balance |
| var38_was_mode | 1 if var38 was sentinel | Missingness in mortgage data is predictive |
| var3_missing | 1 if var3 was -999999 | Unknown nationality signal |
| var36_is_99 | 1 if var36 = 99 | Dominant category flag |
| saldo_*_log | log1p of saldo columns | Corrects right skew in balance data |
| imp_*_log | log1p of imp columns | Corrects right skew in transaction amounts |
| var38_log | log1p of var38 | Corrects right skew in mortgage data |
| base_delta | ult1 minus ult3 | Trend direction — activity increasing or decreasing |
| base_ratio | ult1 divided by ult3 | Relative magnitude of change |

---

## Data Leakage Prevention

| Rule | Reason |
|---|---|
| TARGET saved separately as y_train.pkl | Prevents target from entering feature matrix |
| Cleaning on concat(train + test) | Identical treatment for both datasets |
| StandardScaler fit on fold train only | Fitting on full data leaks test statistics |
| SMOTE inside CV folds only | Pre-split oversampling inflates validation AUC |
| Target encoding inside CV folds only | Full-dataset encoding leaks TARGET into features |
| Post-processing after ensemble only | Business rules applied to predictions not training |
