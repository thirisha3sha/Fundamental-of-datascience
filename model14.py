"""Scenario: You are a data analyst working for a car manufacturing company. As part of your analysis, you have a dataset containing information about the fuel efficiency of different car models. The dataset is stored in a NumPy array named fuel_efficiency, where each element represents the fuel efficiency (in miles per gallon) of a specific car model. Your task is to calculate the average fuel efficiency and determine the percentage improvement in fuel efficiency between two car models.
Question: How would you use NumPy arrays and arithmetic operations to calculate the average fuel efficiency and determine the percentage improvement in fuel efficiency between two car models?
"""
import numpy as np
import pandas as pd

# Example data (replace with your actual dataset or NumPy array)
fuel_efficiency = np.array([30, 25, 28, 32, 27, 29, 31, 26, 33, 30])

# Create a DataFrame for visualization
df = pd.DataFrame({
    'Model': range(1, len(fuel_efficiency) + 1),
    'Fuel Efficiency (MPG)': fuel_efficiency
})

print("\nDataFrame:")
print(df)

# Calculate average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Example: Comparing fuel efficiency between two models
model1_index = 0  # Replace with the index of the first car model (0-based index)
model2_index = 3  # Replace with the index of the second car model (0-based index)

fuel_efficiency_model1 = fuel_efficiency[model1_index]
fuel_efficiency_model2 = fuel_efficiency[model2_index]

# Calculate percentage improvement
percentage_improvement = ((fuel_efficiency_model2 - fuel_efficiency_model1) / fuel_efficiency_model1) * 100

# Print results
print("Average Fuel Efficiency:", average_fuel_efficiency, "MPG")
print(f"Percentage Improvement from Model {model1_index + 1} to Model {model2_index + 1}: {percentage_improvement:.2f}%")
