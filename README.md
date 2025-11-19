# ACLF Risk Prediction System

This repository contains a Python-based tool for predicting the risk factors of Acute-on-Chronic Liver Failure (ACLF) over different time horizons (1 month, 3 months, and 1 year).

The system utilizes pre-trained machine learning models to analyze clinical biomarkers including Total Bilirubin (TB), Sodium (Na), Platelets (PLT), INR, and 2D-Shear Wave Elastography (SWE).

## Project Structure

```text
.
├── ACLFAppUpdated.py      # Main execution script
├── requirements.txt       # Python dependencies
├── Model_1.pkl            # Pre-trained model (1 Month)
├── Model_2.pkl            # Pre-trained model (3 Months)
├── Model_3.pkl            # Pre-trained model (1 Year)
└── ACLF_TEST_COHORT.csv   # Example dataset (optional)
```

## Project Structure
Crucial: The models were trained using `scikit-learn` v1.2.2. Using a newer version (v1.3+) will cause a `ValueError` regarding incompatible dtypes.
### 1. Clone the repository:
```bash
git clone [https://github.com/binhuang15/ACLFapp.git](https://github.com/binhuang15/ACLFapp.git)
cd ACLFapp
```
### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
No command-line arguments are needed. All settings are configured directly within the `ACLFAppUpdated.py` file.

### Step 1: Configure Input Mode
Open `ACLFAppUpdated.py` and find the `USER CONFIGURATION` section at the top:
```python
# Select Input Mode: set to 'csv' or 'manual'
INPUT_MODE = 'csv'
```
### Step 2: Set Data Parameters
#### Option A: Using CSV File (`INPUT_MODE = 'csv'`)
Specify the file path and the row index (1-based) you wish to predict.
```python
CSV_FILE_PATH = 'ACLF_TEST_COHORT.csv'
CSV_ROW_INDEX = 45  # Change this index to test different patients
```
#### Option B: Manual Entry (`INPUT_MODE = 'manual'`)
Input specific clinical values manually in the dictionary:
```python
MANUAL_VALUES = {
    'TB': 351.2,   # Total Bilirubin (umol/L)
    'Na': 139,     # Sodium (mmol/L)
    'PLT': 127,    # Platelets
    'INR': 1.56,   # INR
    'SWE': 39.7    # 2D-SWE (kPa)
}
```
### Step 3: Run the Script
```bash
python ACLFAppUpdated.py
```

## Output Example
```Plaintext
--- Processing CSV Mode (File: ACLF_TEST_COHORT.csv, Row: 45) ---
Data loaded: [[351.2 139.  127.    1.56  39.7]]

--- Prediction Results ---
Risk Factor (One Month)   : 85%
Risk Factor (Three Months): 72%
Risk Factor (One Year)    : 64%
```

## License
MIT License
