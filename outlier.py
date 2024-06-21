import pandas as pd
import numpy as np

# Create a DataFrame
data = pd.DataFrame({'A': [1, 2, 3, 4, 5, 100]})

# Calculate the first quartile (Q1)
Q1 = np.percentile(data['A'], 25)

# Calculate the third quartile (Q3)
Q3 = np.percentile(data['A'], 75)

# Calculate the interquartile range (IQR)
IQR = Q3 - Q1

# Calculate the lower fence
lower_fence = Q1 - 1.5 * IQR

# Calculate the upper fence
upper_fence = Q3 + 1.5 * IQR

# Identify outliers
outliers = data[(data['A'] < lower_fence) | (data['A'] > upper_fence)]
print(outliers)

# Remove outliers
data = data[~(data['A'].isin(outliers['A']))]

# Print the DataFrame
print(data)
