"""You are a data analyst working for a company that sells products online. You have been tasked with analyzing the sales data for the past month. The data is stored in a NumPy array.
Question: How would you find the average price of all the products sold in the past month? Assume 3x3 matrix with each row representing the sales for a different product
"""
import numpy as np
sales_data=np.array([
    [150,300,234],
    [345,200,566],
    [200,566,344]
    ])
avg_price=sales_data.mean()
print("sales data:\n",sales_data)
print(f"\n The avg price of all products sold in the past month is {avg_price:.3f}")
      
