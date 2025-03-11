import pandas as pd
# creating the series
data = [1,2,3,4,5]
series = pd.Series(data)
print(series)

# custom index
a = [10, 20, 30, 40, 50]
b = ['hello','hi','good','thanks','cool']
s = pd.Series(b,index=a)
print(s)

# some operations
print(series*8)
print(series+10)
print(series.mean())

#####################################################################
#####################################################################
# PANDAS DATAFRAME  
#####################################################################
#####################################################################
# A DataFrame is a two-dimensional table (rows and columns), similar to an Excel spreadsheet or SQL table.
data = {
    'Name':['Alice','Chandler','Joey'],
    'Age':[22,23,25],
    'Salary':[12000, 23000, 29000]
}
dataframe = pd.DataFrame(data)
print(dataframe)
# adding custom index
dataframe.index=['A','B','C']
print(dataframe)

# Reading and writing csv data
df = pd.read_csv('data.csv')    # reading
df.to_csv('data.csv',index=False)   # writing

# Reading and writing excel sheet
df = pd.read_excel('data.xlsx')     # reading
df.to_excel('data.xlsx',index=False)    # writing

# Accessing data elements
# selecting columns
print(df['Name'])  # Selecting a single column
print(df[['Name', 'Salary']])  # Selecting multiple columns

# selecting rows
print(df.loc['A'])  # Select row by label
print(df.iloc[1])   # Select row by index position

# filtering
print(df[df['Age'] > 25])  # Get rows where Age > 25

# Modifying dataframe
df['Bonus'] = df['Salary'] * 0.1  # Creates a new column
df['Salary'] = df['Salary'] + 5000  # Updating column
df.drop('Bonus', axis=1, inplace=True)  # Removes the  column
df.drop('A', axis=0, inplace=True)  # Removes row 

#Data Aggregation and Statistics
print(df.describe())  # Summary statistics
print(df.mean())      # Mean of numerical columns
print(df.median())    # Median of numerical columns
print(df.std())       # Standard deviation
print(df['Age'].min()) # Minimum age
print(df['Age'].max()) # Maximum age
grouped = df.groupby('Age').mean()  # Group by Age and calculate mean
print(grouped)

# Handling Missing Data
print(df.isnull().sum())  # Count missing values in each column
df.fillna(0, inplace=True)  # Replace NaN values with 0
df.dropna(inplace=True)  # Removes rows with NaN values

# Sorting and Reordering Data
df_sorted = df.sort_values(by='Salary', ascending=False)  # Sort by column in descending order
print(df_sorted)

df = df[['Salary', 'Age', 'Name']]  # Change column order

# Merging and Joining DataFrames
#Concatenating DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_combined = pd.concat([df1, df2])
print(df_combined)

# Merging DataFrames (SQL-like Join)
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Salary': [50000, 60000, 70000]})
df_merged = pd.merge(df1, df2, on='ID', how='inner')  # Inner join
print(df_merged)