"""Scenario: Suppose you are working as a data scientist for a medical research
organization. Your team has collected data on patients with a certain medical condition and
their treatment outcomes. The dataset includes various features such as age, gender, blood
pressure, cholesterol levels, and whether the patient responded positively (&quot;Good&quot;) or
negatively (&quot;Bad&quot;) to the treatment. The organization wants to use this model to identify
potential candidates who are likely to respond positively to the treatment and improve their
medical approach.
Question: Your task is to build a classification model using the KNN algorithm to predict the
treatment outcome (&quot;Good&quot; or &quot;Bad&quot;) for new patients based on their features. Evaluate the
model&#39;s performance using accuracy, precision, recall, and F1-score.Make predictions on the
test set and display the results."""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Example data (replace with your actual dataset)
data = {
    'Age': [45, 50, 30, 55, 35, 40, 60, 25, 50, 65],
    'Gender': ['M', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'F'],
    'BloodPressure': [120, 130, 110, 140, 115, 125, 135, 118, 128, 145],
    'Cholesterol': [200, 220, 190, 240, 210, 200, 230, 195, 205, 250],
    'Outcome': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Good', 'Bad']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert categorical variables to numerical (if needed)
df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})

# Split data into features (X) and target (y)
X = df[['Age', 'Gender', 'BloodPressure', 'Cholesterol']]
y = df['Outcome']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize KNN classifier
k = 3  # Example: Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model
knn.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

# Display evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# Display classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
