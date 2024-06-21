"""  A health analyst wants to investigate whether the average recovery time of two different treatment methods for
a specific illness is significantly different. For Treatment A, a random sample of 100 patients was collected, and the mean recovery time was found
to be 6.2 days with a standard deviation of 1.5 days. For Treatment B, a random sample of 120 patients was collected, and the mean recovery time was found to be 5.8 days with a
standard deviation of 1.2 days. Using a 95% confidence level, test the hypothesis that the mean recovery times of Treatment A and Treatment B are significantly different.
"""
import pandas as pd
import numpy as np
from scipy import stats

# Step 1: Create a DataFrame with treatment data
data = {
    'Treatment': ['A', 'B'],
    'Sample Size': [100, 120],
    'Mean Recovery Time (days)': [6.2, 5.8],
    'Standard Deviation (days)': [1.5, 1.2]
}
df = pd.DataFrame(data)

# Additional calculations for t-test
mean_A = df.loc[df['Treatment'] == 'A', 'Mean Recovery Time (days)'].values[0]
mean_B = df.loc[df['Treatment'] == 'B', 'Mean Recovery Time (days)'].values[0]
std_A = df.loc[df['Treatment'] == 'A', 'Standard Deviation (days)'].values[0]
std_B = df.loc[df['Treatment'] == 'B', 'Standard Deviation (days)'].values[0]
n_A = df.loc[df['Treatment'] == 'A', 'Sample Size'].values[0]
n_B = df.loc[df['Treatment'] == 'B', 'Sample Size'].values[0]

# Step 2: Perform independent two-sample t-test
t_stat, p_value = stats.ttest_ind_from_stats(mean_A, std_A, n_A, mean_B, std_B, n_B)

# Step 3: Interpret the results
alpha = 0.05  # 95% confidence level
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis. There is sufficient evidence to say that the mean recovery times of Treatment A and Treatment B are significantly different.")
else:
    print("Fail to reject the null hypothesis. There is not sufficient evidence to say that the mean recovery times of Treatment A and Treatment B are significantly different.")
