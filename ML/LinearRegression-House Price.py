# Predict the house price by the features like size, number of bedrooms, age of the house

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#sample data 
data = {
    "Size":[1400, 1600, 1700, 1875],
    "Bedrooms": [3,4,3,4],
    "Age":[20,15,18,10],
    "Price":[245000,312000,279000, 308000]
}

df = pd.DataFrame(data)

# Features and Label
x = df[['Size','Bedrooms','Age']] # features
y = df['Price']     # label

# split the data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state=1)

# train model
model = LinearRegression()
model.fit(x_train,y_train)

# predictions
predictions = model.predict(x_test)
print('Test dataset:',x_test)

# Evaluate
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test,predictions)

print("Predictions:", predictions)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# For new house
new_house_df = pd.DataFrame([[1500, 3, 12]], columns=['Size', 'Bedrooms', 'Age'])
est =model.predict(new_house_df)

print('For new house estimated price is:', est)