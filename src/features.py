"""
features.py — all feature engineering and cleaning functions
Owner: Parul
Due: Day 5

What to build here (in order):

CLEANING (run on concat train+test, split back after):
1. drop_constant_cols()         — remove 34 confirmed constant columns
2. drop_duplicate_cols()        — remove exact copy columns
3. drop_delta_cols()            — remove all delta_*_1y3 columns (1e10 sentinel)
4. impute_sentinels()           — fix var3, var36, var38 sentinel values
5. drop_high_correlation_cols() — remove one from each correlated pair

FEATURE ENGINEERING (still on concat, no y involved):
6. add_row_statistics()   — count_zeros, count_ones, row_sum etc.
7. add_rule_flags()       — is_young, is_elderly, saldo_var30_zero etc.
8. add_log_transforms()   — log1p on all saldo_ and imp_ columns
9. add_temporal_deltas()  — ult1 minus ult3 pairs

POST-PROCESSING (call ONLY on final predictions, never inside CV):
10. apply_post_processing() — set prob=0 where var15<23 or saldo>500000

MASTER PIPELINES:
11. run_full_cleaning_pipeline()  — runs steps 1-5 in correct order
12. run_full_feature_pipeline()   — runs steps 6-9 in correct order

CRITICAL ORDER RULE:
Impute sentinels (step 4) MUST run BEFORE drop_high_correlation_cols (step 5)
Reason: -999999 in var3 distorts correlation values if left in
"""

import numpy as np
import pandas as pd
from src.config import (VAR3_SENTINEL, VAR36_SENTINEL, VAR38_SENTINEL,
                        VAR15_YOUNG_CUTOFF, VAR15_ELDERLY_CUTOFF,
                        SALDO_VAR30_CUTOFF)


def drop_constant_cols(df):
    """
    Remove columns where every value is identical.
    Confirmed from EDA: exactly 34 such columns exist.
    These carry zero information — removing them speeds up all models.
    """
    pass  # Parul to implement


def drop_duplicate_cols(df):
    """
    Remove columns that are exact copies of another column.
    Keep one from each duplicate pair.
    Confirmed from EDA: approximately 5 duplicate pairs exist.
    """
    pass  # Parul to implement


def drop_delta_cols(df):
    """
    Drop all 26 columns starting with delta_
    Reason: EDA showed max value = 1e10 (a sentinel for missing data)
    These columns are dominated by this sentinel — mostly noise.
    """
    pass  # Parul to implement


def impute_sentinels(df):
    """
    Rules confirmed from EDA:
    - var3 == -999999     : 116 rows  → replace with mode, add var3_missing flag
    - var36 == 99         : 30064 rows → keep as category (too frequent to drop),
                            add var36_is_99 flag
    - var38 == 117310.979 : 14868 rows → replace with NaN then median,
                            add var38_was_mode flag
    """
    df = df.copy()

    # --- var3: -999999 = unknown nationality ---
    var3_mode = df.loc[df['var3'] != VAR3_SENTINEL, 'var3'].mode()[0]
    df['var3_missing'] = (df['var3'] == VAR3_SENTINEL).astype(int)
    df['var3'] = df['var3'].replace(VAR3_SENTINEL, var3_mode)
    print(f"var3: replaced {VAR3_SENTINEL} with mode={var3_mode} | flag: var3_missing")

    # --- var36: 99 = dominant missing category ---
    df['var36_is_99'] = (df['var36'] == VAR36_SENTINEL).astype(int)
    var36_mode = df.loc[df['var36'] != VAR36_SENTINEL, 'var36'].mode()[0]
    df['var36'] = df['var36'].replace(VAR36_SENTINEL, var36_mode)
    print(f"var36: replaced {VAR36_SENTINEL} with mode={var36_mode} | flag: var36_is_99")

    # --- var38: sentinel → NaN → median ---
    df['var38_was_mode'] = (df['var38'] == VAR38_SENTINEL).astype(int)
    df['var38'] = df['var38'].replace(VAR38_SENTINEL, np.nan)
    var38_median = df['var38'].median()
    df['var38'] = df['var38'].fillna(var38_median)
    print(f"var38: sentinel → NaN → median={var38_median:.4f} | flag: var38_was_mode")

    # --- Verify zero nulls ---
    remaining_nulls = df.isnull().sum().sum()
    assert remaining_nulls == 0, f"ERROR: {remaining_nulls} nulls remain after imputation!"
    print(f"✅ Zero nulls confirmed. Shape: {df.shape}")

    return df


def drop_high_correlation_cols(df, threshold=0.98):
    """
    Remove one column from each pair where correlation >= threshold.
    IMPORTANT: only call this AFTER impute_sentinels()
    Reason: -999999 left in var3 would make correlations meaningless.
    Reduces ~369 features down to ~143.
    """
    pass  # Bhavisha to implement (she owns the correlation drop per sprint)


