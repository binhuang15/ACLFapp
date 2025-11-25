# ACLF Deterioration Risk Prediction Model

This repository contains a Python-based tool for predicting the risk factors of Acute-on-Chronic Liver Failure (ACLF) over different time horizons (1 month, 3 months, and 1 year).

**Intended use:** Prognostic prediction of 30-day, 90-day, and 1-year outcomes (deterioration risk) for ACLF patients.

**Inputs:** Five clinical/imaging features (total bilirubin [TB, μmol/L], international normalized ratio [INR], sodium [Na, mmol/L], platelet count [PLT, ×10⁹/L], 2D shear wave elastography [2D-SWE, kPa]).

**Outputs:** Probability of deterioration (range: 0–1) for each time point. If the predicted probability was less than or equal to 22.7%, 44.2% or 45.6%, the patients were predicted to recover within 30 days, 90 days or 1 year. If Serum-SWE-ML value was greater than 22.7%, 44.2% or 45.6%, the patients’ condition was expected to deteriorate at corresponding time point.

**Limits:** Predictive performance may vary in populations with extreme feature values or baseline characteristics differing from the study cohort; short-term (30-day) prediction exhibits relatively lower calibration compared to 90-day and 1-year predictions.


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
git clone https://github.com/binhuang15/ACLFapp.git
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
