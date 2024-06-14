"""SET 4
1. You are working as a financial analyst for a university. The university administration wants to analyze the monthly expenses for different departments to better understand their spending patterns and make informed budgeting decisions. You have collected the following data for four departments (Science, Arts, Engineering, and Business) over four months. The dataset is represented as follows, where each row corresponds to a different month and each column represents a department:
Month 1: [10000, 12000, 11000, 9000]
Month 2: [15000, 14000, 13000, 16000]
Month 3: [9000, 9500, 10000, 11000]
Month 4: [12000, 11000, 12500, 13000]
Question: Using NumPy functions, how would you calculate both the variance and covariance matrix of the monthly expenses for the different departments?
"""
import numpy as np

# Monthly expenses data for different departments
expenses = np.array([
    [10000, 12000, 11000, 9000],
    [15000, 14000, 13000, 16000],
    [9000,  9500,  10000, 11000],
    [12000, 11000, 12500, 13000]
])

# Calculate variance of monthly expenses for each department
variance_expenses = np.var(expenses, axis=0, ddof=0)  # ddof=0 for population variance

print("Variance of monthly expenses for each department:")
for i, var in enumerate(variance_expenses):
    print(f"Department {i+1}: {var:.2f}")

# Calculate covariance matrix of monthly expenses
covariance_expenses = np.cov(expenses, rowvar=False)

print("\nCovariance matrix of monthly expenses:")
print(covariance_expenses)
