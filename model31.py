""" Dataset containing daily temperature data for a specific city. The temperature vector T, which stands for the dataset, has n observations that represent the daily temperatures over a specific time period.
 a) Determine the daily temperature changes, represented by the vector D.
 b) Use box plots to visualize the distribution of the daily temperature changes and to identify and quantify any outliers based on the interquartile range (IQR) method.
 c) Discuss the potential impact of outliers on weather forecasting and analysis.
Consider factors such as prediction accuracy, climate trend analysis, and the reliability of statistical measures in the presence of outliers.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Daily temperature (in degrees Celsius) for a specific city over 30 days
np.random.seed(0)  # For reproducibility
T = np.random.normal(loc=20, scale=5, size=30)  # Simulating daily temperatures

# Create DataFrame
df = pd.DataFrame({'Temperature': T})

# a) Determine the daily temperature changes, represented by the vector D
df['TempChange'] = df['Temperature'].diff()

# Drop the first row since it will have NaN for the first difference
df = df.dropna()

# b) Use box plots to visualize the distribution of the daily temperature changes and identify outliers using the IQR method
plt.figure(figsize=(10, 6))

# Boxplot for daily temperature changes
sns.boxplot(y=df['TempChange'])
plt.title('Boxplot of Daily Temperature Changes')
plt.ylabel('Temperature Change (°C)')
plt.show()

# Calculate IQR and identify outliers
Q1 = df['TempChange'].quantile(0.25)
Q3 = df['TempChange'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['TempChange'] < lower_bound) | (df['TempChange'] > upper_bound)]

print("Outliers based on IQR method:")
print(outliers)

# c) Discussion on the potential impact of outliers on weather forecasting and analysis

discussion = """
Outliers can significantly impact weather forecasting and analysis in several ways:

1. Prediction Accuracy: Outliers can skew the results of predictive models, leading to inaccurate forecasts. For instance, an unusually high or low temperature can affect the model's ability to learn the typical temperature patterns.

2. Climate Trend Analysis: Outliers can distort the understanding of climate trends. For example, a single day with an extreme temperature change might be mistaken for a trend rather than an anomaly.

3. Reliability of Statistical Measures: Outliers can affect the reliability of statistical measures such as mean and standard deviation. In the presence of outliers, the mean temperature change might not represent the central tendency accurately, and the standard deviation might be inflated, suggesting higher variability than actually exists.

To mitigate the impact of outliers, it's important to:
- Identify and analyze the causes of outliers (e.g., data entry errors, unusual weather events).
- Use robust statistical methods that are less sensitive to outliers, such as median and interquartile range.
- Consider excluding outliers from the dataset if they are determined to be erroneous or irrelevant to the analysis.

Overall, while outliers provide valuable information about extreme events, they need to be handled carefully to ensure accurate weather forecasting and analysis.
"""

print(discussion)
