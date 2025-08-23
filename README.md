# Learning-AI

Tracking my learning through this repo

## What is Machine Learning (ML)?

Machine Learning is a branch of Artificial Intelligence where computers learn patterns from data and make predictions or decisions without being explicitly programmed.

---

---

## Types Of ML

1. Supervised Learning
   The model learns from labeled data (input + known output)
   Example
   Predicting house prices (regression)
   Spam email detection (classification)
2. Unsupervised Learning
   The model learns from unlabeled data (only inputs, no outputs)
   Example:
   Customer segmentation (clustering)
   Dimensionality reduction (PCA)
3. Reinforcement Learning
   The model learns by trial and error, receiving rewards or penalties.
   Example:
   Game AI (chess, Go, video games)
   self-driving cars

---

---

## ML Workflow

1. Data Collection: Gather data from sources like files, databases, APIs.
2. Data Preprocessing: Clean the data, handle missing values, remove duplicates, scale features.
3. Feature Engineering: Select or create important features to improve model performance.
4. Modeling: Choose and train a machine learning algorithm.
5. Evaluation: Test the model using metrics to see how well it performs on unseen data.

---

---

## Evaluation Metrics

a. Classification Metrics (for predicting categories)

- Accuracy: (correct predictions/Total predictions) - not reliable for imbalanced datasets.
- Precision: (true positives/predicted positives) - how many predicted positives are actually positive.
- Recall (sensitivity): (true positives/Actual positives) - how many actual positives did the model catch.
- F1-score: Harmonic mean of precision and recall:
  F1=2*((precision*Recall)/(precision+recall))
- ROC-AUC: Measures how well the model separates classes across thresholds. AUC=1 is perfect.

---

b. Regression Metrics (for predicting continuous values)

- Mean squarred error: Average squared difference between predicted and actual values.
- Root Mean Squared Error: Square root of MSE; same units as target variable.
- Mean Absolute Error: Average absolute difference between predicted and actual values.
- R-squared: Fraction of variance in target variable explained by the model. 1 is perfect fit, model predicts no better than mean.

---

---
