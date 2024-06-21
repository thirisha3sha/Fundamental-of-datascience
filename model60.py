"""Scenario: In a study, you have collected data on the hours spent studying (variable x)
and the corresponding exam scores (variable y) for a group of students. Calculate the
covariance between study hours and exam scores to explore if there is a relationship."""
import numpy as np

# Example daily sales data (replace with your actual data)
daily_sales = np.array([100, 120, 130, 110, 105, 115, 125, 135, 140, 130,
                        120, 125, 110, 115, 120, 130, 135, 140, 145, 150,
                        140, 135, 130, 125, 120, 115, 110, 105, 100, 95])

# Calculate variance of daily sales
sales_variance = np.var(daily_sales)

print(f"Variance of daily sales: {sales_variance}")

# Example study hours and exam scores data (replace with your actual data)
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
exam_scores = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

# Calculate covariance between study hours and exam scores
covariance = np.cov(study_hours, exam_scores)[0, 1]

print(f"Covariance between study hours and exam scores: {covariance}")
