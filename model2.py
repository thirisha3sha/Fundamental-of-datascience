"""A clinic wants to know the most common health issues among their patients. They have a list of all the  health issues that their patients have been diagnosed with in the past year, along with the number of patients who have been diagnosed with each issue.
 Question: Write a program that will calculate the frequency distribution of health issues and print out the most common health issue using the following dataset:

DISEASE_NAME  DIAGNOSED_PATIENTS
Hypertension      250
Asthma           180
Depression         160
Arthritis        140
Migraine           80"""
import pandas as pd
data = {
    'disease_name': ['Hypertension', 'Asthma', 'Depression', 'Arthritis', 'Migraine'],
    'diagnosed_patients': [250, 180, 160, 140, 80]
}
df=pd.DataFrame(data)
print("dataset:\n",df)
most_common_issue=df.loc[df['diagnosed_patients'].idxmax()]
print("\n most common health issue:")
print(f"Disease:{most_common_issue['disease_name']}  diagnosed patients:{most_common_issue['diagnosed_patients']}")


