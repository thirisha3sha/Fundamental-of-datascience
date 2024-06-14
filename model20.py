"""Scenario: You are investigating a dataset representing the daily temperatures in a city. Calculate the variance and identify potential outliers that may indicate unusual weather conditions.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate sample data: Daily temperatures (replace with actual data)
dates = pd.date_range(start='2023-01-01', periods=30)  # 30 days of data
temperatures = np.concatenate([
    np.random.normal(loc=20, scale=5, size=25),  # Normal days
    np.random.normal(loc=35, scale=2, size=5)    # Potential hot days (outliers)
])

# Ensure lengths match
if len(dates) != len(temperatures):
    raise ValueError("Dates and temperatures arrays must have the same length")

# Create DataFrame
df_temperatures = pd.DataFrame({
    'Date': dates,
    'Temperature': temperatures
})

# Calculate variance
temperature_variance = np.var(df_temperatures['Temperature'], ddof=0)  # Population variance
print(f"Variance of Daily Temperatures: {temperature_variance:.2f}")

# Identify potential outliers using z-score
z_scores = np.abs(stats.zscore(df_temperatures['Temperature']))
threshold = 2.5  # Z-score threshold for outlier detection

# Filter outliers
outliers = df_temperatures[z_scores > threshold]

# Plot temperatures with potential outliers highlighted
plt.figure(figsize=(10, 6))
plt.plot(df_temperatures['Date'], df_temperatures['Temperature'], marker='o', linestyle='-', color='b', label='Daily Temperatures')
plt.scatter(outliers['Date'], outliers['Temperature'], color='r', label='Potential Outliers')
plt.title('Daily Temperatures with Potential Outliers')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nPotential Outliers:")
print(outliers)
