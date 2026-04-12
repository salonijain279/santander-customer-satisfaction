# Model card — Santander Customer Satisfaction Classifier

A model card is a standard industry document that describes
what a model does, how it was built, and what it should and
should not be used for. Fill in the blanks after training.

## Model details
| Property | Value |
|---|---|
| Model type | Ensemble — XGBoost + LightGBM + Random Forest + MLP + LogReg |
| Version | 1.0 |
| Date | April 2026 |
| Team | Saloni, Shiv, Parul, Madhu, Bhavisha |
| Evaluation metric | AUC-ROC |
| Final CV AUC | fill after tuning |
| Public LB AUC | fill after submission |

## Intended use
Identify retail banking customers at risk of dissatisfaction
so the bank can intervene proactively. Internal business use only.

## What this model must NOT be used for
- Automatically closing or restricting customer accounts
- Denying products or services
- Any decision where model output is the only input
- Customers outside the Santander retail banking segment

## Training data
| Property | Value |
|---|---|
| Source | Kaggle — Santander Customer Satisfaction 2016 |
| Training rows | 76,020 |
| Features | 369 anonymized numeric |
| Target | 0=satisfied, 1=unsatisfied |
| Class balance | 96% satisfied, 4% unsatisfied |

## Performance
| Metric | Value |
|---|---|
| CV AUC-ROC | fill |
| CV AUC std | fill |
| Public LB AUC | fill |
| Naive baseline (always predict 0) | 0.500 AUC |
| Random baseline | 0.500 AUC |

## Validation strategy
- StratifiedKFold n=5, random_state=42
- Each model trained with 5 random seeds, predictions averaged
- No data leakage — all transforms fit inside CV folds only
- Public LB used for reference only, not for model selection

## Known limitations
- Features are anonymized — cannot verify what they represent
- Data is from 2015-2016 — customer behaviour may have changed
- Model is correlational, not causal
- Performance on minority class is uncertain due to 96:4 imbalance
