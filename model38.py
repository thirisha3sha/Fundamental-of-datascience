""" Scenario: A public health organization wants to investigate the relationship between air pollution levels and respiratory diseases in a city. They have collected data on the annual average concentration of air pollutants and the number of respiratory disease cases reported each year.
Task: Write a program to calculate the correlation coefficient between air pollution levels and respiratory disease cases, and create a scatter plot of the data using the following mock dataset:
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock data
data = {
    'air_pollution_levels': [10, 20, 15, 25, 30, 35, 40, 45, 50, 55],
    'respiratory_disease_cases': [15, 25, 20, 30, 35, 40, 45, 50, 55, 60]
}

# Create a dataframe
df = pd.DataFrame(data)

# Calculate correlation coefficient
corr_coef = np.corrcoef(df['air_pollution_levels'], df['respiratory_disease_cases'])[0, 1]

print(f'Correlation Coefficient: {corr_coef:.2f}')

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['air_pollution_levels'], df['respiratory_disease_cases'], color='b', marker='o', alpha=0.7)
plt.title('Relationship between Air Pollution Levels and Respiratory Disease Cases')
plt.xlabel('Air Pollution Levels')
plt.ylabel('Respiratory Disease Cases')
plt.grid(True)
plt.tight_layout()
plt.show()
