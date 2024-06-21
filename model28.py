""" Scenario: A research institute conducted a study on the relationship between diet and health outcomes among a group of 18 randomly selected participants.
They collected data on participants' ages and cholesterol levels with the following results.
 
Question:Calculate the mean, median, and standard deviation of ages and cholesterol levels using Pandas.
Create boxplots to visualize the distribution of ages and cholesterol levels.
Generate a scatter plot and a quantile-quantile (q-q) plot based on these two variables to explore their relationship and distribution characteristics.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
data = {
    'Age': [23, 45, 56, 34, 47, 50, 29, 40, 33, 25, 48, 52, 31, 44, 37, 36, 49, 41],
    'Cholesterol': [190, 230, 210, 220, 240, 260, 195, 205, 215, 198, 225, 250, 202, 238, 222, 215, 245, 210]
}
df = pd.DataFrame(data)
print("datset preview:\n",df)
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()
mean_cholesterol = df['Cholesterol'].mean()
median_cholesterol = df['Cholesterol'].median()
std_cholesterol = df['Cholesterol'].std()
print(f"Mean Age: {mean_age}, Median Age: {median_age}, Standard Deviation Age: {std_age}")
print(f"Mean Cholesterol: {mean_cholesterol}, Median Cholesterol: {median_cholesterol}, Standard Deviation Cholesterol: {std_cholesterol}")

# Create boxplots
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title('Boxplot of Ages')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Cholesterol'])
plt.title('Boxplot of Cholesterol Levels')

plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Age'], y=df['Cholesterol'])
plt.title('Scatter Plot of Age vs Cholesterol')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.show()

# Q-Q plot for Age
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')

# Q-Q plot for Cholesterol
plt.subplot(1, 2, 2)
stats.probplot(df['Cholesterol'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Cholesterol')

plt.tight_layout()
plt.show()
