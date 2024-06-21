"""Scenario: You are working on a project that involves analyzing a dataset containing information about houses in a neighborhood. The dataset is stored in a CSV file, and you have imported it into a NumPy array named house_data. Each row of the array represents a house, and the columns contain various features such as the number of bedrooms, square footage, and sale price.
Question: Using NumPy arrays and operations, how would you find the average sale price of houses with more than four bedrooms in the neighborhood?
"""
import numpy as np

# Sample house data (mock data)
# Assuming each row represents a house: [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 2000, 300000],
    [4, 2500, 350000],
    [5, 3000, 400000],
    [4, 2800, 380000],
    [6, 3500, 450000],
    [3, 1800, 280000],
    [5, 3200, 420000],
])

# Print the house_data array (optional)
print("House Data:")
print(house_data)
print()

# Filter houses with more than four bedrooms
bedrooms = house_data[:, 0]  # Selecting the first column (bedrooms)
filtered_houses = house_data[bedrooms > 4]

# Calculate the average sale price of houses with more than four bedrooms
average_sale_price = np.mean(filtered_houses[:, 2])  # Selecting the third column (sale price)

print(f"Average Sale Price of Houses with More than Four Bedrooms: ${average_sale_price:.2f}")
