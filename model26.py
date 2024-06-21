"""A music streaming service wants to analyze the popularity of different music genres listened to by users over the past month. They have a dataset containing the genres of songs played and the number of times each genre has been played. Write a Python program that calculates the frequency distribution of music genres and prints out the most played genre.
"""
import pandas as pd
data={
    'genre': ['Pop', 'Rock', 'Jazz', 'Pop', 'Rock', 'Jazz', 'Classical', 'Pop', 'Rock', 'Pop'],
    'plays': [150, 200, 80, 120, 300, 60, 90, 200, 150, 220]
}
df=pd.DataFrame(data)
print("\n dataset preview:\n",df)
genre_distribution=df.groupby('genre')['plays'].sum()
print("frequency distribution of music generes:",genre_distribution)
most_played_genre=genre_distribution.idxmax()
most_plays=genre_distribution.max()
print(f"\n most played genre:{most_played_genre} with {most_plays} plays")
