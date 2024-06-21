"""Scenario: You work as a data scientist for a real estate company. The company has
collected data on various houses, including features such as the size of the house, number of
bedrooms, location, and other relevant attributes. The marketing team wants to build a
predictive model to estimate the price of houses based on their features. They believe that
linear regression modeling can be an effective approach for this task.
Question:Your task is write a Python program to perform bivariate analysis and build a linear
regression model to predict house prices based on a selected feature (e.g., house size) from
the dataset. Additionally, you need to evaluate the model&#39;s performance to ensure its accuracy
and reliability."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Example house data (replace with your actual dataset)
data = {
    'HouseSize': [1500, 1800, 1350, 2000, 1200, 1600, 1550, 1720, 1850, 1400],
    'NumBedrooms': [3, 4, 2, 4, 2, 3, 3, 4, 4, 2],
    'Location': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Price': [300000, 380000, 270000, 420000, 250000, 350000, 330000, 390000, 400000, 280000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select a feature for bivariate analysis (e.g., HouseSize)
feature = 'HouseSize'

# Bivariate analysis: Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df[feature], df['Price'], color='blue', alpha=0.7)
plt.title(f'Bivariate Analysis: House Price vs {feature}')
plt.xlabel(feature)
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Calculate correlation coefficient
corr_coef = np.corrcoef(df[feature], df['Price'])[0, 1]
print(f"Correlation Coefficient between {feature} and Price: {corr_coef:.2f}")

# Prepare data for modeling
X = df[[feature]]
y = df['Price']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# Visualize predicted vs actual prices
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual', alpha=0.7)
plt.scatter(X_test, y_pred, color='red', label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted House Prices')
plt.xlabel(feature)
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
