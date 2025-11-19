# ACLF Risk Prediction System

This repository contains a Python-based tool for predicting the risk factors of Acute-on-Chronic Liver Failure (ACLF) over different time horizons (1 month, 3 months, and 1 year). 

The system utilizes pre-trained machine learning models to analyze clinical biomarkers including Total Bilirubin (TB), Sodium (Na), Platelets (PLT), INR, and 2D-Shear Wave Elastography (SWE).

## 📂 Project Structure

```text
.
├── main.py                # Main execution script
├── requirements.txt       # Python dependencies
├── Model_1.pkl            # Pre-trained model (1 Month)
├── Model_2.pkl            # Pre-trained model (3 Months)
├── Model_3.pkl            # Pre-trained model (1 Year)
└── ACLF_TEST_COHORT.csv   # Example dataset (optional)
