"""	Scenario: You are a data analyst at a retail chain tasked with analyzing customer transaction data to optimize pricing strategies. The dataset includes purchase amounts (in dollars) from customer transactions over the past month.
Questions:Calculate the mean (average) purchase amount to determine the typical transaction size and average spending behavior of customers.
Identify the mode of the purchase amounts to pinpoint the most frequently occurring transaction amount, aiding in understanding popular spending levels among customers.
:"""
import pandas as pd
import numpy as np

# Sample data: Purchase amounts (in dollars) from customer transactions over the past month
data = {
    'PurchaseAmount': [50, 75, 20, 20, 35, 40, 100, 20, 75, 50, 60, 50, 30, 80, 75, 100, 25, 50, 40, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the mean (average) purchase amount
mean_purchase_amount = df['PurchaseAmount'].mean()
print(f"Mean (Average) Purchase Amount: ${mean_purchase_amount:.2f}")

# Calculate the mode (most frequently occurring) purchase amount
mode_purchase_amount = df['PurchaseAmount'].mode()
if len(mode_purchase_amount) == 1:
    print(f"Mode (Most Frequent) Purchase Amount: ${mode_purchase_amount[0]}")
else:
    print(f"Mode (Most Frequent) Purchase Amounts: {list(mode_purchase_amount)}")

# Display the DataFrame
print("\nDataFrame with Purchase Amounts:")
print(df)
