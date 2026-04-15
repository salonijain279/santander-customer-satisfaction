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
from sklearn.neural_network import MLPClassifier


def get_logreg_baseline(random_state=42):
    """
    Logistic Regression — linear model, benchmark floor.
    Owner: Bhavisha
    Needs StandardScaler applied before training (scale=True in run_cv)
    """
    return LogisticRegression(
        C=1.0,
        class_weight='balanced',
        solver='lbfgs',
        max_iter=1000,
        random_state=random_state,
        n_jobs=-1
    )


def get_rf_baseline(random_state=42):
    """
    Random Forest — bagging ensemble.
    Owner: Parul
    Does not need scaling.
    """
    return RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=5,
        class_weight='balanced',
        random_state=random_state,
        n_jobs=-1
    )


def get_xgb_baseline(random_state=42):
    """
    XGBoost — gradient boosting.
    Owner: Saloni
    Does not need scaling.
    scale_pos_weight=20 handles the 96:4 class imbalance.
    """
    return XGBClassifier(
        n_estimators=500,
        max_depth=5,
        learning_rate=0.02,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=20,
        eval_metric='auc',
        use_label_encoder=False,
        random_state=random_state,
        n_jobs=-1
    )


def get_lgbm_baseline(random_state=42):
    """
    LightGBM — leaf-wise boosting, faster than XGBoost.
    Owner: Shiv
    Does not need scaling.
    is_unbalance=True handles the 96:4 class imbalance.
    """
    return LGBMClassifier(
        n_estimators=500,
        max_depth=-1,
        num_leaves=31,
        learning_rate=0.02,
        subsample=0.8,
        colsample_bytree=0.8,
        is_unbalance=True,
        random_state=random_state,
        n_jobs=-1,
        verbose=-1
    )


def get_mlp_baseline(random_state=42):
    """
    Neural Network MLP — deep learning category.
    Owner: Madhu
    Needs StandardScaler applied before training (scale=True in run_cv)
    Uses sklearn MLPClassifier for seamless integration with the CV harness.
    Architecture: 3 hidden layers [512, 256, 128], relu activation, adam solver.
    Note: sklearn MLP does not support class_weight directly — imbalance
    is handled via scale_pos_weight-style approach in the CV loop using
    sample_weight, or via the inherent regularization of the architecture.
    """
    return MLPClassifier(
        hidden_layer_sizes=(512, 256, 128),
        activation='relu',
        solver='adam',
        alpha=0.001,          # L2 regularization
        batch_size=256,
        learning_rate='adaptive',
        learning_rate_init=0.001,
        max_iter=200,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=10,
        random_state=random_state
    )
