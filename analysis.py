import pandas as pd

df = pd.read_csv('inpatient.csv', sep='|')
print(df.columns.tolist())

icd_dgns_codes = df['ICD_DGNS_CD1']
icd_dgns_e_codes = df['ICD_DGNS_E_CD1']
icd_prcdr_codes = df['ICD_PRCDR_CD1']
drg_codes = df['CLM_DRG_CD']
hcpcs_codes = df['HCPCS_CD']
op_npi_codes = df['OP_PHYSN_NPI']
nch_type_codes = df['NCH_CLM_TYPE_CD']
service_type_codes = df['CLM_SRVC_CLSFCTN_TYPE_CD']

icd_dgns_frequency = icd_dgns_codes.value_counts()
print("ICD Diagnostic Codes Frequency:\n", icd_dgns_frequency)
icd_dgns_e_frequency = icd_dgns_e_codes.value_counts()
print("ICD Diagnostic E Codes Frequency:\n", icd_dgns_e_frequency)
icd_prcdr_frequency = icd_prcdr_codes.value_counts()
print("ICD Procedure Codes Frequency:\n", icd_prcdr_frequency)
drg_frequency = drg_codes.value_counts()
print("Claim DRG Codes Frequency:\n", drg_frequency)
hcpcs_frequency = hcpcs_codes.value_counts()
print("HCPCS Codes Frequency:\n", hcpcs_frequency)
op_npi_frequency = op_npi_codes.value_counts()
print("OP Physician NPI Codes Frequency:\n", op_npi_frequency)
nch_type_frequency = nch_type_codes.value_counts()
print("NCH Claim Type Codes Frequency:\n", nch_type_frequency)
service_type_frequency = service_type_codes.value_counts()
print("Claim Service Classification Type Codes Frequency:\n", service_type_frequency)

missing_icd_dgns = icd_dgns_codes.isnull().sum()
print(f"Missing ICD Diagnostic Codes: {missing_icd_dgns}")
missing_icd_dgns_e = icd_dgns_e_codes.isnull().sum()
print(f"Missing ICD Diagnostic E Codes: {missing_icd_dgns_e}")
missing_icd_prcdr = icd_prcdr_codes.isnull().sum()
print(f"Missing ICD Procedure Codes: {missing_icd_prcdr}")
missing_drg = drg_codes.isnull().sum()
print(f"Missing Claim DRG Codes: {missing_drg}")
missing_hcpcs = hcpcs_codes.isnull().sum()
print(f"Missing HCPCS Codes: {missing_hcpcs}")
missing_op_npi = op_npi_codes.isnull().sum()
print(f"Missing OP Physician NPI Codes: {missing_op_npi}")
missing_nch_type = nch_type_codes.isnull().sum()
print(f"Missing NCH Claim Type Codes: {missing_nch_type}")
missing_service_type = service_type_codes.isnull().sum()
print(f"Missing Claim Service Classification Type Codes: {missing_service_type}")

df['ICD_DGNS_CD1'].fillna('MISSING', inplace=True)
df['ICD_DGNS_E_CD1'].fillna('MISSING', inplace=True)
df['ICD_PRCDR_CD1'].fillna('MISSING', inplace=True)
df['CLM_DRG_CD'].fillna('MISSING', inplace=True)
df['HCPCS_CD'].fillna('MISSING', inplace=True)
df['OP_PHYSN_NPI'].fillna('MISSING', inplace=True)
df['NCH_CLM_TYPE_CD'].fillna('MISSING', inplace=True)
df['CLM_SRVC_CLSFCTN_TYPE_CD'].fillna('MISSING', inplace=True)

print("Top 5 Most Common ICD Diagnostic Codes:\n", icd_dgns_frequency.head())
print("Top 5 Most Common ICD Diagnostic E Codes:\n", icd_dgns_e_frequency.head())
print("Top 5 Most Common ICD Procedure Codes:\n", icd_prcdr_frequency.head())
print("Top 5 Most Common Claim DRG Codes:\n", drg_frequency.head()) 
print("Top 5 Most Common HCPCS Codes:\n", hcpcs_frequency.head())
print("Top 5 Most Common OP Physician NPI Codes:\n", op_npi_frequency.head())
print("Top 5 Most Common NCH Claim Type Codes:\n", nch_type_frequency.head())
print("Top 5 Most Common Claim Service Classification Type Codes:\n", service_type_frequency.head())

kidney_related = df[df['ICD_DGNS_CD1'].str.contains('Z940',na=False)]
common_procedures_kidney = kidney_related['ICD_PRCDR_CD1'].value_counts()
print("Common Procedures for Kidney Transplant Patients:\n", common_procedures_kidney.head())
common_hcpcs_kidney = kidney_related['HCPCS_CD'].value_counts()
print("Common HCPCS Codes for Kidney Transplant Patients:\n", common_hcpcs_kidney.head())
common_drg_kidney = kidney_related['CLM_DRG_CD'].value_counts()
print("Common DRG Codes for Kidney Transplant Patients:\n", common_drg_kidney.head())
