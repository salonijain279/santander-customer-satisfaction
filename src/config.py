import os

# ── Data paths (local machine) ──────────────────────────
RAW_DATA_PATH    = 'data/raw/'
PROCESSED_PATH   = 'data/processed/'
OOF_PATH         = 'outputs/oof/'
SUBMISSIONS_PATH = 'outputs/submissions/'
FI_PATH          = 'outputs/feature_importance/'

# ── Kaggle notebook path ─────────────────────────────────
# Use this when running inside a Kaggle notebook
KAGGLE_PATH = '/kaggle/input/competitions/santander-customer-satisfaction/'

# ── File shortcuts ───────────────────────────────────────
TRAIN_FILE   = os.path.join(RAW_DATA_PATH, 'train.csv')
TEST_FILE    = os.path.join(RAW_DATA_PATH, 'test.csv')
MASTER_TRAIN = os.path.join(PROCESSED_PATH, 'master_train.pkl')
MASTER_TEST  = os.path.join(PROCESSED_PATH, 'master_test.pkl')
Y_TRAIN      = os.path.join(PROCESSED_PATH, 'y_train.pkl')

# ── CV strategy — never change these values ──────────────
# Changing these would make folds incomparable across team members
CV_N_SPLITS     = 5
CV_RANDOM_STATE = 42
SEEDS           = [42, 7, 13, 99, 21]  # for multi-seed averaging

# ── Column names ─────────────────────────────────────────
TARGET_COL = 'TARGET'
ID_COL     = 'ID'

# ── Sentinel values — confirmed from EDA ─────────────────
# These exact values appear in the data as stand-ins for missing
VAR3_SENTINEL  = -999999          # 116 rows
VAR36_SENTINEL = 99               # 30,064 rows (40% of data)
VAR38_SENTINEL = 117310.979016494 # 14,868 rows (20% of data)

# ── Post-processing thresholds — confirmed from EDA ──────
VAR15_YOUNG_CUTOFF   = 23      # zero unsatisfied customers under 23
VAR15_ELDERLY_CUTOFF = 80      # elevated dissatisfaction above 80
SALDO_VAR30_CUTOFF   = 500000  # zero unsatisfied above this balance

# ── Feature selection sizes ───────────────────────────────
TOP_FEATURES_TREES  = 250  # for XGB, LGBM, RF
TOP_FEATURES_LINEAR = 50   # for LogReg, MLP
