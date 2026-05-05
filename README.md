# Santander Customer Satisfaction — Predictive Analytics Project

Predicting which customers are dissatisfied with Santander Bank using anonymized tabular data.  
This is a binary classification problem with severe class imbalance (~24:1 ratio).

**Course:** MSBA — Predictive Analytics  
**Dataset:** [Kaggle — Santander Customer Satisfaction](https://www.kaggle.com/c/santander-customer-satisfaction)  
**Metric:** AUC-ROC (not accuracy — due to imbalance)

---

## Project Structure

```
santander-customer-satisfaction/
├── data/
│   └── raw/               # train.csv, test.csv (from Kaggle)
├── notebooks/
│   ├── 01_eda.ipynb       # Exploratory Data Analysis
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_CV_Splits_Setup.ipynb
│   ├── 04_LightGBM.ipynb
│   ├── 05_XGBoost.ipynb
│   ├── 06_RandomForest.ipynb
│   ├── 07_NeuralNetwork.ipynb
│   ├── 08_Ensemble_Stacking.ipynb
│   ├── 09_CatBoost.ipynb
│   ├── 10_Advanced_Feature_Engineering.ipynb
│   ├── 11_Optuna_Tuning.ipynb
│   ├── 12_Advanced_Tuning_XGB_Cat.ipynb
│   ├── 13_Ensemble-best-allinone_light_gbm.ipynb  # Champion Nelder-Mead Blend
│   ├── 14_logistic-regression.ipynb               # Baseline exploration
│   └── 15_Mlp_nn.ipynb                            # Final Neural Network Refinement
├── pickles/               # OOF and Test predictions (lgbm_oof.pkl, etc.)
├── requirements.txt
└── README.md
```

---

## Setup

```bash
# Install all dependencies
pip3 install -r requirements.txt

# Add Python scripts to PATH (run once)
echo 'export PATH="/Users/dagur/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Launch Jupyter
jupyter notebook
```

---

## Notebooks

### `01_eda.ipynb` — Exploratory Data Analysis
Comprehensive analysis of the 371 anonymized features. Identified key insights like the `-999999` sentinel value in `var3`, the extreme sparsity (~90% zeros), and the critical predictive power of `var38` (account value) and `var15` (age).

### `02_Feature_Engineering.ipynb` — Initial Engineering
Standardized the feature set from 369 down to **95 core features** through zero-variance removal, duplicate detection, and correlation-based filtering. Created initial baseline features like `num_zeros` and age bins.

### `03_CV_Splits_Setup.ipynb` — Shared CV Strategy
The foundation for our ensemble. This notebook establishes a fixed **5-fold Stratified Cross-Validation** split. By saving these indices to `cv_fold_indices.pkl`, we ensure every model in the ensemble "sees" the exact same training and validation subsets, which is a prerequisite for leak-free stacking.

### `04_LightGBM.ipynb` — The First Booster
Implemented a production-grade LightGBM pipeline using **5-Fold Cross-Validation** with a shared seed. Exported **Out-Of-Fold (OOF)** predictions to `pickles/` to enable leak-free ensembling.

### `05_XGBoost.ipynb` — GPU-Accelerated Boosting
Implemented XGBoost using the `hist` tree method for GPU acceleration in Google Colab. Updated logic to handle XGBoost v2.0+ requirements (moving `early_stopping_rounds` to the constructor).

### `06_RandomForest.ipynb` — The Bagging Family
Introduced a Random Forest model to provide architectural diversity. While slightly lower in individual AUC (~0.818), its uncorrelated errors make it a vital contributor to the final ensemble.

### `07_NeuralNetwork.ipynb` — Deep Learning (MLP)
A Multi-Layer Perceptron (MLP) built with TensorFlow. Features an internal `StandardScaler` to ensure the mathematical weights aren't dominated by large-scale features like `var38`. This model finds non-linear patterns that tree-based models often miss.

### `09_CatBoost.ipynb` — The Third Booster
Completed the "Big Three" gradient boosters. CatBoost’s symmetric tree structure provides a robust "third opinion" that helped bridge the gap to 0.827 AUC.

### `10_Advanced_Feature_Engineering.ipynb` — The "Santander Special"
The breakthrough notebook where we implemented:
*   **Row-wise Sparsity:** `count_zeros` and `count_non_zeros`.
*   **Feature Interactions:** Top-tier interactions like `var15 * var38` (Age * Mortgage) and `var15 * saldo_var30`.
*   **Result:** Increased feature count to **102** and significantly improved CV stability.

### `11_Optuna_Tuning.ipynb` & `12_Advanced_Tuning_XGB_Cat.ipynb`
Automated Bayesian hyperparameter optimization using **Optuna**. Ran 100 trials for each booster to find the "Gold Tier" configuration for `learning_rate`, `max_depth`, and `lambda` regularization.

### `13_Ensemble-best-allinone_light_gbm.ipynb` — The Champion Model
The master ensemble notebook. Instead of simple stacking, it uses **Nelder-Mead optimization** to find the precise mathematical weights for each of the "Big Five" models. This optimization achieved our peak performance of **0.82745** on the Private Leaderboard.

### `14_logistic-regression.ipynb` — Baseline Benchmarking
An exploratory notebook focusing on the Linear Model family. While it served as a robust baseline (CV AUC ~0.804), it confirmed that the complex non-linear interactions in the data are best captured by our tree-based boosters.

### `15_Mlp_nn.ipynb` — Final Neural Network Refinement
Refined MLP architecture incorporating the class-imbalance weights (24:1) and the advanced feature interactions. This notebook produced the final deep-learning probabilities used in the champion blend.

---

## Model Ensemble Architecture

Our winning strategy relies on a **Weighted Blend Optimization** architecture:

1.  **Level 0 (Base Models):** Five models from four different families (LGBM, XGB, CAT, RF, MLP) trained on the same 5-fold CV split.
2.  **OOF Generation:** Each model generates "Out-Of-Fold" predictions to create an unbiased meta-feature set.
3.  **Level 1 (Optimization):** Used the **Nelder-Mead algorithm** to minimize the log-loss of the weighted average. This effectively "learnt" that the LightGBM and CatBoost models were the most reliable, while the MLP provided critical diversity to reduce variance.

---

## Session Log

### May 4, 2026

#### Finalization & Academic Reporting
- **Champion Model Finalization:** Finalized the **Nelder-Mead Ensemble** weights, achieving a Private Leaderboard score of **0.82745**.
- **Project Documentation:**
  - Generated a professional, table-driven **FINAL_PROJECT_WRITEUP.md**.
  - Created a script-based conversion to **Word (.docx)** format for academic submission.
- **Repository Cleanup:** Moving all final code to the `main` branch and implementing a robust `.gitignore` to handle large binary artifacts.

---

## Key Findings (EDA & Modeling)

| Finding | Detail |
|---|---|
| Class imbalance | 96% satisfied, 4% dissatisfied — use AUC, not accuracy |
| Hidden missing values | `var3 = -999999` → replace with mode in Feature Engineering |
| Sparsity | ~90% zeros — `num_zeros` per row is a critical engineered feature |
| Feature Interactions | `var15 * var38` (Age * Value) significantly improves booster performance |
| Ensemble Value | Stacking different families (Trees vs. NN) reduces noise and boosts score by ~0.002+ |

---

## Feature Journey Summary

| Step | Action | Features |
|---|---|---|
| Start | Raw features (excl. ID, TARGET) | 369 |
| Phase 1 | Initial Cleaning & Selection | 95 |
| Phase 2 | Advanced FE (Zeros & Interactions) | **102** |

---

## Next Steps

- [x] Feature Engineering (`02_Feature_Engineering.ipynb`) — **complete**
- [x] Model Training — LGBM, XGBoost, CatBoost, RF, NN — **complete**
- [x] Hyperparameter tuning — Optuna optimization — **complete**
- [x] Final Ensemble — Nelder-Mead Optimization — **complete**
- [x] Final project documentation and academic report generation — **complete**
