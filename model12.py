"""You are a data scientist working in a healthcare organization. Your team wants to predict patient readmission risks based on medical history and treatment details. Your task is to build a classification and regression trees (CART) model for readmission prediction. Write Python code to load the patient data, preprocess it, split it into training and testing sets, train a CART model, and visualize the decision tree for interpretation.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Step 1: Load and preprocess patient data
# Assuming you have a CSV file 'patient_data.csv' with columns including features and target variable 'readmitted'
# Replace 'patient_data.csv' with your actual dataset path

# Example data (replace with actual data loading code)
data = {
    'Age': [65, 25, 38, 50, 60],
    'Blood Pressure': [140, 120, 130, 135, 128],
    'Cholesterol': [260, 190, 220, 240, 250],
    'Treatment': ['A', 'B', 'B', 'A', 'C'],
    'Readmitted': [1, 0, 1, 0, 1]  # 1 for readmitted, 0 for not readmitted
}

df = pd.DataFrame(data)

# Step 2: Prepare data for modeling
# Separate features (X) and target variable (y)
X = df.drop('Readmitted', axis=1)
y = df['Readmitted']

# Convert categorical variables into dummy/indicator variables if necessary
X = pd.get_dummies(X)

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a CART model (Decision Tree Classifier)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 5: Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['Not Readmitted', 'Readmitted'])
plt.title("Decision Tree for Patient Readmission Prediction")
plt.show()

# Step 6: Model evaluation (optional)
y_pred = clf.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
