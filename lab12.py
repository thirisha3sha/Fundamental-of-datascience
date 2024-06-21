"""You work as a data analyst for a large e-commerce company that sells a variety of products online. Your company has collected sales data over the past year and wants to analyze and visualize this data to gain insights into sales trends, product performance, and customer behavior. To understand which product categories are most popular, create line, scatter and bar plot that displays the distribution of sales across different product categories. Each plot has to represents a category, and the height of the bar indicates the total sales
"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: sales data for different product categories
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Electronics': [2000, 2200, 2500, 2300, 2400, 2600, 2700, 2900, 3000, 3100, 3200, 3300],
    'Clothing': [1500, 1600, 1700, 1650, 1800, 1750, 1900, 2000, 2100, 2200, 2250, 2300],
    'Books': [1000, 1100, 1200, 1150, 1300, 1250, 1350, 1400, 1500, 1550, 1600, 1650],
    'Furniture': [800, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the month as the index
df.set_index('Month', inplace=True)

# Plot the data
plt.figure(figsize=(14, 8))

# Line plot
plt.subplot(3, 1, 1)
for category in df.columns:
    plt.plot(df.index, df[category], marker='o', label=category)
plt.title('Line Plot: Sales Distribution Across Product Categories')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend()

# Scatter plot
plt.subplot(3, 1, 2)
for category in df.columns:
    plt.scatter(df.index, df[category], label=category)
plt.title('Scatter Plot: Sales Distribution Across Product Categories')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend()

# Bar plot
plt.subplot(3, 1, 3)
bar_width = 0.2
index = range(len(df.index))
for i, category in enumerate(df.columns):
    plt.bar([p + bar_width*i for p in index], df[category], width=bar_width, label=category)
plt.title('Bar Plot: Sales Distribution Across Product Categories')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks([p + 1.5 * bar_width for p in index], df.index)
plt.legend()

plt.tight_layout()
plt.show()
