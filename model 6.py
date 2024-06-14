"""Scenario: You are working on a data analysis project that involves analyzing the weekly sales and customer traffic data for a retail store. You have a dataset containing the weekly sales and customer traffic values for each week of a year. Your task is to develop a Python program that generates line plots and scatter plots to visualize the sales and customer traffic data.
   - Question:
  	Develop a Python program to create a line plot of the weekly sales data.
 	Develop a Python program to create a scatter plot of the weekly customer traffic data.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset for weekly sales
data_sales = {
    'Week': list(range(1, 53)),
    'Weekly Sales': [
        1500, 1600, 1700, 1650, 1800, 1900, 2000, 2100, 2200, 2150, 2300, 2400, 2500,
        2600, 2700, 2750, 2900, 3000, 3100, 3200, 3300, 3250, 3400, 3500, 3600, 3700,
        3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000,
        5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300
    ]
}

# Create DataFrame for weekly sales
df_sales = pd.DataFrame(data_sales)
print("sales data:\n",df_sales)

# Line plot for weekly sales
plt.figure(figsize=(10, 6))
plt.plot(df_sales['Week'], df_sales['Weekly Sales'], marker='o')
plt.title('Weekly Sales Over a Year')
plt.xlabel('Week')
plt.ylabel('Weekly Sales')
plt.grid(True)
plt.show()

# Sample dataset for weekly customer traffic
data_traffic = {
    'Week': list(range(1, 53)),
    'Customer Traffic': [
        100, 110, 120, 115, 130, 140, 150, 160, 170, 165, 180, 190, 200, 210, 220, 225,
        240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
        390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540,
        550, 560, 570, 580, 590, 600
    ][:52]  

}

# Create DataFrame for weekly customer traffic
df_traffic = pd.DataFrame(data_traffic)
print("\n tarffic data:\n",df_traffic)

# Scatter plot for weekly customer traffic
plt.figure(figsize=(10, 6))
plt.scatter(df_traffic['Week'], df_traffic['Customer Traffic'], color='r')
plt.title('Weekly Customer Traffic Over a Year')
plt.xlabel('Week')
plt.ylabel('Customer Traffic')
plt.grid(True)
plt.show()
