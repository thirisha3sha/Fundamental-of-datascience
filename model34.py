"""Scenario: You are a financial analyst reviewing the daily returns of an investment portfolio over the past month.
Your task is to calculate the variance of the daily returns to assess the volatility and risk associated with the portfolio.:::"""
import pandas as pd
import numpy as np

# Step 1: Create a sample dataframe of daily returns
# Let's create a sample dataframe with hypothetical daily returns
dates = pd.date_range(start='2024-05-01', periods=30, freq='B')  # Business days for a month
np.random.seed(0)  # For reproducibility
daily_returns = np.random.normal(loc=0.001, scale=0.02, size=len(dates))  # Normal distribution of returns
df = pd.DataFrame({'Date': dates, 'Daily_Return': daily_returns})

# Step 2: Calculate the variance of daily returns
variance_daily_returns = np.var(df['Daily_Return'], ddof=1)  # ddof=1 for sample variance

print(f"Variance of daily returns: {variance_daily_returns:.6f}")
