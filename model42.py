"""You are a data scientist working in an e-commerce platform. Your team wants to enhance product recommendation strategies by clustering customers based on their
browsing and purchasing patterns. Your task is to build a clustering model, such as K-means, to segment customers into distinct groups. Write Python code to load the
customer interaction data, preprocess it, apply K-means clustering for customer segmentation, and evaluate the model's performance using metrics such as silhouette score.
 
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Sample customer interaction data (mock data)
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'browsing_time_minutes': [10, 15, 5, 20, 30, 25, 10, 15, 8, 18],
    'purchase_amount': [50, 100, 20, 150, 200, 180, 60, 80, 30, 120]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame (optional)
print(df)

# Extract features for clustering
X = df[['browsing_time_minutes', 'purchase_amount']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
df['cluster'] = kmeans.labels_

# Evaluate the clustering with silhouette score
silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
print(f'Silhouette Score: {silhouette_avg:.2f}')

# Print cluster centers (optional)
print('Cluster Centers:')
print(scaler.inverse_transform(kmeans.cluster_centers_))

# Visualize the clusters (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(df['browsing_time_minutes'], df['purchase_amount'], c=df['cluster'], cmap='viridis', s=50, alpha=0.7)
plt.title('Customer Segmentation by K-means Clustering')
plt.xlabel('Browsing Time (minutes)')
plt.ylabel('Purchase Amount')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
