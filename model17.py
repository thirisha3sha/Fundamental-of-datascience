""""You are a data scientist working in an e-commerce company. Your team wants to classify customer reviews as positive or negative to analyze sentiment and improve customer service. Your task is to build a support vector machine (SVM) classifier for sentiment analysis. Write Python code to load the review data, preprocess it, split it into training and testing sets, train an SVM classifier, and evaluate its performance using metrics such as accuracy and F1-score.
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score

# Sample customer reviews and their corresponding sentiments (0 for negative, 1 for positive)
reviews = [
    "This product is great and works perfectly.",
    "Very disappointed with the quality and performance.",
    "Excellent service and fast delivery!",
    "I regret buying this. It's not worth the money.",
    "The customer support was unhelpful and rude."
]
sentiments = [1, 0, 1, 0, 0]

# Initialize NLTK resources (download if not already downloaded)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Preprocessing function
def preprocess(text):
    # Tokenization
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Return preprocessed text as a single string
    return ' '.join(words)

# Preprocess the reviews
preprocessed_reviews = [preprocess(review) for review in reviews]

# Vectorize the preprocessed text data using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_reviews)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, sentiments, test_size=0.2, random_state=42)

# Initialize SVM classifier
svm_classifier = SVC(kernel='linear', random_state=42)

# Train the SVM classifier
svm_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = svm_classifier.predict(X_test)

# Calculate accuracy and F1-score
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print results
print(f"Accuracy: {accuracy:.2f}")
print(f"F1-score: {f1:.2f}")
