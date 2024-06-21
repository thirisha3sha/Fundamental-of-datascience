"""Scenario: You are dealing with a dataset containing the monthly expenses of different
departments in a company. Use NumPy functions to efficiently calculate both the variance
and covariance matrix of these expenses."""
import numpy as np

# Example monthly expenses data for 3 departments over 6 months
# Replace this with your actual data
expenses_data = np.array([
    [10000, 12000, 11000, 13000, 12500, 11500],  # Department A
    [8000, 8500, 9000, 9500, 9200, 8800],       # Department B
    [15000, 15500, 16000, 16500, 17000, 17500]  # Department C
])

# Calculate variance of expenses for each department
variance = np.var(expenses_data, axis=1)
print("Variance of expenses for each department:")
print(variance)

# Calculate covariance matrix of expenses among departments
covariance_matrix = np.cov(expenses_data)
print("\nCovariance matrix of expenses among departments:")
print(covariance_matrix)
