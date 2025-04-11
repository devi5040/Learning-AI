# Logistic regression - Email spam detection

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv('./dataset/spam.csv')

x = data['text']        # Feature: email content
y = data['label']       # Label: 1 = spam, 0 = not spam

vectorizer = CountVectorizer()      # Convert text to numbers
x_vectorized = vectorizer.fit_transform(x)

