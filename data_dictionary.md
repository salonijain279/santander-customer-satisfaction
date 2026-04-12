# Data dictionary — Santander Customer Satisfaction

## What is this file?
A data dictionary explains what every column means, what its
values represent, and what was done to it.
Since Santander anonymized all column names, we decoded them
using naming patterns and confirmed findings from EDA.
Think of it as the legend on a map — without it you are guessing.

## Dataset facts
| Property | Value |
|---|---|
| Train rows | 76,020 |
| Test rows | 75,818 |
| Raw features | 369 anonymized numeric columns |
| Class balance | 96.04% satisfied (0), 3.96% unsatisfied (1) |
| Ratio | approximately 24 satisfied for every 1 unsatisfied |
| Evaluation metric | AUC-ROC — accuracy is meaningless at this imbalance |
| Missing values | encoded as sentinel numbers, not NaN |

## Column prefix decoder (Spanish banking terminology)
| Prefix | Spanish word | Plain English meaning | Data type |
|---|---|---|---|
| ind_ | Indicador | Binary flag — yes or no for a product or status | 0 or 1 only |
| num_ | Numero | Count — how many transactions or products | Integer |
| saldo_ | Saldo | Balance — account balance in currency | Float |
| imp_ | Importe | Amount — transaction amount in currency | Float |
| delta_ | Delta | Change over time — DROPPED (contains 1e10 sentinel) | Float |
| var_ | Variable | Standalone features that don't fit other groups | Mixed |

## Time window suffix decoder
| Suffix | Plain English meaning |
|---|---|
| _ult1 | Data from the last 1 month |
| _ult3 | Data from the last 3 months |
| _hace2 | Data from 2 months ago |
| _hace3 | Data from 3 months ago |
| _medio | Average or mean value |

## Product group decoder
| Code in column name | Product group |
|---|---|
| var30 | Cash products — current accounts |
| var01 | Card products — credit and debit cards |
| var31 | Loan products — personal and mortgage loans |
| var13 | Short-term savings |
| var17 | Long-term savings |
| var44 | Investment products |
| var5 | Core banking — main account |

## Known decoded columns (confirmed via EDA and literature)
| Column | What it most likely represents | Key finding from EDA |
|---|---|---|
| var3 | Nationality or region code — 208 unique values | Sentinel -999999 = unknown nationality — 116 rows |
| var15 | Customer age | Range 5 to 105. Zero unsatisfied customers under age 23 — confirmed from data |
| var36 | Unknown categorical feature | Values are 0,1,2,3 and 99. Value 99 appears in 30,064 rows — 40% of data |
| var38 | Mortgage value or net worth estimate | Right-skewed distribution. Sentinel 117310.979 appears 14,868 times — 20% of data |
| saldo_var30 | Cash account balance | Second most important predictor. Zero balance = strong dissatisfaction signal |
| saldo_medio_var5_ult3 | Average core account balance last 3 months | 65% of unsatisfied customers have this equal to zero |
| num_var4 | Number of products held by customer | Low product count correlates with dissatisfaction |
| num_var22_ult3 | Number of transactions last 3 months | Activity proxy — low activity = disengaged customer |

## Sentinel values — handle before any modelling
| Column | Sentinel value | How many rows | Treatment applied |
|---|---|---|---|
| var3 | -999999 | 116 rows | Replaced with mode (2). Binary flag var3_missing created |
| var36 | 99 | 30,064 rows | Kept as its own category (too frequent to treat as missing). Binary flag var36_is_99 created |
| var38 | 117310.979016494 | 14,868 rows | Replaced with NaN then filled with median. Binary flag var38_was_mode created |
| All delta_ columns | 1e10 | Many rows | All 26 delta columns dropped entirely |

## Constant columns dropped — all 34
These columns have the same value for every single customer.
They contain zero information and were removed in cleaning.

ind_var2_0, ind_var2, ind_var27_0, ind_var28_0, ind_var28,
ind_var27, ind_var41, ind_var46_0, ind_var46, num_var27_0,
num_var28_0, num_var28, num_var27, num_var41, num_var46_0,
num_var46, saldo_var28, saldo_var27, saldo_var41, saldo_var46,
imp_amort_var18_hace3, imp_amort_var34_hace3,
imp_reemb_var13_hace3, imp_reemb_var33_hace3,
imp_trasp_var17_out_hace3, imp_trasp_var33_out_hace3,
num_var2_0_ult1, num_var2_ult1, num_reemb_var13_hace3,
num_reemb_var33_hace3, num_trasp_var17_out_hace3,
num_trasp_var33_out_hace3, saldo_var2_ult1,
saldo_medio_var13_medio_hace3

## Engineered features created in Phase 3
| Feature name | How it is calculated | Why it helps |
|---|---|---|
| count_zeros | Count of features equal to zero per customer row | Most powerful engineered feature. Inactive customers have many zeros and are more likely dissatisfied |
| count_ones | Count of features equal to one per row | Captures sparsity pattern across binary indicator columns |
| count_neg | Count of negative features per row | Negative balances signal financial stress |
| num_nonzero | Count of non-zero features per row | Engagement proxy — active customers have more non-zero values |
| row_sum | Sum of all features per row | Total activity level |
| row_mean | Mean of all features per row | Average activity level |
| row_std | Standard deviation of all features per row | Spread of activity |
| row_max | Maximum feature value per row | Peak activity |
| is_young | 1 if var15 is less than 23, else 0 | Deterministic rule — zero unsatisfied customers under 23 in entire training data |
| is_elderly | 1 if var15 is greater than 80, else 0 | Slightly elevated dissatisfaction rate in this segment |
| saldo_var30_zero | 1 if saldo_var30 equals zero, else 0 | Over 50% of unsatisfied customers have zero cash balance |
| saldo5_ult3_zero | 1 if saldo_medio_var5_ult3 equals zero, else 0 | 65% of unsatisfied customers have zero recent average balance |
| var38_was_mode | 1 if var38 was the sentinel value, else 0 | The missingness itself is predictive |
| var3_missing | 1 if var3 was -999999, else 0 | Unknown nationality may correlate with account type |
| var36_is_99 | 1 if var36 equals 99, else 0 | Dominant missing-value category |
| saldo_*_log | log1p of all saldo columns | Fixes right skew in balance distributions |
| imp_*_log | log1p of all imp columns | Fixes right skew in transaction amount distributions |
| var38_log | log1p of var38 | Fixes right skew in mortgage/net worth distribution |
| base_delta | ult1 minus ult3 for key base features | Captures trend — is activity going up or down? |
| base_ratio | ult1 divided by ult3 for key base features | Captures relative change — by how much? |

## Data leakage prevention rules
| Rule | Plain English reason |
|---|---|
| y_train.pkl saved separately from X | The target (who is dissatisfied) must never be in the feature set |
| Cleaning done on concat(train + test) | Both datasets get identical column treatment — no shape mismatch later |
| StandardScaler fit on fold train split only | If you fit on the full dataset, the test data leaks its statistics into training |
| SMOTE applied inside CV folds only | If you oversample before splitting, fake minority samples appear in validation — your AUC looks great but it is a lie |
| Target encoding inside CV folds only | If you encode using the full TARGET column, you leak the answer into the features |
| Post-processing applied after ensemble only | These rules are applied to predictions, not used during training |
