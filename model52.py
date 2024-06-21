"""Scenario: You are a data analyst working for a company that sells products online. You
have been tasked with analyzing the sales data for the past month. The data is stored in a
NumPy array.
Question: How would you find the average price of all the products sold in the past month?
Assume 3x3 matrix with each row representing the sales for a different product"""
import numpy as np

# Sample data: sales data for the past month
# Each row represents the sales for a different product
# Columns could represent sales on different days/weeks of the month
sales_data = np.array([
    [150, 200, 250],
    [300, 350, 400],
    [500, 450, 550]
])

# Calculate the average price of all the products sold
average_price = np.mean(sales_data)

# Output the result
print(f"The average price of all the products sold in the past month is {average_price:.2f}")
