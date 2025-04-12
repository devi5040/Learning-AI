# Logistic regression - Email spam detection

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import os

filepath = os.path.join('dataset','spam.csv')
data = pd.read_csv(filepath, encoding='latin-1')

x = data['text']        # Feature: email content
y = data['label']       # Label: 1 = spam, 0 = not spam

vectorizer = CountVectorizer()      # Convert text to numbers
x_vectorized = vectorizer.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=42)

# train the model
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# print train data features and labels
print('Train data - Features:')
print(x_train)
print('Train data - Labels:')
print(y_train)

# print test data features and labels
print('Features:')
print(x_test)
print('Labels:')
print(y_pred)

# Evaluate model
print('Accuracy:',accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))