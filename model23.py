""""Scenario: You are a financial analyst at a credit card company analyzing transaction data to understand customer spending patterns. The dataset includes transaction amounts (in dollars) for each cardholder over the past month. Utilize measures of central tendency to answer the following questions:
Calculate the mean (average) transaction amount to assess the typical spending behavior of cardholders.
Identify the mode of the transaction amounts to determine the most frequently occurring spending level, aiding in understanding common transaction sizes.
"""
import pandas as pd
import numpy as np
from scipy import stats

# Create a synthetic dataset of transaction amounts
transaction_amounts = np.random.normal(100, 50, 1000).tolist()  # Normally distributed transaction amounts
transaction_amounts += [50] * 50  # Adding duplicate values to create a mode
transaction_amounts += [20, 20, 20, 30, 30, 30]  # Adding some specific amounts

# Create a DataFrame
df = pd.DataFrame(transaction_amounts, columns=['TransactionAmount'])

# Calculate the mean (average) transaction amount
mean_transaction_amount = df['TransactionAmount'].mean()
print(f"Mean (average) transaction amount: ${mean_transaction_amount:.2f}")

# Identify the mode of the transaction amounts
mode_transaction_amount = stats.mode(df['TransactionAmount'])[0][0]
print(f"Mode (most frequent) transaction amount: ${mode_transaction_amount:.2f}")

# Display the DataFrame
print("\nDataFrame:")
print(df.head(10))  # Display the first 10 rows of the DataFrame

