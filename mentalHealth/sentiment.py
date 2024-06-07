import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Importing the dataset
dataset = pd.read_csv(r'C:\Users\Admin\Desktop\Hackthon\PyHack24-Dominators-15\mentalHealth\startup_sentiment.tsv', delimiter='\t', quoting=3)

# Keep only the first 10050 rows
dataset = dataset.iloc[:10051]

# Cleaning the texts
corpus = []
for i in range(0, 10051):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Summary'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
cv = CountVectorizer(max_features=None)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Training the Logistic Regression model on the Training set
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Function to clean and preprocess a single review
def preprocess_review(review):
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    return review

# Function to predict the sentiment of a single review
def predict_sentiment(review):
    processed_review = preprocess_review(review)
    review_vector = cv.transform([processed_review]).toarray()
    prediction = classifier.predict(review_vector)
    return prediction[0]

# # User input
# user_review = input("Enter a review: ")
# sentiment = predict_sentiment(user_review)

# # Output the result
# sentiment_dict = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
# print(f"The sentiment of the review is: {sentiment_dict[sentiment]}")