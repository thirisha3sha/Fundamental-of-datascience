"""What is the average satisfaction score and 95% confidence interval for various vacation destinations, and which destinations receive the highest average scores? Additionally, how does the sentiment of travel reviews vary across different destinations?
"""
import pandas as pd
import numpy as np
from scipy import stats

# Sample data (mock data)
data = {
    'Destination': ['Beach', 'Mountains', 'City', 'Countryside', 'Island'],
    'Satisfaction_Score': [4.3, 4.5, 4.1, 4.4, 4.2],
    'Reviews': [100, 120, 80, 90, 110],  # Number of reviews (optional for sentiment analysis)
    'Sentiment_Score': [0.8, 0.75, 0.85, 0.78, 0.82]  # Example sentiment scores (optional)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame (optional)
print(df)

# Calculate average satisfaction score and 95% confidence interval
avg_score = df['Satisfaction_Score'].mean()
confidence_interval = stats.t.interval(0.95, len(df)-1, loc=np.mean(df['Satisfaction_Score']), scale=stats.sem(df['Satisfaction_Score']))

print(f'Average Satisfaction Score: {avg_score:.2f}')
print(f'95% Confidence Interval: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})')

# Identify destination with highest average satisfaction score
highest_score_destination = df.loc[df['Satisfaction_Score'].idxmax(), 'Destination']
highest_score = df['Satisfaction_Score'].max()

print(f'\nDestination with Highest Average Satisfaction Score:')
print(f'{highest_score_destination}: {highest_score:.2f}')

# Optional: Analyze sentiment variation (example)
# You can plot or further analyze sentiment scores if available in the dataset

# Example plot of sentiment scores (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.bar(df['Destination'], df['Sentiment_Score'], color='skyblue')
plt.title('Sentiment Scores across Destinations')
plt.xlabel('Destination')
plt.ylabel('Sentiment Score')
plt.ylim(0, 1)  # Assuming sentiment score range is [0, 1]
plt.grid(True)
plt.tight_layout()
plt.show()
