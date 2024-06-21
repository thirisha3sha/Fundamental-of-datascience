"""Scenario: You are working on a data analysis project that involves analyzing the monthly
temperature and rainfall data for a city. You have a dataset containing the monthly
temperature and rainfall values for each month of a year. Your task is to develop a Python
program that generates line plots and scatter plots to visualize the temperature and rainfall
data.
Question:
1. Develop a Python program to create a line plot of the monthly temperature data.
2: Develop a Python program to create a scatter plot of the monthly rainfall data."""
import matplotlib.pyplot as plt
import pandas as pd

# Sample data for monthly temperature and rainfall
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [30, 32, 35, 40, 45, 50, 55, 53, 48, 40, 35, 30],  # Example temperatures
    'Rainfall': [2.1, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 4.8, 4.2, 3.5, 3.0, 2.5]  # Example rainfall in inches
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the 'Month' column as the index for better plotting
df.set_index('Month', inplace=True)

# Line Plot for Temperature
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)  # Rotate month names for better readability
plt.show()

# Scatter Plot for Rainfall
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['Rainfall'], color='r')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (inches)')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)  # Rotate month names for better readability
plt.show()
