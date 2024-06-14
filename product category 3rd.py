"""You work as a data analyst for a large e-commerce company that sells a variety of products online.
Your company has collected sales data over the past year and wants to analyze and visualize this data to gain insights into sales trends, product performance,
and customer behavior. To understand which product categories are most popular, create line, scatter and bar plot that displays the distribution of sales across
different product categories.
Each plot has to represents a category, and the height of the bar indicates the total sales"""      

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a DataFrame with sales data
data = {
    'ProductID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'ProductCategory': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing', 'Toys', 'Toys', 'Books', 'Books'],
    'Sales': [200, 150, 300, 250, 100, 120, 90, 110, 80, 70]
}
df = pd.DataFrame(data)

# Step 2: Group the data by product category and calculate the total sales for each category
grouped_df = df.groupby('ProductCategory')['Sales'].sum().reset_index()

# Step 3: Create line, scatter, and bar plots to visualize the distribution of sales

# Line plot
plt.figure(figsize=(10, 5))
plt.plot(grouped_df['ProductCategory'], grouped_df['Sales'], marker='o', linestyle='-')
plt.title('Total Sales by Product Category (Line Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(grouped_df['ProductCategory'], grouped_df['Sales'], color='r')
plt.title('Total Sales by Product Category (Scatter Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(10, 5))
plt.bar(grouped_df['ProductCategory'], grouped_df['Sales'], color='g')
plt.title('Total Sales by Product Category (Bar Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()