def add_row_statistics(df):
    """
    Create aggregate statistics across all features per customer row.
    These capture how 'active' or 'engaged' a customer is.

    Features to create:
    count_zeros  — how many features equal zero for this customer
    count_ones   — how many features equal one
    count_neg    — how many features are negative
    num_nonzero  — how many features are non-zero (engagement proxy)
    row_sum      — sum of all features
    row_mean     — mean of all features
    row_std      — standard deviation across features
    row_max      — maximum feature value

    Why count_zeros matters: dissatisfied customers tend to have
    many zero values — they have fewer active products and
    lower account activity.
    """
    pass  # Shiv to implement (per sprint Day 4 assignment)


def add_rule_flags(df):
    """
    Create binary flags from patterns confirmed in EDA.
    These are the 'free AUC points' — deterministic patterns
    that the data itself showed us.

    Flags to create:
    is_young         — var15 < 23  (zero unsatisfied customers under 23)
    is_elderly       — var15 > 80  (elevated dissatisfaction rate)
    saldo_var30_zero — saldo_var30 == 0  (50%+ unsatisfied have this)
    saldo5_ult3_zero — saldo_medio_var5_ult3 == 0  (65% unsatisfied have this)
    """
    pass  # Parul to implement (per sprint Day 4 assignment)


def add_log_transforms(df):
    """
    Apply log1p transformation to all monetary columns.
    These columns (saldo_ and imp_) are heavily right-skewed —
    a few very large values stretch the scale.
    log1p(x) = log(x+1), safely handles zeros.
    Keep both original and log version — tree models can use both.

    Columns to transform: all saldo_* , all imp_* , and var38
    """
    df = df.copy()

    saldo_cols = [c for c in df.columns if c.startswith('saldo_')]
    imp_cols   = [c for c in df.columns if c.startswith('imp_')]
    extra_cols = ['var38']

    cols_to_transform = saldo_cols + imp_cols + extra_cols
    print(f"Transforming {len(cols_to_transform)} columns")
    print(f"  saldo_: {len(saldo_cols)} | imp_: {len(imp_cols)} | extra: {len(extra_cols)}")

    log_data = {
        f'log1p_{col}': np.log1p(df[col].clip(lower=0))
        for col in cols_to_transform
    }
    df = pd.concat([df, pd.DataFrame(log_data, index=df.index)], axis=1)


    # Verify no inf or NaN introduced
    log_cols   = [f'log1p_{c}' for c in cols_to_transform]
    inf_count  = np.isinf(df[log_cols]).sum().sum()
    null_count = df[log_cols].isnull().sum().sum()

    assert inf_count  == 0, f"ERROR: {inf_count} inf values found!"
    assert null_count == 0, f"ERROR: {null_count} NaN values found!"
    print(f"New log columns added: {len(log_cols)}")
    print(f"Total shape: {df.shape}")
    print(f"✅ No inf or NaN — log transforms clean")

    return df


def add_temporal_deltas(df):
    """
    Create trend features from paired time-window columns.
    For each base feature that has both _ult1 and _ult3 versions:
    - delta = ult1 - ult3  (direction: is it going up or down?)
    - ratio = ult1 / ult3  (relative change: by how much?)

    Handle divide by zero with np.nan then fill with 0.

    Pairs to process:
    num_var22, saldo_medio_var5, saldo_medio_var8,
    num_var45, num_op_var39, num_op_var41
    """
    pass  # Bhavisha to implement (per sprint Day 4 assignment)


def apply_post_processing(preds, X_test):
    """
    Apply deterministic rules to final predictions only.

    WARNING: never call this inside CV or during model training.
    Only call after the final ensemble, just before submission.

    Rules:
    1. var15 < 23       → set probability to 0.0
       (zero unsatisfied customers under 23 in entire training data)
    2. saldo_var30 > 500000 → set probability to 0.0

    Args:
        preds  : numpy array of predicted probabilities
        X_test : test feature dataframe (needs var15 and saldo_var30)

    Returns:
        preds : modified predictions array
    """
    pass  # Bhavisha to implement (per sprint Day 10 assignment)


def run_full_cleaning_pipeline(X, X_test):
    """
    Master cleaning function. Runs all cleaning steps in correct order.
    Concatenates train+test, cleans together, splits back.

    Why concat? So both datasets get identical treatment.
    If we clean separately, a column might be dropped in train
    but kept in test — causing a shape mismatch later.

    Returns: X_clean, X_test_clean
    """
    pass  # Parul to wire together after implementing all steps above


def run_full_feature_pipeline(X_clean, X_test_clean):
    """
    Master feature engineering function. Runs all feature creation steps.
    Also runs on concatenated data — no y involved, zero leakage risk.

    Returns: X_master, X_test_master
    """
    pass  # Parul to wire together after implementing all steps above
