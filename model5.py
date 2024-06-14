"""Scenario: In a medical study, you have collected data on patients' recovery times after a procedure. Calculate the 10th, 50th, and 90th percentiles to understand the distribution of recovery times."""
import pandas as pd
import numpy as np
data={
    'patient_id':list(range(1,21)),
    'recovery_time':[10, 12, 15, 14, 17, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    }
df=pd.DataFrame(data)
print("\n dataset:\n",df)
p10=np.percentile(df['recovery_time'],10)
p50=np.percentile(df['recovery_time'],50)
p90=np.percentile(df['recovery_time'],90)
print("\n 10th percentile:",p10)
print("\n 50th percentile:",p50)
print("\n 90th percentile:",p90)
