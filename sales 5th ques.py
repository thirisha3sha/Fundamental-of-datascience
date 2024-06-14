"""Scenario: You are working on a data visualization project and need to create basic plots
using Matplotlib. You have a dataset containing the monthly sales data for a company, including the month and corresponding sales values. Your task is to develop a Python
program that generates line plots and bar plots to visualize the sales data.
Question:
1. How would you develop a Python program to create a line plot of the monthly
sales data?

2: How would you develop a Python program to create a bar plot of the monthly
sales data?"""
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a DataFrame with the monthly sales data
sales_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [1000, 1200, 1300, 900, 1100, 1150, 1050, 1250, 1400, 1350, 1500, 1600]
}
df = pd.DataFrame(sales_data)

# Step 2: Create plots for the monthly sales data

plt.figure(figsize=(14, 6))

# Line plot for monthly sales data
plt.subplot(1, 2, 1)
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)

# Bar plot for monthly sales data
plt.subplot(1, 2, 2)
plt.bar(df['Month'], df['Sales'], color='g')
plt.title('Monthly Sales Data (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
