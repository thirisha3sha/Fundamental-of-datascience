"""Question: Classification and Regression Trees (CART) for Car Price Prediction
You are working for a car dealership, and you want to predict the price of used cars based on
various features such as the car&#39;s mileage, age, brand, and engine type. You have collected a
dataset of used cars with their respective prices.
Write a Python program that loads the car dataset and allows the user to input the features of
a new car they want to sell. The program should use the Classification and Regression Trees
(CART) algorithm from scikit-learn to predict the price of the new car based on the input
features.
The CART algorithm will create a tree-based model that will split the data into subsets based
on the chosen features and their values, leading to a decision path that eventually predicts the
price of the car. The program should output the predicted price and display the decision path
(the sequence of conditions leading to the prediction) for the new car."""
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder

# Example car data (replace with your actual dataset)
data = {
    'Mileage': [50000, 60000, 30000, 70000, 20000],
    'Age': [3, 5, 2, 6, 1],
    'Brand': ['Toyota', 'Honda', 'Toyota', 'Ford', 'Honda'],
    'EngineType': ['Gas', 'Diesel', 'Gas', 'Gas', 'Diesel'],
    'Price': [25000, 18000, 30000, 15000, 22000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical variables (Brand and EngineType)
le_brand = LabelEncoder()
df['Brand'] = le_brand.fit_transform(df['Brand'])

le_engine = LabelEncoder()
df['EngineType'] = le_engine.fit_transform(df['EngineType'])

# Features and target
X = df[['Mileage', 'Age', 'Brand', 'EngineType']]
y = df['Price']

# Build CART model (DecisionTreeRegressor)
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# User input for new car features
print("Enter details of the new car:")
mileage = int(input("Mileage (in miles): "))
age = int(input("Age (in years): "))
brand = input("Brand (Toyota, Honda, Ford, etc.): ")
engine_type = input("Engine Type (Gas, Diesel, etc.): ")

# Encode user input for prediction
brand_encoded = le_brand.transform([brand])[0]
engine_encoded = le_engine.transform([engine_type])[0]

# Predict price for the new car
new_car = [[mileage, age, brand_encoded, engine_encoded]]
predicted_price = model.predict(new_car)[0]

# Display predicted price
print(f"\nPredicted Price of the Car: ${predicted_price:.2f}")
