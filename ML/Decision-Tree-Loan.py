# 1. Import Libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 2. Sample Dataset
data = {
    'Age': [25, 45, 35, 33, 52, 23],
    'Income': [50000, 100000, 60000, 58000, 120000, 40000],
    'LoanAmount': [20000, 30000, 25000, 27000, 10000, 22000],
    'CreditScore': [600, 750, 650, 700, 800, 580],
    'Defaulted': [1, 0, 1, 0, 0, 1]   # 1 = Defaulted, 0 = Not Defaulted
}

df = pd.DataFrame(data)

# 3. Features & Label
X = df[['Age', 'Income', 'LoanAmount', 'CreditScore']]
y = df['Defaulted']

# 4. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Train Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 6. Predict
predictions = model.predict(X_test)

# 7. Evaluate
print("Prediction:", predictions)
print(classification_report(y_test, predictions))
