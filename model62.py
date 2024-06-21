"""Scenario: You work as a data scientist for a marketing agency, and one of your clients is
a large e-commerce company. The company wants to understand the purchasing behavior of
its customers and segment them into different groups based on their buying patterns. The e-
commerce company has provided you with transaction data, including customer IDs, the total
amount spent in each transaction, and the number of items purchased.
Question: Build a clustering model using the K-Means algorithm to group customers based
on their spending and purchase behavior and visualize the clusters using scatter plots or other
appropriate visualizations to gain insights into customer distribution and distinguish different
segments."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Example transaction data (replace with your actual data)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmount': [100, 250, 150, 80, 300, 200, 180, 210, 90, 120],
    'NumItems': [2, 5, 3, 1, 6, 4, 3, 4, 2, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select relevant features for clustering
X = df[['TotalAmount', 'NumItems']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the number of clusters (k)
k = 3  # Example: Assume 3 clusters

# Build K-Means clustering model
kmeans = KMeans(n_clusters=k, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original DataFrame
df['Cluster'] = cluster_labels

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(df['TotalAmount'], df['NumItems'], c=df['Cluster'], cmap='viridis', edgecolor='k', s=100)
plt.title('Customer Segmentation based on Spending and Purchase Behavior')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
