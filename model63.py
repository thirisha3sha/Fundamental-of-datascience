"""Scenario: You work as a data scientist for a retail company that operates multiple stores.
The company is interested in segmenting its customers based on their purchasing behavior to
better understand their preferences and tailor marketing strategies accordingly. To achieve
this, your team has collected transaction data from different stores, which includes customer
IDs, the total amount spent in each transaction, and the frequency of visits.
Question: Your task is to build a clustering model using the K-Means algorithm to group
customers into distinct segments based on their spending patterns."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Example transaction data (replace with your actual data)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmount': [100, 250, 150, 80, 300, 200, 180, 210, 90, 120],
    'Frequency': [5, 10, 7, 3, 12, 8, 6, 9, 4, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select relevant features for clustering
X = df[['TotalAmount', 'Frequency']]

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
plt.scatter(df['TotalAmount'], df['Frequency'], c=df['Cluster'], cmap='viridis', edgecolor='k', s=100)
plt.title('Customer Segmentation based on Spending Patterns')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
