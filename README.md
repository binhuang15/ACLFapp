ACLF Risk Prediction SystemThis repository contains a Python-based tool for predicting the risk factors of Acute-on-Chronic Liver Failure (ACLF) over different time horizons (1 month, 3 months, and 1 year).The system utilizes pre-trained machine learning models to analyze clinical biomarkers including Total Bilirubin (TB), Sodium (Na), Platelets (PLT), INR, and 2D-Shear Wave Elastography (SWE).📂 Project Structure.
├── main.py                # Main execution script
├── requirements.txt       # Python dependencies
├── Model_1.pkl            # Pre-trained model (1 Month)
├── Model_2.pkl            # Pre-trained model (3 Months)
├── Model_3.pkl            # Pre-trained model (1 Year)
└── ACLF_TEST_COHORT.csv   # Example dataset (optional)
⚙️ Prerequisites & InstallationCrucial: The models were trained using scikit-learn v1.2.2. Using a newer version (v1.3+) will cause a ValueError regarding incompatible dtypes.Clone the repository:git clone [https://github.com/YourUsername/Your-Repo-Name.git](https://github.com/YourUsername/Your-Repo-Name.git)
cd Your-Repo-Name
Install dependencies:pip install -r requirements.txt
For users in China (Tsinghua Mirror):To ensure fast and successful installation, use the Tsinghua mirror:pip install -r requirements.txt -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)
🚀 UsageNo command-line arguments are needed. All settings are configured directly within the main.py file.Step 1: Configure Input ModeOpen main.py and find the USER CONFIGURATION section at the top:# Select Input Mode: set to 'csv' or 'manual'
INPUT_MODE = 'csv' 
Step 2: Set Data ParametersOption A: Using CSV File (INPUT_MODE = 'csv')Specify the file path and the row index (0-based) you wish to predict.CSV_FILE_PATH = 'ACLF_TEST_COHORT.csv'
CSV_ROW_INDEX = 45  # Change this index to test different patients
Option B: Manual Entry (INPUT_MODE = 'manual')Input specific clinical values manually in the dictionary:MANUAL_VALUES = {
    'TB': 351.2,   # Total Bilirubin (umol/L)
    'Na': 139,     # Sodium (mmol/L)
    'PLT': 127,    # Platelets
    'INR': 1.56,   # INR
    'SWE': 39.7    # 2D-SWE (kPa)
}
Step 3: Run the Scriptpython main.py
📊 Output Example--- Processing CSV Mode (File: ACLF_TEST_COHORT.csv, Row: 45) ---
Data loaded: [[351.2 139.  127.    1.56  39.7]]

--- Prediction Results ---
Risk Factor (One Month)   : 85%
Risk Factor (Three Months): 72%
Risk Factor (One Year)    : 64%
⚠️ TroubleshootingError: ValueError: node array from the pickle has an incompatible dtypeCause: Incompatibility between the scikit-learn version used for training and the one installed in your environment.Solution: Downgrade to the specific version listed in requirements.txt:pip install scikit-learn==1.2.2 -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)
📝 LicenseMIT License
