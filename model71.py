"""32.Question: Logistic Regression for Customer Churn Prediction
You are working for a telecommunications company, and you want to predict whether a
customer will churn (leave the company) based on their usage patterns and demographic data.
You have collected a dataset of past customers with their churn status (0 for not churned, 1
for churned) and various features.

Write a Python program that allows the user to input the features (e.g., usage minutes,
contract duration) of a new customer. The program should use logistic regression from scikit-
learn to predict whether the new customer will churn or not based on the input features."""
from sklearn.linear_model import LogisticRegression
import numpy as np

# Example dataset (replace with your actual dataset)
# Features: usage minutes, contract duration, etc.
# Target: churn status (0 for not churned, 1 for churned)
X_train = np.array([[100, 12],    # Example customer 1
                    [200, 6],     # Example customer 2
                    [150, 9],     # Example customer 3
                    [250, 3]])    # Example customer 4
y_train = np.array([0, 0, 1, 1])  # Example churn status

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# User input for new customer features
print("Enter the features of the new customer:")
usage_minutes = float(input("Usage minutes: "))
contract_duration = float(input("Contract duration (months): "))

# Predict whether the new customer will churn
new_customer = np.array([[usage_minutes, contract_duration]])
predicted_churn = model.predict(new_customer)

# Output the predicted churn status
if predicted_churn[0] == 1:
    print("\nThe model predicts that the customer will churn.")
else:
    print("\nThe model predicts that the customer will not churn.")
