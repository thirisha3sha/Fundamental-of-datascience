""".Scenario: You are working on a data analysis project that involves analyzing the monthly temperature and rainfall data for a city.
You have a dataset containing the monthly temperature and rainfall values for each month of a year. Your task is to develop a Python program that
generates line plots and scatter plots to visualize the temperature and rainfall Data."""
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a DataFrame with monthly temperature and rainfall data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [30.5, 32.0, 35.1, 38.2, 40.3, 42.5, 45.0, 44.5, 40.0, 35.2, 32.1, 30.0],
    'Rainfall': [2.5, 2.0, 3.0, 3.5, 4.0, 5.0, 6.0, 5.5, 4.0, 3.5, 2.5, 2.0]
}
df = pd.DataFrame(data)

# Step 2: Generate line plots for temperature and rainfall
plt.figure(figsize=(14, 6))

# Line plot for Temperature
plt.subplot(1, 2, 1)
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)

# Line plot for Rainfall
plt.subplot(1, 2, 2)
plt.plot(df['Month'], df['Rainfall'], marker='o', linestyle='-', color='g')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (inches)')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

# Step 3: Generate scatter plots for temperature and rainfall
plt.figure(figsize=(14, 6))

# Scatter plot for Temperature
plt.subplot(1, 2, 1)
plt.scatter(df['Month'], df['Temperature'], color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)

# Scatter plot for Rainfall
plt.subplot(1, 2, 2)
plt.scatter(df['Month'], df['Rainfall'], color='g')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (inches)')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


