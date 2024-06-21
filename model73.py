"""34.Question: Evaluation Metrics for Model Performance
You have trained a machine learning model on a dataset, and now you want to evaluate its
performance using various metrics.
Write a Python program that loads a dataset and trained model from scikit-learn. The program
should ask the user to input the names of the features and the target variable they want to use
for evaluation. The program should then calculate and display common evaluation metrics
such as accuracy, precision, recall, and F1-score for the model&#39;s predictions on the test data."""
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Generate synthetic dataset (replace with your actual dataset loading code)
X, y = make_classification(n_samples=1000, n_features=5, random_state=42)

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model (replace with your actual model training code)
model = LogisticRegression()
model.fit(X_train, y_train)

# User input for features and target variable
print("Enter the names of the features:")
feature_names = input().strip().split()
print("Enter the name of the target variable:")
target_name = input().strip()

# Assume feature_names and target_name match the column names in your dataset

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Display the evaluation metrics
print("\nEvaluation Metrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")
