"""You are a data scientist working in a mobile app development company. Your team wants to segment users based on their app usage behavior to
tailor personalized features and notifications. Your task is to perform k-means clustering to segment users into distinct groups. Write Python code to load the app usage data,
preprocess it, apply k-means clustering, and visualize the clusters using scatter plots."""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data creation: user ID and their app usage in hours for different features
data = {
    'UserID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Feature1': [5, 3, 6, 7, 8, 2, 9, 5, 4, 3],
    'Feature2': [10, 12, 11, 9, 6, 4, 13, 7, 8, 3],
    'Feature3': [15, 16, 15, 14, 13, 8, 18, 12, 11, 7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Preprocess data: normalize features
features = df.drop('UserID', axis=1)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Visualization of clusters using scatter plots
plt.figure(figsize=(12, 6))

# Plot clusters for Feature1 vs Feature2
plt.subplot(1, 2, 1)
plt.scatter(df['Feature1'], df['Feature2'], c=df['Cluster'], cmap='viridis')
plt.title('Feature1 vs Feature2')
plt.xlabel('Feature1')
plt.ylabel('Feature2')

# Plot clusters for Feature1 vs Feature3
plt.subplot(1, 2, 2)
plt.scatter(df['Feature1'], df['Feature3'], c=df['Cluster'], cmap='viridis')
plt.title('Feature1 vs Feature3')
plt.xlabel('Feature1')
plt.ylabel('Feature3')

plt.tight_layout()
plt.show()

# Print the DataFrame with assigned clusters
print("DataFrame with assigned clusters:")
print(df)
