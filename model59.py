"""Scenario: You are working on a project that involves analyzing customer reviews for a
product. You have a dataset containing customer reviews, and your task is to develop a
Python program that calculates the frequency distribution of words in the reviews.
Question: Develop a Python program to calculate the frequency distribution of words in the
customer reviews dataset?"""
import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Sample data (assuming 'review_text' column exists in the DataFrame)
data = {
    'review_id': [1, 2, 3, 4, 5],
    'review_text': [
        "This product is amazing and highly recommended.",
        "Not satisfied with the quality, will not buy again.",
        "Great value for money, excellent customer service.",
        "Poor packaging, product arrived damaged.",
        "Very happy with my purchase, exceeded expectations."
    ]
}

# Create DataFrame
reviews_data = pd.DataFrame(data)

# Function to preprocess text (remove punctuation and convert to lowercase)
def preprocess_text(text):ChildProcessError
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Preprocess each review text and tokenize into words
reviews_data['review_text'] = reviews_data['review_text'].apply(preprocess_text)
words = ' '.join(reviews_data['review_text']).split()  # Split text into words

# Calculate frequency distribution of words
word_freq = Counter(words)

# Display the frequency distribution (optional)
print("Frequency distribution of words in customer reviews:")
for word, freq in word_freq.most_common():
    print(f'{word}: {freq}')

# Optionally, plot the top 20 most common words
plt.figure(figsize=(10, 6))
common_words = word_freq.most_common(20)
words, frequencies = zip(*common_words)
plt.bar(words, frequencies, color='skyblue')
plt.title('Top 20 Most Common Words in Customer Reviews')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
