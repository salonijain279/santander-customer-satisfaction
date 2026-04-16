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
│   └── 02_Feature_Engineering.ipynb
├── pickles/               # Saved outputs (plots, pkl files)
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
Covers:
1. Data shape and types (76,020 rows × 371 columns)
2. Missing values — no NaNs, but `var3` uses `-999999` as a hidden missing sentinel
3. Target variable — 96% satisfied (0), 4% dissatisfied (1) → severe 24:1 imbalance
4. Feature groups — `saldo`, `imp`, `num`, `ind`, `delta`, `var`
5. Sparsity — ~90% of all values are zero
6. Key features — `var38` (account value), `var15` (age)
7. Correlation with TARGET
8. Train vs Test distribution check

### `02_Feature_Engineering.ipynb` — Feature Engineering
**Input:** `pickles/train_eda.pkl`, `pickles/test_eda.pkl`  
**Output:** `pickles/train_clean.pkl`, `pickles/test_clean.pkl`

**Golden Rule:** Every transformation applied to train must be applied to test in the same way.

Steps:
1. Remove zero-variance features — dropped **34** features (369 → 335)
2. Remove sparse features (99th pct = 0) — dropped **188** features (335 → 147)
3. Remove duplicate columns — dropped **6** features (147 → 141)
4. Fix `var3` sentinel value — replaced `-999999` with mode (`2`): 116 in train, 120 in test
5. Engineer new features — added **8** features (141 → 149)
6. Log-transform skewed features — transformed **31** `saldo`/`imp` columns (count stays 149)
7. Remove low-correlation + highly inter-correlated features — dropped **54** features (149 → **95**)
8. Save clean pickles

---

## Session Log

### April 15, 2026

#### Environment Setup
- Installed all packages from `requirements.txt` using `pip3` — `xgboost`, `lightgbm`, `tensorflow`, `scikit-learn`, `optuna`, `keras-tuner`, etc. were missing
- Fixed PATH warning: added `/Users/dagur/Library/Python/3.9/bin` to `~/.zshrc` so `pip`, `jupyter`, and `tensorboard` commands work from any terminal

#### Feature Engineering Notebook (`02_Feature_Engineering.ipynb`)
- **Feature journey:** Started with 369 features → ended with **95 features** after 7 cleaning/engineering steps
- **Step 1 — Zero variance removal:** Dropped 34 features that had the same value for every customer (e.g. `ind_var2_0`, `ind_var2`) — these carry zero information
- **Step 2 — Sparse feature removal:** Dropped 188 features where the 99th percentile is 0 (meaning 99%+ of values are zero) — too sparse to be useful
- **Step 3 — Duplicate column removal:** Dropped 6 columns with identical values to another column — common in anonymized datasets; detected using a hash of column values
- **Step 4 — Fix `var3` sentinel value:** Replaced `-999999` (coded missing value) with mode computed from train only — 116 occurrences in train, 120 in test; replacement value = `2`
- **Step 5 — New features engineered:**
  - `num_zeros` — count of zero-valued features per customer (dissatisfied customers tend to use fewer products)
  - `num_zeros_saldo`, `num_zeros_imp`, `num_zeros_num`, `num_zeros_ind` — group-level zero counts
  - `var15_below_23` — binary flag for customers under 23 (different behavior pattern)
  - `var15_bin` — age grouped into 5 bins (bin edges computed from train only, applied to test)
  - `log_var38` — log(1+var38) to fix extreme skew (skewness before: 51.27 → after: 0.38)
- **Step 6 — Log transform skewed financial features:** Applied `log1p` to 31 `saldo` and `imp` columns (skewness > 1.5, all values ≥ 0)
- **Step 7 — Correlation-based removal:**
  - Dropped 2 features with near-zero correlation with TARGET (< 0.001)
  - Dropped 52 features that were > 95% correlated with another feature (kept the one more correlated with TARGET)
- **Sanity checks passed:** No missing values, same columns in train/test, TARGET only in train, no zero-variance remaining

#### EDA Notebook (`01_eda.ipynb`)
- **Bug fix:** Feature group total showed **383** instead of the correct **369** features
  - Root cause: groups used substring matching (`'imp' in c`, `'delta' in c`) which caused columns to appear in multiple groups simultaneously, inflating the sum
  - Fix: use `set()` union across all groups for a true unique count — `all_grouped = set(c for cols in groups.values() for c in cols)`
- **Correlation analysis:** Reviewed Pearson correlations between all features and `TARGET`
  - Values are small (±0.01–0.15) — expected for anonymized banking data
  - `var38` is the strongest single predictor (account value / loan amount)
  - Positive correlation → higher value = more dissatisfied (red bars in plot)
  - Negative correlation → higher value = more satisfied (blue bars in plot)
  - Reminder: use XGBoost feature importance as the real filter, not correlation alone
- **Train vs Test distribution visualization:** Explained the current histogram approach and its limitations
  - `np.log1p()` used because raw values are highly skewed (e.g. `var38` ranges from 0 to millions) — log compresses the scale so differences are visible
  - `clip(lower=0)` applied before log to handle negative values
  - Proposed better alternatives:
    - **KDE plots** — smooth curves, no binning artifacts, filled area for easy comparison
    - **ECDF plots** — best for spotting distributional shift; identical distributions = perfectly overlapping lines
    - Both options include **KS statistic** (Kolmogorov-Smirnov) to quantify shift numerically (KS > 0.10 = investigate)

---

## Key Findings (EDA)

| Finding | Detail |
|---|---|
| Class imbalance | 96% satisfied, 4% dissatisfied — use AUC, not accuracy |
| Hidden missing values | `var3 = -999999` → replace with mode in Feature Engineering |
| Sparsity | ~90% zeros — `num_zeros` per row is a useful engineered feature |
| Useless features | Zero-variance + 99th-pct-is-zero features drop count from 369 → ~142 |
| Strongest predictor | `var38` (account value/loan amount) |
| Age feature | `var15` → create under-23 binary flag + age bins |

---

## Feature Journey Summary

| Step | Action | Features |
|---|---|---|
| Start | Raw features (excl. ID, TARGET) | 369 |
| Step 1 | Remove zero variance | 335 |
| Step 2 | Remove sparse (99th pct = 0) | 147 |
| Step 3 | Remove duplicate columns | 141 |
| Step 4 | Fix var3 (no feature change) | 141 |
| Step 5 | Engineer new features | 149 |
| Step 6 | Log transform (no feature change) | 149 |
| Step 7 | Correlation-based removal | **95** |

---

## Next Steps

- [x] Feature Engineering (`02_Feature_Engineering.ipynb`) — **complete, 95 features ready**
- [ ] Model Training — XGBoost, LightGBM baseline
- [ ] Hyperparameter tuning — Optuna / Keras Tuner
- [ ] Final evaluation on test set
