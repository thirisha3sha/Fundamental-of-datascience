"""
You are a data scientist working in a pharmaceutical company. Your team wants to classify drug compounds based on their chemical properties to streamline research and development efforts. Your task is to perform hierarchical clustering to group drug compounds into clusters based on their molecular features. Write Python code to load the chemical data, preprocess it, apply hierarchical clustering, and visualize the hierarchical structure using dendrograms.
"""
import pandas as pd
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

# Step 2: Create a DataFrame with mock chemical data
data = {
    'Compound': ['DrugA', 'DrugB', 'DrugC', 'DrugD', 'DrugE'],
    'Feature1': [0.2, 0.4, 0.6, 0.8, 1.0],
    'Feature2': [0.5, 0.7, 0.3, 0.9, 0.1],
    'Feature3': [0.8, 0.2, 0.4, 0.6, 0.9]
}

df = pd.DataFrame(data)
df.set_index('Compound', inplace=True)

# Step 4: Hierarchical clustering
# Calculate the linkage matrix
Z = hierarchy.linkage(df, method='average', metric='euclidean')
#5: Visualize the dendrogram
plt.figure(figsize=(10, 6))
dn = hierarchy.dendrogram(Z, labels=df.index, orientation='top', leaf_rotation=90)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Drug Compounds')
plt.ylabel('Distance')
plt.tight_layout()
plt.show()
