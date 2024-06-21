"""Scenario: You are working on a data visualization project and need to create basic plots
using Matplotlib. You have a dataset containing the monthly sales data for a company, including the month and corresponding sales values. Your task is to develop a Python
program that generates line plots and bar plots to visualize the sales data.
Question:
1. How would you develop a Python program to create a line plot of the monthly
sales data?

2: How would you develop a Python program to create a bar plot of the monthly
sales data?

"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: monthly sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the month as the index
df.set_index('Month', inplace=True)

# Plot the data
plt.figure(figsize=(14, 8))

# Line plot
plt.subplot(2, 1, 1)
plt.plot(df.index, df['Sales'], marker='o', linestyle='-', color='b', label='Sales')
plt.title('Line Plot: Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)

# Bar plot
plt.subplot(2, 1, 2)
plt.bar(df.index, df['Sales'], color='skyblue', label='Sales')
plt.title('Bar Plot: Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y')

plt.tight_layout()
plt.show()
