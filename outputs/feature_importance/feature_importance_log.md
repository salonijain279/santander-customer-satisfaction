# Feature importance log

After every model run, call save_feature_importance() from utils.py.
Then update the top 5 rows in the table for your model below.
A feature appearing in the top 20 across multiple models is
genuinely important. A feature that only helps one model should
stay in that model's specific pipeline, not the master dataframe.

## Top features by model (fill after Day 6 baselines)

### XGBoost — owner: Saloni
| Rank | Feature | Importance | Date |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### LightGBM — owner: Shiv
| Rank | Feature | Importance | Date |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### Random Forest — owner: Parul
| Rank | Feature | Importance | Date |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Features confirmed important across ALL models
Fill this after Day 7 when all baselines are done.

| Feature | XGB rank | LGBM rank | RF rank | Decision |
|---|---|---|---|---|
| | | | | |

## Engineered features — did they help?
Fill this by running model with and without each feature.

| Feature | AUC with | AUC without | Delta | Keep? |
|---|---|---|---|---|
| count_zeros | | | | |
| is_young | | | | |
| saldo_var30_zero | | | | |
| saldo5_ult3_zero | | | | |
| var38_log | | | | |
| temporal deltas | | | | |
