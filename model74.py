"""Question: You are a data scientist working for an e-commerce company. The marketing
team has conducted an A/B test to evaluate the effectiveness of two different website designs
(A and B) in terms of conversion rate. They randomly divided the website visitors into two
groups, with one group experiencing design A and the other experiencing design B. After a
week of data collection, you now have the conversion rate data for both groups. You want to
determine whether there is a statistically significant difference in the mean conversion rates
between the two website designs.
Question:
&quot;Based on the data collected from the A/B test, is there a statistically significant difference in
the mean conversion rates between website design A and website design B?&quot;"""
import numpy as np
from scipy import stats

# Conversion rate data (replace with your actual data)
conversion_rate_A = np.array([0.12, 0.11, 0.10, 0.14, 0.13])
conversion_rate_B = np.array([0.10, 0.09, 0.11, 0.12, 0.10])

# Calculate sample statistics
mean_A = np.mean(conversion_rate_A)
mean_B = np.mean(conversion_rate_B)
std_dev_A = np.std(conversion_rate_A, ddof=1)  # ddof=1 for sample standard deviation
std_dev_B = np.std(conversion_rate_B, ddof=1)
n_A = len(conversion_rate_A)
n_B = len(conversion_rate_B)

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)

# Determine degrees of freedom
degrees_freedom = n_A + n_B - 2

# Print results
print(f"Mean conversion rate for Design A: {mean_A:.4f}")
print(f"Mean conversion rate for Design B: {mean_B:.4f}")
print(f"Standard deviation for Design A: {std_dev_A:.4f}")
print(f"Standard deviation for Design B: {std_dev_B:.4f}")
print(f"Sample size for Design A: {n_A}")
print(f"Sample size for Design B: {n_B}")
print(f"Degrees of freedom: {degrees_freedom}")
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis.")
    print("There is a statistically significant difference in the mean conversion rates between Design A and Design B.")
else:
    print("\nFail to reject the null hypothesis.")
    print("There is no statistically significant difference in the mean conversion rates between Design A and Design B.")
