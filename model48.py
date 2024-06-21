"""Scenario: You are working on a data visualization project and need to create basic plots using Matplotlib. You have a dataset containing the monthly sales data for a company, including the month and corresponding sales values. Your task is to develop a Python program that generates line plots and bar plots to visualize the sales data.
Question:  How would you develop a Python program to create a line plot of the monthly sales data?How would you develop a Python program to create a bar plot of the monthly sales data?
"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample monthly sales data (mock data)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [35000, 42000, 39000, 41000, 38000, 45000, 48000, 50000, 49000, 51000, 48000, 52000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame (optional)
print("Monthly Sales Data:")
print(df)
print()

# Generate a line plot for monthly sales data
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Generate a bar plot for monthly sales data
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='skyblue', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.legend()
plt.tight_layout()
plt.show()
