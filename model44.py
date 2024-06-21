"""	Scenario: You are working on a project that involves analyzing the sales performance of a company over the past four quarters. The quarterly sales data is stored in a NumPy array named sales_data, where each element represents the sales amount for a specific quarter. Your task is to calculate the total sales for the year and determine the percentage increase in sales from the first quarter to the fourth quarter.
Question: Using NumPy arrays and arithmetic operations calculate the total sales for the year and determine the percentage increase in sales from the first quarter to the fourth quarter?
"""
import numpy as np
import pandas as pd

# Sample quarterly sales data (mock data)
sales_data = np.array([50000, 60000, 70000, 80000])

# Calculate total sales for the year
total_sales = np.sum(sales_data)

# Determine percentage increase from Q1 to Q4
sales_q1 = sales_data[0]
sales_q4 = sales_data[-1]
percentage_increase = ((sales_q4 - sales_q1) / sales_q1) * 100

# Print results
print(f'Total sales for the year: ${total_sales}')
print(f'Percentage increase from Q1 to Q4: {percentage_increase:.2f}%')
