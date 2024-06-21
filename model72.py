"""33.Question: K-Means Clustering for Customer Segmentation
You are working for an e-commerce company and want to segment your customers into
distinct groups based on their purchasing behavior. You have collected a dataset of customer
data with various shopping-related features.
Write a Python program that allows the user to input the shopping-related features of a new
customer. The program should use K-Means clustering from scikit-learn to assign the new
customer to one of the existing segments based on the input features."""
from sklearn.cluster import KMeans
import numpy as np

# Example dataset (replace with your actual dataset)
# Features: shopping-related features
X = np.array([[10, 5],    # Example customer 1
              [15, 8],    # Example customer 2
              [8, 4],     # Example customer 3
              [12, 6],    # Example customer 4
              [18, 9]])   # Example customer 5

# Train a K-Means clustering model
k = 3  # Number of clusters (adjust as needed)
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# User input for new customer features
print("Enter the shopping-related features of the new customer:")
feature1 = float(input("Feature 1: "))
feature2 = float(input("Feature 2: "))

# Predict the cluster for the new customer
new_customer = np.array([[feature1, feature2]])
predicted_cluster = kmeans.predict(new_customer)

# Output the predicted cluster
print(f"\nThe new customer is predicted to belong to cluster {predicted_cluster[0]}")
