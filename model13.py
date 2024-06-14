"""Scenario: You are a financial analyst working with an investment portfolio. You need to calculate the total value of investments after applying fees and taxes. You have the following data:
·                  List of investment values in USD.
·                  Fee rate as a percentage of the total investment value.
·                  Tax rate as a percentage applied to the net investment value after deducting fees.
Question: Use arithmetic operations to calculate the net value of investments after deducting fees and applying taxes, given the investment values, fee rate, and tax rate?
"""
import pandas as pd
fee_rate = 1.5  # Fee rate as a percentage (1.5%)
tax_rate = 15  # Tax rate as a percentage (15%)

data = {
    'Investment Value (USD)':[10000, 15000, 12000, 18000] 
}

df = pd.DataFrame(data)

# Calculate total fee deduction
df['Fee Deduction'] = df['Investment Value (USD)'] * (fee_rate / 100)

# Calculate net investment value after deducting fees
df['Net Investment Value'] = df['Investment Value (USD)'] - df['Fee Deduction']

# Calculate total tax deduction based on the net investment value
df['Tax Deduction'] = df['Net Investment Value'] * (tax_rate / 100)

# Calculate final net value of investments after deducting fees and applying taxes
df['Final Net Value'] = df['Net Investment Value'] - df['Tax Deduction']

# Display the DataFrame with calculated columns
print("DataFrame with Calculations:")
print(df)

# Summarize total net value of investments after fees and taxes
total_net_value = df['Final Net Value'].sum()
print(f"\nTotal Net Value of Investments after Fees and Taxes: ${total_net_value:.2f}")
