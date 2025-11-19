import joblib
import numpy as np
import pandas as pd
import sys
import os

# ==========================================
#           USER CONFIGURATION
# ==========================================

# Select Input Mode: set to 'csv' or 'manual'
INPUT_MODE = 'csv'
# INPUT_MODE = 'manual'

# --- CONFIGURATION FOR CSV MODE ---
CSV_FILE_PATH = 'ACLF_TEST_COHORT.csv'
# The row index in the CSV file you want to predict (integer)
CSV_ROW_INDEX = 1

# --- CONFIGURATION FOR MANUAL MODE ---
# Enter values here if INPUT_MODE is set to 'manual'
MANUAL_VALUES = {
    'TB': 351.2,  # Total Bilirubin (umol/L)
    'Na': 139,  # Sodium (mmol/L)
    'PLT': 127,  # Platelets
    'INR': 1.56,  # INR
    'SWE': 39.7  # 2D-SWE (kPa)
}

# ==========================================
#           SYSTEM CONFIGURATION
# ==========================================

FEATURE_LIST = ['TB', 'Na', 'PLT', 'INR', 'SWE']

MODEL_PATHS = {
    '1_month': 'Model_1.pkl',
    '3_months': 'Model_2.pkl',
    '1_year': 'Model_3.pkl'
}


def load_models():
    """
    Loads the pre-trained models from disk.
    """
    models = {}
    try:
        print("--- Loading Models ---")
        models['model_1'] = joblib.load(MODEL_PATHS['1_month'])
        models['model_2'] = joblib.load(MODEL_PATHS['3_months'])
        models['model_3'] = joblib.load(MODEL_PATHS['1_year'])
        print("Models loaded successfully.\n")
        return models
    except FileNotFoundError as e:
        print(f"Error: Model file not found. {e}")
        sys.exit(1)


def get_csv_data(file_path, row_idx):
    """
    Reads data from a CSV file based on the specified row index.
    """
    row_idx = row_idx - 1
    print(f"--- Processing CSV Mode (File: {file_path}, Row: {row_idx}) ---")
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        df = pd.read_csv(file_path, encoding='gbk')

        # Validate columns
        missing_cols = [col for col in FEATURE_LIST if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing columns in CSV: {missing_cols}")

        # Check index bounds
        if row_idx < 0 or row_idx > len(df):
            raise IndexError(f"Row index {row_idx} is out of bounds (Max: {len(df)}).")

        # Extract features and reshape to (1, -1)
        data = df[FEATURE_LIST].iloc[row_idx].values.reshape(1, -1)
        print(f"Data loaded: {data}")
        return data

    except Exception as e:
        print(f"CSV Error: {e}")
        sys.exit(1)


def get_manual_data(values_dict):
    """
    Converts manual dictionary input into a numpy array.
    """
    print("--- Processing Manual Mode ---")
    try:
        # Ensure order is correct based on FEATURE_LIST
        data_list = [values_dict[feature] for feature in FEATURE_LIST]
        data = np.array(data_list).reshape(1, -1)
        print(f"Data loaded: {data}")
        return data
    except KeyError as e:
        print(f"Manual Data Error: Missing value for feature {e}")
        sys.exit(1)


def predict_and_output(models, data_input):
    """
    Runs the prediction and prints the formatted output.
    """
    print("\n--- Prediction Results ---")

    # Predict probabilities for the positive class (index 1)
    prob_1 = models['model_1'].predict_proba(data_input)[:, 1][0]
    prob_2 = models['model_2'].predict_proba(data_input)[:, 1][0]
    prob_3 = models['model_3'].predict_proba(data_input)[:, 1][0]

    # Format and print
    print('Risk Factor (One Month)   : {:.0f}%'.format(prob_1 * 100))
    print('Risk Factor (Three Months): {:.0f}%'.format(prob_2 * 100))
    print('Risk Factor (One Year)    : {:.0f}%'.format(prob_3 * 100))


if __name__ == '__main__':

    # 1. Load Models
    models = load_models()

    # 2. Prepare Data based on Input Mode
    final_input_data = None

    if INPUT_MODE.lower() == 'csv':
        final_input_data = get_csv_data(CSV_FILE_PATH, CSV_ROW_INDEX)

    elif INPUT_MODE.lower() == 'manual':
        final_input_data = get_manual_data(MANUAL_VALUES)

    else:
        print(f"Error: Invalid INPUT_MODE '{INPUT_MODE}'. Please choose 'csv' or 'manual'.")
        sys.exit(1)

    # 3. Execute Prediction
    predict_and_output(models, final_input_data)