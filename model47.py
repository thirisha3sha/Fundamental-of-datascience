"""You are a data scientist working in a retail company. Your team wants to analyze customer purchase data to identify patterns and trends in buying behavior. Your task is to preprocess the customer dataset, handle missing values, and perform Principal Component Analysis (PCA) to visualize the high-dimensional data in a lower-dimensional space. Write Python code to load the customer data, preprocess it, apply PCA, and visualize the data points in a scatter plot."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Sample customer purchase data (mock data)
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 30, np.nan, 35, 40],
    'Income': [50000, 80000, 60000, np.nan, 70000],
    'PurchaseAmount': [1000, 1500, 1200, 1800, 1300],
    'Frequency': [2, 3, 2, 4, 3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)
print()

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Income'] = df['Income'].fillna(df['Income'].mean())

# Separate features (X) and target (y)
X = df[['Age', 'Income', 'PurchaseAmount', 'Frequency']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create a new DataFrame with PCA results
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])

# Plot the data points in a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df_pca['PC1'], df_pca['PC2'], s=100, alpha=0.5)
plt.title('PCA of Customer Purchase Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.tight_layout()
plt.show()
