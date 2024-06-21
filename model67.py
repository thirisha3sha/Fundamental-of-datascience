"""Scenario: You work as a data scientist for an e-commerce company that sells a wide
range of products online. The company collects vast amounts of data about its customers,
including their purchase history, browsing behavior, demographics, and more. The marketing
team wants to understand their customer base better and improve their targeted marketing
strategies. They have asked you to perform customer segmentation using clustering
techniques to identify distinct groups of customers with similar characteristics.
Question: Your task is to use Python and clustering algorithms to segment the customers into
different groups based on their behavior and characteristics. The marketing team will use
these segments to tailor their marketing campaigns and promotions effectively."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Generate synthetic customer data (replace with your actual dataset)
np.random.seed(42)
n_samples = 1000

# Generate random customer data
age = np.random.randint(18, 70, size=n_samples)
income = np.random.randint(20000, 150000, size=n_samples)
purchase_frequency = np.random.randint(1, 10, size=n_samples)  # How often they purchase (1-10)
purchase_amount = np.random.randint(50, 500, size=n_samples)  # Average purchase amount ($50-$500)

# Create DataFrame
data = pd.DataFrame({
    'Age': age,
    'Income': income,
    'PurchaseFrequency': purchase_frequency,
    'PurchaseAmount': purchase_amount
})

# Scale the data (important for clustering)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Apply K-Means clustering
k = 4  # Number of clusters (can be adjusted based on analysis)
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to original DataFrame
data['Cluster'] = clusters

# Visualize clusters using PCA for dimensionality reduction (to 2D)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
principal_df['Cluster'] = clusters

# Scatter plot of the clusters
plt.figure(figsize=(10, 6))
scatter = plt.scatter(principal_df['PC1'], principal_df['PC2'], c=principal_df['Cluster'], cmap='viridis', alpha=0.6)
plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter, label='Cluster')
plt.show()

# Analyze cluster characteristics (e.g., average values)
cluster_analysis = data.groupby('Cluster').mean()
print(cluster_analysis)
