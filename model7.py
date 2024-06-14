"""Scenario: You are a data analyst working for a company that manufactures electronics. You have been tasked with analyzing the sales data for the past month. The data is stored in a NumPy array.
	Question: How would you find the average revenue from all the products sold in the past month? Assume a 4x4 matrix with each row representing the sales for a different product.
"""
import numpy as np
sales_data = np.array([
    [1000, 1200, 800, 950],
    [1500, 1100, 1300, 900],
    [1600, 1400, 900, 1100],
    [1800, 1700, 950, 1200]
])
print("\n Dataset preview:\n",sales_data)
average_revenue = np.mean(sales_data)
print(f"The average revenue from all products sold in the past month is: ${average_revenue:.2f}")
