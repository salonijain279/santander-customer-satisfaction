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
│   └── 12_Advanced_Tuning_XGB_Cat.ipynb
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

### `08_Ensemble_Stacking.ipynb` — The Final Stage
The "Meta-Model" notebook that combines all previous work.
*   **Simple Average:** Provides a stable, high-performance baseline.
*   **Logistic Regression Stacking:** Learns the optimal weights for each model family based on their OOF performance.

---

## Model Ensemble Architecture

Our winning strategy relies on a **Stacked Generalization** architecture:

1.  **Level 0 (Base Models):** Five models from four different families (GBDT, Bagging, Deep Learning) are trained on the same 5-fold CV split.
2.  **OOF Generation:** Each model generates "Out-Of-Fold" predictions—predicting on the 20% validation set during training. This creates a new "meta-feature" set where each row represents the model's unbiased estimate.
3.  **Level 1 (Meta-Model):** A Logistic Regression model is trained using the OOF predictions as input and the actual `TARGET` as the label. It learns to weight the "Boosters" heavily but uses the "NN" and "RF" to smooth out errors.

---

## Session Log

### May 2, 2026

#### Model Diversification & The "Big Five" Ensemble
- **Goal:** Break the 0.825 AUC barrier by moving beyond a single model.
- **Strategy:** Built a diverse ensemble across four distinct model families:
  - **Boosting:** LightGBM, XGBoost (GPU), and CatBoost.
  - **Bagging:** Random Forest.
  - **Deep Learning:** Neural Network (MLP) with `StandardScaler` integration.
- **Advanced Feature Engineering ("Santander Special"):**
  - Added row-wise statistics: `count_zeros` and `count_non_zeros` to capture product usage density.
  - Created strategic interaction features (e.g., `var15 * var38`) to capture non-linear relationships between age and account value.
- **Hyperparameter Optimization:**
  - Conducted extensive **Optuna** studies (100 trials each) for LightGBM, XGBoost, and CatBoost.
  - Achieved a significant boost in CV AUC (from ~0.838 to **0.841**) by finding the "Gold Tier" parameters for the advanced feature set.

#### Ensembling & Stacking Strategy
- **Methodology:** Implemented **Stacking** to combine the "expert opinions" of all five models.
- **Leak-Free Validation:** Used **Out-Of-Fold (OOF)** predictions. Each model predicts on the 20% validation fold it never saw during training, ensuring no data leakage.
- **Meta-Model:** Trained a `LogisticRegression` "Final Judge" on the OOF predictions. The meta-model learns which base model to trust for specific types of customers.
- **Results:** The ensemble reached a Private Leaderboard score of **0.82716**.

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
- [x] Final Ensemble — OOF Stacking — **complete**
- [ ] Final project documentation and academic disclosure
