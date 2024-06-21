"""30.Question : Decision Tree for Iris Flower Classification
You are analyzing the famous Iris flower dataset to classify iris flowers into three species
based on their sepal and petal dimensions. You want to use a Decision Tree classifier to
accomplish this task.
Write a Python program that loads the Iris dataset from scikit-learn, and allows the user to
input the sepal length, sepal width, petal length, and petal width of a new flower. The
program should then use the Decision Tree classifier to predict the species of the new flower."""
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (species)

# Train a Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# User input for new flower's sepal and petal dimensions
print("Enter the dimensions of the new flower:")
sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

# Predict the species of the new flower
new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = clf.predict(new_flower)

# Output the predicted species
predicted_species = iris.target_names[prediction][0]
print(f"\nThe predicted species of the new flower is: {predicted_species}")
