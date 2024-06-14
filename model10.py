"""You are working with an e-commerce company that has collected data on the purchase amounts made by customers over the past month. The dataset includes the purchase amounts (in dollars) for each transaction. Utilize measures of central tendency to answer the following questions:
·       Calculate the mean (average) purchase amount to understand the typical spending behavior of customers.
·       Identify the mode of the purchase amounts to find the most frequently occurring purchase amount, helping the company understand popular spending levels
"""
import pandas as pd
import numpy as np
purchase_data = {
    'purchase_id':list(range(100,123))[:20],
    'Purchase Amount': [50, 30, 80, 50, 100, 80, 60, 50, 30, 50, 40, 60, 70, 80, 90, 60, 80, 50, 60, 70]
}
df = pd.DataFrame(purchase_data)
print("sales data:\n",df)
mean_purchase_amount = np.mean(df['Purchase Amount'])
mode_purchase_amount = df['Purchase Amount'].mode()[0]
print(f"The mean purchase amount is: ${mean_purchase_amount:.2f}")
print(f"The mode of purchase amounts is: ${mode_purchase_amount}")
