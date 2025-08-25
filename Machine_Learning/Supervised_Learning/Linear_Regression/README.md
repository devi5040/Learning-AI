# Linear Regression

A simple regression algorithm that models the relationship between input variables (X) and output variable (Y) as a straight line.

- **Best Fit Line**: It is the straight line that most accurately represents the relationship between the independent variable(input) and dependent variable (output).

- _Goal of Best Fit Line_: The goal of linear regression is to find a straight line that minimizes the error between the observed data points and the predicted values. This line helps us predict the dependent variable for new, unseen data.
- **Equation of Best-Fit Line**: The best-fit line is represented by the equation
  y = mx+b
- **Minimizing the error(The least squares method)**: To find best-fit line we use a method called Least Squares.
  The idea behind this method is to minimize the sum of squared differences between the actual values and the predicted values from the line.
  These differences are called residuals.
  Residual = yᵢ − ŷᵢ
  yi is actual observed value
  y^i is predicted value from the line for xi
  Sumofsquarederrors(SSE)=Σ (yi - ŷi)^2
- **Interpretation of Best-Fit Line**

- Slope (m): The slope of the best-fit line indicates how much the dependent variable (y) changes with each unit change in the independent variable (x).
- Intercept (b): The intercept represents the predicted value of y when x = 0. It’s the point where the line crosses the y-axis.

In linear regression some hypothesis are made:

- Assumes Linearity: The method assumes the relationship between the variables is linear.
- Sensitivity to Outliers: Outliers can significantly affect the slope an dintercept, skewing the best-fit line.

## Types of Linear Regression

1. Simple Linear Regression
   It is used when we want to predict a target value(dependent variable) using only one input feature(independent variable).
   Formula: y = θ₀ + θ₁x
2. Multiple Linear Regression
   Multiple linear regression involves more than one independent variable and one dependent variable.
   Formula: ŷ = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ

## Use case of Multiple Linear Regression

1. Real estate pricing
2. Financial Forecasting
3. Agricultural Yield Prediction
4. E-commerce Sales Analysis

---

## Cost function

The difference between predicted value and true value and it is called cost function or loss function.
J = (1/n) Σᵢ₌₁ⁿ (ŷᵢ - yᵢ)²

---

## Gradient Descent for Linear Regression

It is an optimization technique used to train a linear regression model by minimizing the prediction error.
How it works:

- Start with random values for slope and intercept.
- Calculate the error between predicted and actual values.
- Find how much each parameter contributes to the error(gradient).
- Update the parameters in the direction that reduces the error.
- Repeat until the error is as small as possible.

---

## Evaluation metrics for Linear Regression
