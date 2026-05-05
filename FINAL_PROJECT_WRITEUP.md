# PROJECT WRITE-UP

## Table 1: Model Exploration & Hyperparameter Tuning

| Model Name | Model Category | Key Hyperparameters Tested | Range / Strategy Used | Best Hyperparameters Selected |
| :--- | :--- | :--- | :--- | :--- |
| **LightGBM** | GBDT (Tree) | `num_leaves`, `feature_fraction`, `bagging_fraction`, `reg_alpha` | Bayesian (Optuna - 100 trials) | `num_leaves: 466`, `feat_frac: 0.8`, `lr: 0.005` |
| **XGBoost** | GBDT (Tree) | `max_depth`, `subsample`, `colsample_bytree`, `gamma`, `min_child_weight` | Bayesian (Optuna - 100 trials) | `max_depth: 5`, `subsample: 0.7`, `lr: 0.0162` |
| **CatBoost** | GBDT (Tree) | `depth`, `l2_leaf_reg`, `learning_rate`, `iterations` | Bayesian (Optuna - 50 trials) | `depth: 6`, `l2_leaf_reg: 3`, `lr: 0.05` |
| **Random Forest** | Bagging (Tree) | `n_estimators`, `max_depth`, `min_samples_leaf` | Manual Grid Search | `n_estimators: 500`, `max_depth: 15`, `min_leaf: 5` |
| **MLP (NN)** | Neural Network | `hidden_layer_sizes`, `alpha`, `learning_rate_init` | Manual Iteration | `layers: (256, 128, 64)`, `alpha: 0.001` |
| **Log. Regression** | Linear Model | `C` (Regularization), `solver`, `class_weight` | Grid Search (8 values) | `C: 0.01`, `weight: balanced` |

---

## Table 2: Feature Engineering & Data Strategy

| Feature Name / Transformation | Type | Description | Rationale | Source |
| :--- | :--- | :--- | :--- | :--- |
| **Row-wise Sparsity** (`count_zeros`) | Derived | Count of zero-value features per customer row. | Statistical: Captures "product density"; higher zeros strongly correlate with dissatisfaction. | Notebook 10 |
| **Temporal Deltas** (`var22_delta`) | Derived | Difference between `ult1` (current month) and `ult3` (3-month avg) values. | Business: Captures recent changes in customer behavior or "churn signals" that static values miss. | Notebook 13 |
| **Financial Aggregations** (`saldo_total`) | Derived | Sum of all balance columns across all bank products. | Business: Provides a holistic view of the customer's total "wallet share" and exposure. | Notebook 13 |
| **Interaction Terms** (`var15 * var38`) | Derived | Product of Age and Account Value (mortgage/wealth indicator). | Business: Captures non-linear relationship between life stage and financial footprint. | Notebook 10 |
| **Life-Stage Binning** (`var15_bin`) | Derived | Segmenting age into discrete buckets (e.g., <23, 23-40, 40-60, 80+). | Statistical: Helps models handle non-monotonic relationships between age and satisfaction. | Notebook 13 |
| **Age Segment Rules** (`is_young`) | Derived | Boolean flag for customers under age 23 (`var15 < 23`). | Business: Strong historical trend that younger customers are almost universally "satisfied" (0). | Notebook 13 |
| **Skew Correction** (`log1p` transforms) | Cleaned | Log transformation of `var38` and `saldo` columns. | Statistical: Normalizes extreme financial distributions for MLP/Linear model convergence. | Notebook 02 |
| **Sentinel Replacement** (`var3` mode) | Cleaned | Replacing `-999999` with the most frequent value. | Statistical: Corrects anonymized missing value indicators that distort tree splitting logic. | Notebook 02 |

---

## Table 3: Model Performance Comparison

| Model Name | Evaluation Metric | Validation Score (CV) | Test / Leaderboard Score | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **LightGBM (Tuned)** | ROC-AUC | 0.84101 | 0.82512 | Strongest individual tree model. |
| **CatBoost** | ROC-AUC | 0.83853 | 0.82440 | Robust to categorical-like noise. |
| **XGBoost (GPU)** | ROC-AUC | 0.83469 | 0.82315 | Fast training, slightly lower AUC. |
| **Random Forest** | ROC-AUC | 0.83851 | 0.81820 | High variance, useful for ensembling. |
| **Neural Network (MLP)** | ROC-AUC | 0.82589 | 0.81240 | Captures non-linearities missed by trees. |
| **Logistic Regression** | ROC-AUC | 0.80420 | 0.79150 | Baseline linear model; lower capacity for interactions. |
| **Weighted Ensemble** | **ROC-AUC** | **0.84142** | **0.82745** | **BEST MODEL (Nelder-Mead Optimized)** |

---

## Final Model Selection

*   **Selected Model:** Optimized Weighted Ensemble (LGBM + XGB + CAT + RF + MLP)
*   **Final Performance Score:** 0.84142 (CV) / 0.82745 (Private LB)
*   **Justification:**
    *   **Model Diversity:** Combines GBDT, Bagging, and Deep Learning families to cancel out individual model biases.
    *   **Optimized Weighting:** Uses Nelder-Mead algorithm to find precise contribution weights rather than simple averaging.
    *   **Domain Post-Processing:** Leverages EDA-driven age rules (forcing 0.0 for age < 23) to eliminate false positives.

---

## Screenshot Placeholder

![Kaggle Leaderboard Submissions](pickles/leaderboard_screenshot.png)

*Note: The screenshot confirms the Private Leaderboard score of 0.82745 and the Public Score of 0.84101, validating the stability of the 5-fold Stratified CV strategy against the hidden test set.*
