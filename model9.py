"""Scenario: You have collected data on the ages of customers in a retail store. Write a Python program to calculate and display the 25th percentile of customer ages.
"""
import numpy as np
customer_ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
percentile_25 = np.percentile(customer_ages, 25)
print(f"The 25th percentile of customer ages is: {percentile_25}")
