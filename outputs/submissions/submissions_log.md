# Submission log

Every Kaggle submission must be logged here BEFORE submitting.
One row per submission. Max 2 submissions per day (Kaggle limit).

## File naming convention
Format: MMDD_MEMBERNAME_MODEL_VERSION.csv
Examples:
- 0419_saloni_xgb_baseline.csv
- 0421_shiv_lgbm_tuned_v2.csv
- 0422_bhavisha_ensemble_blend1.csv
- 0423_madhu_mlp_smote_v1.csv
- 0424_parul_rf_tuned_v3.csv
- 0425_saloni_stack_final.csv

## The delta rule
Delta = Public LB AUC minus CV AUC
If delta is below -0.005 — something is wrong. Stop and investigate.
Common causes: data leakage, scaler fit on wrong data, SMOTE before split.
If delta is above +0.005 — got lucky on public set. Do not trust it.

## Submission table

| # | Date | File name | Member | Model | CV AUC | Public LB | Delta | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | First submission |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |
| 6 | | | | | | | | |
| 7 | | | | | | | | |
| 8 | | | | | | | | |
| 9 | | | | | | | | |
| 10 | | | | | | | | Best candidate |

## Final submission decisions
Select final 2 based on CV AUC, not public LB AUC.

| Slot | File name | CV AUC | Public LB | Why chosen |
|---|---|---|---|---|
| Final 1 | | | | Best CV AUC overall |
| Final 2 | | | | Best ensemble / backup |
