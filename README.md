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

## Supervised Learning

The model learns from labeled data (inputs + known outputs).
Goal: Predict outputs for new, unseen data.
Types of Problems:

- Regression: Predict continuous values (e.g. house prices, temperature)
- Classification: Predict categories(e.g. spam/not spam, disease yes/no)

1. Linear Regression
   A simple regression algorithm that models the relationship between input variables (X) and output variable (Y) as a straight line.
   **Best Fit Line**: It is the straight line that most accurately represents the relationship between the independent variable(input) and dependent variable (output).
   _Goal of Best Fit Line_: The goal of linear regression is to find a straight line that minimizes the error between the observed data points and the predicted values. This line helps us predict the dependent variable for new, unseen data.
   **Equation of Best-Fit Line**: The best-fit line is represented by the equation
   y = mx+b
   **Minimizing the error(The least squares method)**: To find best-fit line we use a method called Least Squares.
   The idea behind this method is to minimize the sum of squared differences between the actual values and the predicted values from the line.
   These differences are called residuals.
   Residual = y_i - u_hat_i
   yi is actual observed value
   y^i is predicted value from the line for xi
   Sumofsquarederrors(SSE)=Σ (yi - ŷi)^2
   **Interpretation of Best-Fit Line**

   - Slope (m): The slope of the best-fit line indicates how much the dependent variable (y) changes with each unit change in the independent variable (x).
   - Intercept (b): The intercept represents the predicted value of y when x = 0. It’s the point where the line crosses the y-axis.

   In linear regression some hypothesis are made:

   - Assumes Linearity: The method assumes the relationship between the variables is linear.
   - Sensitivity to Outliers: Outliers can significantly affect the slope an dintercept, skewing the best-fit line.
