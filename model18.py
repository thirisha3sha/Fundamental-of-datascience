"""A company wants to know if there is a correlation between the number of sales they make and the amount of advertising they spend. They have data on the number of sales they made each month for the past year, as well as the amount of advertising they spent each month. Write a program that will calculate the correlation coefficient between sales and advertising, and create a scatter plot of the data.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (replace with actual data if available)
months = range(1, 13)
sales = [100, 110, 120, 115, 130, 140, 150, 160, 170, 165, 180, 190]
advertising = [2000, 2200, 2400, 2300, 2500, 2600, 2800, 3000, 3200, 3100, 3300, 3500]

# Create a DataFrame
data = {
    'Month': months,
    'Sales': sales,
    'Advertising': advertising
}
df = pd.DataFrame(data)

# Calculate correlation coefficient between Sales and Advertising
correlation_coefficient = np.corrcoef(df['Sales'], df['Advertising'])[0, 1]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Advertising'], df['Sales'], color='b', marker='o')
plt.title('Sales vs Advertising Spending')
plt.xlabel('Advertising Spending ($)')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()

# Add correlation coefficient to the plot
plt.text(2000, 150, f'Correlation Coefficient: {correlation_coefficient:.2f}', fontsize=12, color='red')

# Show plot
plt.show()

# Print correlation coefficient
print(f'Correlation Coefficient between Sales and Advertising: {correlation_coefficient:.2f}')
