"""Scenario: A retail store wants to know if there is a correlation between the number of customers they get and the amount of money they spend on promotions. They have data on the number of customers they had each month for the past year, as well as the amount of money spent on promotions each month.
   Question: Write a program that will calculate the correlation coefficient between customers and promotional spending, and create a scatter plot of the data.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Customers': [200, 220, 250, 230, 240, 300, 310, 280, 260, 270, 290, 320],
    'PromotionalSpending': [1000, 1200, 1300, 1100, 1150, 1500, 1600, 1400, 1350, 1250, 1450, 1550]
}
df = pd.DataFrame(data)
print("Dataset Preview:\n",df)
correlation_coefficient, _ = pearsonr(df['Customers'], df['PromotionalSpending'])
print("\nCorrelation Coefficient between Customers and Promotional Spending:\n",correlation_coefficient)
# Creating a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PromotionalSpending', y='Customers', data=df)
plt.title('Scatter Plot of Promotional Spending vs. Customers')
plt.xlabel('Promotional Spending ($)')
plt.ylabel('Number of Customers')
plt.grid(True)
plt.show()
