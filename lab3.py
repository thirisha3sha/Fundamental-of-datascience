"""Scenario: In a medical study, you have collected data on patients' recovery times after a procedure. Calculate the
10th, 50th, and 90th percentiles to understand the distribution of recovery times.write python code
and sample  output"""
import numpy as np
import pandas as pd
data={
    'patient_id':list(range(102,115)),
    'recovery_time':[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    }
df=pd.DataFrame(data)
p10=np.percentile(df['recovery_time'],10)
p50=np.percentile(df['recovery_time'],50)
p90=np.percentile(df['recovery_time'],90)
print("10th percentile:",p10)
print("50th percentile:",p50)
print("90th percentile:",p90)
