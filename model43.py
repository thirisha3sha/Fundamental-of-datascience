"""You are working on a data visualization project for a fitness tracker company. The company has collected data on the number of steps taken by users each month. Your task is to develop a Python program that generates line plots and bar plots to visualize the monthly step count data.
Question:How would you develop a Python program to create a line plot of the monthly step count data? How would you develop a Python program to create a bar plot of the monthly step count data?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample monthly step count data (mock data)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    'Step_Count': [100000, 110000, 105000, 115000, 120000, 125000, 130000, 135000, 140000, 145000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame (optional)
print(df)

# Line Plot: Monthly step count trend
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Step_Count'], marker='o', linestyle='-', color='b', label='Monthly Step Count')
plt.title('Monthly Step Count Trend')
plt.xlabel('Month')
plt.ylabel('Step Count')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Bar Plot: Total step counts by month
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Step_Count'], color='g', alpha=0.7)
plt.title('Total Monthly Step Counts')
plt.xlabel('Month')
plt.ylabel('Total Step Count')
plt.grid(True)
plt.tight_layout()
plt.show()
