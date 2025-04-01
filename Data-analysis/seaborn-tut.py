import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample dataset -> seaborn comes with some in built datasets
df = sns.load_dataset('penguins')
df.head()

# scatter plot -> Used to show relationships between two numerical variables.
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.show()

# Line plot 
sns.lineplot(data=df, x="bill_length_mm", y="flipper_length_mm", hue="species")
plt.show()

# Histogram -> To visualize the distribution of a numerical variable
sns.histplot(df["bill_length_mm"], bins=20, kde=True)
plt.show()

# Box plot -> Used to detect outliers and distribution spread.
sns.boxplot(data=df, x="species", y="bill_length_mm")
plt.show()

# Heatmap -> Used to show correlations between numerical variables.
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

# Pair plot -> Shows relationships between multiple numerical variables.
sns.pairplot(df, hue="species")
plt.show()
