"""
models.py — baseline model configurations
Owner: Saloni
Due: Day 6 (after baselines are confirmed)

What to build here:
One function per model that returns a configured model instance.
Each function accepts random_state as argument so multi-seed
training works cleanly from utils.run_cv_multiseed().

Models needed (one from each category — prof requirement):
1. get_logreg_baseline()  — Linear model
2. get_rf_baseline()      — Bagging ensemble
3. get_xgb_baseline()     — Gradient boosting
4. get_lgbm_baseline()    — Leaf-wise boosting
5. get_mlp_baseline()     — Deep learning (Madhu owns this one)

Imbalance handling per model:
- LogReg  : class_weight='balanced'
- RF      : class_weight='balanced'
- XGB     : scale_pos_weight=20
- LGBM    : is_unbalance=True
- MLP     : class_weight={0:1, 1:24}
"""

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def get_logreg_baseline(random_state=42):
    """
    Logistic Regression — linear model, benchmark floor.
    Owner: Bhavisha
    Needs StandardScaler applied before training (scale=True in run_cv)
    """
    pass  # Bhavisha to implement


def get_rf_baseline(random_state=42):
    """
    Random Forest — bagging ensemble.
    Owner: Parul
    Does not need scaling.
    """
    pass  # Parul to implement


def get_xgb_baseline(random_state=42):
    """
    XGBoost — gradient boosting.
    Owner: Saloni
    Does not need scaling.
    scale_pos_weight=20 handles the 96:4 class imbalance.
    """
    pass  # Saloni to implement


def get_lgbm_baseline(random_state=42):
    """
    LightGBM — leaf-wise boosting, faster than XGBoost.
    Owner: Shiv
    Does not need scaling.
    is_unbalance=True handles the 96:4 class imbalance.
    """
    pass  # Shiv to implement


def get_mlp_baseline(random_state=42):
    """
    Neural Network MLP — deep learning category.
    Owner: Madhu
    Needs StandardScaler applied before training (scale=True in run_cv)
    Use keras/tensorflow.
    Architecture: 3 hidden layers [512, 256, 128], selu activation,
    AlphaDropout, class_weight={0:1, 1:24}
    """
    pass  # Madhu to implement
