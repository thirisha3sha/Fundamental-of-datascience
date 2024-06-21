"""Scenario: You are a data analyst working for a social media platform. As part of your
analysis, you have a dataset containing user interaction data, including the number of likes
received by each post. Your task is to develop a Python program that calculates the frequency
distribution of likes among the posts.
Question: Develop a Python program to calculate the frequency distribution of likes among
the posts?"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample data (assuming 'likes' column exists in the DataFrame)
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [50, 30, 70, 40, 60, 80, 90, 55, 75, 65]  # Example likes received by each post
}

# Create DataFrame
interaction_data = pd.DataFrame(data)

# Calculate frequency distribution of likes
likes_distribution = interaction_data['likes'].value_counts().sort_index()

# Print the frequency distribution
print("Frequency distribution of likes among the posts:")
print(likes_distribution)

# Optionally, plot the frequency distribution (bar plot)
plt.figure(figsize=(10, 6))
plt.bar(likes_distribution.index, likes_distribution.values, color='skyblue')
plt.title('Frequency Distribution of Likes Among Posts')
plt.xlabel('Number of Likes')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
