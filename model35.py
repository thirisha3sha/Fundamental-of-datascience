"""
5.     Scenario: You are a data scientist working for a company that sells products online. You have been tasked with analyzing the sales data for the past month.
The data is stored in a Pandas data frame.
Question: How would you find the top 5 products that have been sold the most in the past month?
 
"""
import pandas as pd
import numpy as np

# Step 1: Create a sample dataframe with product sales data
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product D', 'Product A', 'Product C', 'Product B', 'Product D'],
    'Sales': [50, 30, 20, 40, 25, 35, 45, 15, 60, 10]
}
df = pd.DataFrame(data)

# Step 2: Aggregate sales data by product
product_sales = df.groupby('Product')['Sales'].sum().reset_index()

# Step 3: Sort and select top 5 products with highest sales
top_5_products = product_sales.sort_values(by='Sales', ascending=False).head(5)

print("Top 5 products sold the most in the past month:")
print(top_5_products)
