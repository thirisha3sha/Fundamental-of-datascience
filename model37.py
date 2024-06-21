"""You are a data scientist working in a fintech startup. Your team wants to predict loan default risks based on borrower
characteristics such as credit score, income, and loan amount. Your task is to build a logistic regression model to predict loan default probabilities.
Write Python code to load the loan dataset, preprocess it, split it into training and testing sets, train a logistic regression model, and evaluate its performance
  on the test set using metrics such as accuracy, precision, recall, and F1-score.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Create a sample dataframe
data = {
    'credit_score': [720, 620, 690, 720, 650, 680, 700, 710, 690, 750],
    'income': [50000, 60000, 75000, 55000, 45000, 70000, 90000, 85000, 80000, 95000],
    'loan_amount': [10000, 20000, 30000, 15000, 12000, 25000, 40000, 30000, 35000, 45000],
    'default': [0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Separate features (X) and target (y)
X = df[['credit_score', 'income', 'loan_amount']]
y = df['default']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Predict on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'Confusion Matrix:\n{conf_matrix}')
