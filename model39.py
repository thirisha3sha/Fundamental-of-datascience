"""You work as a data analyst for a popular online streaming service that offers a variety of content, including movies, TV shows, and documentaries. Your company has collected viewership data over the past year and wants to analyze and visualize this data to gain insights into viewing trends, content performance, and user preferences. To understand which content categories are most popular, create line, scatter, and bar plots that display the distribution of viewership across different content categories. Each plot should represent a category, and the height of the bar should indicate the total viewership count for that category.
Question: Using Python, how would you create line, scatter, and bar plots to visualize the distribution of viewership across different content categories?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock data for viewership across content categories
data = {
    'Category': ['Movies', 'TV Shows', 'Documentaries', 'Anime', 'Comedy', 'Drama'],
    'Viewership': [50000, 30000, 20000, 15000, 10000, 25000],
    'Rating': [4.2, 4.0, 4.5, 3.8, 4.1, 4.3],
    'Year': [2019, 2020, 2021, 2019, 2020, 2021]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame (optional)
print(df)

# Line Plot: Viewership trend over years for a specific category (e.g., Movies)
plt.figure(figsize=(8, 5))
movies_data = df[df['Category'] == 'Movies']
plt.plot(movies_data['Year'], movies_data['Viewership'], marker='o', linestyle='-', color='b', label='Movies')
plt.title('Viewership Trend for Movies Over Years')
plt.xlabel('Year')
plt.ylabel('Viewership Count')
plt.xticks(df['Year'].unique())  # Ensure all years are shown on the x-axis
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter Plot: Relationship between viewership and rating for all categories
plt.figure(figsize=(8, 5))
plt.scatter(df['Viewership'], df['Rating'], color='r', alpha=0.7)
plt.title('Viewership vs. Rating for Different Content Categories')
plt.xlabel('Viewership Count')
plt.ylabel('Rating')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Plot: Total viewership for each content category
plt.figure(figsize=(8, 5))
plt.bar(df['Category'], df['Viewership'], color='g', alpha=0.7)
plt.title('Total Viewership by Content Category')
plt.xlabel('Content Category')
plt.ylabel('Total Viewership')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
