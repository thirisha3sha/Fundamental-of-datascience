"""Question: K-Nearest Neighbors (KNN) Classifier
You are working on a classification problem to predict whether a patient has a certain medical
condition or not based on their symptoms. You have collected a dataset of patients with
labeled data (0 for no condition, 1 for the condition) and various symptom features.
Write a Python program that allows the user to input the features of a new patient and the
value of k (number of neighbors). The program should use the KNN classifier from the scikit-
learn library to predict whether the patient has the medical condition or not based on the input
features."""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Example synthetic dataset (replace with your actual dataset)
np.random.seed(42)
n_samples = 1000

# Generate random patie""nt data
symptom1 = np.random.randint(0, 2, size=n_samples)  # Example symptom feature 1 (binary)
symptom2 = np.random.randint(0, 2, size=n_samples)  # Example symptom feature 2 (binary)
symptom3 = np.random.randint(0, 2, size=n_samples)  # Example symptom feature 3 (binary)
symptom4 = np.random.randint(0, 2, size=n_samples)  # Example symptom feature 4 (binary)
condition = np.random.randint(0, 2, size=n_samples)  # Condition label (0 or 1)

# Create DataFrame
data = pd.DataFrame({
    'Symptom1': symptom1,
    'Symptom2': symptom2,
    'Symptom3': symptom3,
    'Symptom4': symptom4,
    'Condition': condition
})

# Features (X) and target (y)
X = data[['Symptom1', 'Symptom2', 'Symptom3', 'Symptom4']]
y = data['Condition']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features if necessary (not always required for binary features)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the KNN classifier
k = int(input("Enter the value of k (number of neighbors): "))
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# User input for new patient's symptoms
print("\nEnter symptoms of the new patient (binary, 0 or 1):")
symptom1_new = int(input("Symptom 1: "))
symptom2_new = int(input("Symptom 2: "))
symptom3_new = int(input("Symptom 3: "))
symptom4_new = int(input("Symptom 4: "))

# Predict whether the new patient has the condition
new_patient = np.array([[symptom1_new, symptom2_new, symptom3_new, symptom4_new]])
new_patient_scaled = scaler.transform(new_patient)  # Scale input for prediction
prediction = knn.predict(new_patient_scaled)

if prediction[0] == 1:
    print("\nThe model predicts that the patient has the medical condition.")
else:
    print("\nThe model predicts that the patient does not have the medical condition.")
