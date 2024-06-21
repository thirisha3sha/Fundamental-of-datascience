"""Scenario: You are a data scientist working for a company that sells products online. You have been tasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame.
Question: How would you find the top 5 products that have been sold the most in the past month?
 
 
"""
import pandas as pd

# Sample sales data for the past month
data = {
    'ProductID': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 1, 2, 3, 4, 5, 1, 2, 3],
    'ProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E',
                    'Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E',
                    'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C',
                    'Product_D', 'Product_E', 'Product_A', 'Product_B', 'Product_C'],
    'QuantitySold': [10, 15, 10, 5, 20, 10, 5, 20, 10, 5, 25, 10, 15, 10, 5, 25, 10, 5, 20, 10]
}

# Create DataFrame
df = pd.DataFrame(data)

# Group by ProductID and ProductName to sum the quantities sold
grouped_df = df.groupby(['ProductID', 'ProductName']).sum().reset_index()

# Sort the products by the total quantities sold in descending order
sorted_df = grouped_df.sort_values(by='QuantitySold', ascending=False)

# Select the top 5 products
top_5_products = sorted_df.head(5)

# Display the top 5 products
print("Top 5 Products Sold in the Past Month:")
print(top_5_products)
