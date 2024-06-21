""" calculate the variance of monthly rainfall in a region's dataset and identify potential outliers that may indicate unusual weather patterns using NumPy, given the following data?
 
DATASET: 20, 22, 24, 26, 28, 30, 32, 34, 36, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70
"""
import numpy as np
import pandas as pd 

# Define the dataset
rainfall_data = [20, 22, 24, 26, 28, 30, 32, 34, 36, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70]

# Create a DataFrame
df = pd.DataFrame(rainfall_data, columns=['Monthly Rainfall'])

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the variance
variance = np.var(df['Monthly Rainfall'], ddof=1)
print(f"\nVariance of monthly rainfall: {variance}")

# Identify potential outliers using the IQR method
Q1 = df['Monthly Rainfall'].quantile(0.25)
Q3 = df['Monthly Rainfall'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Monthly Rainfall'] < lower_bound) | (df['Monthly Rainfall'] > upper_bound)]

print("\nPotential outliers:")
if outliers.empty:
    print("None")
else:
    print(outliers)
    print("\nOutlier values:")
    print(outliers['Monthly Rainfall'].values)

# Printing the bounds for reference
print(f"\nLower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")
