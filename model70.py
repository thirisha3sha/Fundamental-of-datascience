"""31.Question : Linear Regression for Housing Price Prediction
You are a real estate analyst trying to predict housing prices based on various features of the
houses, such as area, number of bedrooms, and location. You have collected a dataset of
houses with their respective prices.
Write a Python program that allows the user to input the features (area, number of bedrooms,
etc.) of a new house. The program should use linear regression from scikit-learn to predict the
price of the new house based on the input features."""
from sklearn.linear_model import LinearRegression
import numpy as np

# Example dataset (replace with your actual dataset)
# Features: area (in square feet), number of bedrooms, location (numeric code), etc.
# Target: price (in dollars)
X_train = np.array([[1500, 3, 1],   # Example house 1
                    [2000, 4, 2],   # Example house 2
                    [1800, 3, 1],   # Example house 3
                    [2100, 4, 2]])  # Example house 4
y_train = np.array([300000, 400000, 350000, 425000])  # Example prices

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# User input for new house features
print("Enter the features of the new house:")
area = float(input("Area (sq. ft.): "))
bedrooms = int(input("Number of bedrooms: "))
location = int(input("Location code (numeric): "))

# Predict the price of the new house
new_house = np.array([[area, bedrooms, location]])
predicted_price = model.predict(new_house)

# Output the predicted price
print(f"\nThe predicted price of the new house is: ${predicted_price[0]:,.2f}")
