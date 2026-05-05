# Team Alignment: Feature Engineering & Ensembling Guidelines

Hello Team! 👋

I've completed the feature engineering pipeline (see `02_Feature_Engineering.ipynb`) and generated the clean dataset:
* `train_clean.pkl`
* `test_clean.pkl`

As we are all building different models on this dataset with the ultimate goal of **ensembling** them at the end, it is critical that we align on a few key rules to ensure our models are compatible and don't suffer from data leakage.

---

## 1. 🚨 Identical Cross-Validation Folds (CRITICAL)
If we plan on doing any form of stacking or blending (using the predictions of our models to train a final meta-model), **we MUST use the exact same Train/Validation split indices**. 

* **The Danger:** If my validation set overlaps with your training set, our final meta-model will suffer from severe data leakage and overfit tremendously.
* **The Solution:** We must all use the exact same seed and fold strategy. 
  * Let's agree to use `StratifiedKFold(n_splits=5, random_state=42)` across all our models.
  * *Do not shuffle the data independently before splitting.*

## 2. ⚖️ Standard Scaling Requirement
The current `_clean.pkl` files have `log1p` applied to skewed features (like `saldo` and `var38`), but **they are NOT standard scaled**. 

* **Tree Models (XGBoost, LightGBM, Random Forest):** You are good to go. Tree models do not require scaling.
* **Distance/Linear Models (Neural Networks, SVM, Logistic Regression, KNN):** You **MUST** apply a `StandardScaler` or `MinMaxScaler` inside your pipeline before training. If you train directly on the raw `.pkl` features, your models will likely fail to converge or perform very poorly.

## 3. 📉 Correlation Drops & Advanced Models
In my pipeline (Step 7), I dropped features with `< 1e-3` linear correlation to the target, and dropped highly inter-correlated features (keeping the one with higher target correlation).

* **Why this matters:** A feature might have near-zero *linear* correlation with the target, but a Neural Network or an XGBoost model might still find a highly predictive *non-linear* interaction between that feature and another one. 
* **The Solution:** If you are running highly complex models and find they are underperforming, let me know! I can easily spin up an alternative dataset version that skips **Step 7** so your models have access to the full feature space to find non-linear patterns.

## 4. 📊 Probability Outputs Only
When saving your Out-Of-Fold (OOF) predictions and Test predictions for the ensemble:
* Please ensure your models output **predicted probabilities** (e.g., using `.predict_proba()[:, 1]`) ranging from `0.0` to `1.0`.
* **Do NOT save hard class labels (0 or 1).** Ensembling hard classes loses a lot of confidence nuance and performs significantly worse than averaging probabilities.

---

### ✅ Quick Checklist Before Training:
- [ ] Am I using `StratifiedKFold(n_splits=5, random_state=42)`?
- [ ] If I'm building a NN/SVM/LogReg, did I add `StandardScaler` to my pipeline?
- [ ] Am I saving OOF probabilities instead of hard 0/1 predictions?
- [ ] Am I reading directly from `train_clean.pkl` and `test_clean.pkl` without re-running early preprocessing?

Let me know if you have any questions!
