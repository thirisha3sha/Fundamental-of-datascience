"""Scenario: You are working on a data analysis project that involves analyzing the monthly temperature and rainfall data for a city. You have a dataset containing the monthly temperature and rainfall values for each month of a year. Your task is to develop a Python program that generates line plots and scatter plots to visualize the temperature and rainfall Data.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: monthly temperature (in Celsius) and rainfall (in mm) for a city
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [5, 6, 9, 13, 18, 21, 25, 24, 20, 14, 9, 6],
    'Rainfall': [50, 40, 45, 60, 70, 80, 90, 85, 75, 65, 55, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the month as the index
df.set_index('Month', inplace=True)

# Plot the data
plt.figure(figsize=(14, 8))

# Line plot
plt.subplot(2, 1, 1)
plt.plot(df.index, df['Temperature'], marker='o', label='Temperature', color='tab:blue')
plt.plot(df.index, df['Rainfall'], marker='s', label='Rainfall', color='tab:green')
plt.title('Line Plot: Monthly Temperature and Rainfall')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend()

# Scatter plot
plt.subplot(2, 1, 2)
plt.scatter(df.index, df['Temperature'], label='Temperature', color='tab:blue')
plt.scatter(df.index, df['Rainfall'], label='Rainfall', color='tab:green')
plt.title('Scatter Plot: Monthly Temperature and Rainfall')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()
