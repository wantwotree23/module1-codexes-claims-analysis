import pandas as pd

df = pd.read_csv('inpatient.csv', sep='|')
print(df.columns.tolist())

icd_codes = df['ICD_DGNS_CD1']