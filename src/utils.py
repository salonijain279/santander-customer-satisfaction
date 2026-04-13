"""
utils.py — CV harness, scoring, and experiment logging
Owner: Bhavisha
Due: Day 5

What to build here:
1. get_skf()            — returns the standard StratifiedKFold
2. run_cv()             — runs 5-fold CV, returns OOF predictions + AUC
3. run_cv_multiseed()   — runs CV across 5 seeds, averages predictions
4. log_experiment()     — appends one row to experiments.csv
5. save_feature_importance() — saves top 30 features to outputs/

CRITICAL RULES (do not break these):
- StandardScaler must be fit inside CV fold train split ONLY
- Never fit scaler on full X or on test data
- OOF predictions: row i must be predicted by fold that never trained on row i
- y (TARGET) is passed in as argument, never loaded from file inside here
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from src.config import CV_N_SPLITS, CV_RANDOM_STATE


def get_skf():
    """
    Returns the standard StratifiedKFold splitter for the project.
    Always use this — never create StratifiedKFold inline in notebooks.
    Guarantees identical folds across all team members.
    """
    return StratifiedKFold(
        n_splits=CV_N_SPLITS,
        shuffle=True,
        random_state=CV_RANDOM_STATE
    )

def auc(y_true, y_pred):
    """Simple AUC-ROC scorer. Use this everywhere — never use accuracy."""
    return roc_auc_score(y_true, y_pred)
    

def run_cv(model, X, y, scale=False, model_name='model'):
    """
    Runs stratified 5-fold cross-validation.

    Args:
        model      : sklearn model with predict_proba method
        X          : feature dataframe — master_train (no TARGET column)
        y          : target series — y_train (always kept separate)
        scale      : True for LogReg and MLP, False for tree models
        model_name : string label for printing

    Returns:
        oof      : numpy array of OOF predictions, shape (76020,)
        mean_auc : float — average AUC across 5 folds
        std_auc  : float — standard deviation across 5 folds
        fold_aucs: list of 5 individual fold AUC scores
    """
    pass  # Bhavisha to implement


def run_cv_multiseed(model_fn, X, y, seeds, scale=False, model_name='model'):
    """
    Trains the same model across multiple random seeds.
    Averages OOF predictions across seeds.
    Adds 0.001-0.003 AUC for free by reducing variance.

    Args:
        model_fn : function that returns a fresh model e.g. get_xgb_baseline
        seeds    : list of random states e.g. [42, 7, 13, 99, 21]

    Returns:
        avg_oof     : averaged OOF predictions
        all_aucs    : dict of seed -> mean_auc
        overall_auc : AUC of the averaged OOF
    """
    pass  # Bhavisha to implement


def log_experiment(model_name, member, features_desc, params,
                   imbalance_method, cv_auc_mean, cv_auc_std,
                   seed_aucs=None, public_lb_auc=None, notes=''):
    """
    Appends one row to experiments.csv.
    Call this after every single CV run without exception.

    Args:
        model_name      : e.g. 'XGBoost'
        member          : e.g. 'Saloni'
        features_desc   : e.g. 'top_250 + count_zeros + log_var38'
        params          : dict of hyperparameters used
        imbalance_method: e.g. 'scale_pos_weight=20'
        cv_auc_mean     : float
        cv_auc_std      : float
        seed_aucs       : dict of seed -> auc e.g. {42: 0.831, 7: 0.829}
        public_lb_auc   : float or None (fill after Kaggle submission)
        notes           : e.g. 'count_zeros added +0.003 AUC'
    """
    pass  # Bhavisha to implement


def save_feature_importance(importances, feature_names, model_name, member):
    """
    Saves top 30 feature importances to outputs/feature_importance/
    Filename format: MEMBER_MODELNAME_fi.csv
    e.g. saloni_xgboost_fi.csv

    Args:
        importances   : array of importance scores from model
        feature_names : list of column names
        model_name    : string
        member        : string
    """
    pass  # owner to implement
