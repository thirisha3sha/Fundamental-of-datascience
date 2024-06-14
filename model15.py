"""Scenario: You are working with a dataset representing the daily sales of a product over the past month. Calculate the variance of the daily sales to understand how much the sales figures deviate from the mean
"""
import pandas as pd
import numpy as np
date=list(pd.date_range(start='2023-01-01', end='2023-01-30', freq='D'))
# Create a DataFrame
data={
    'Date':date,
    'Daily Sales':[1000, 1200, 800, 1100, 1300, 900, 1000, 950, 1050, 1150, 
               1250, 1100, 1000, 1300, 1200, 1100, 1050, 1000, 950, 1150, 
               1250, 1100, 1000, 1300, 1200, 1100, 1050, 1000, 950, 1150][:30]
    }
df=pd.DataFrame(data)
print("sales data:\n",df)
# Calculate the variance of daily sales
sales_variance = np.var(df['Daily Sales'], ddof=0)  # ddof=0 for population variance
print(f"Variance of Daily Sales: {sales_variance:.2f}")
