# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 2. Sample Data (Annual Income vs Spending Score)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6],
    'Annual Income (k$)': [15, 16, 17, 80, 85, 88],
    'Spending Score (1-100)': [39, 81, 6, 77, 40, 95]
}
df = pd.DataFrame(data)

# 3. Features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# 4. KMeans Clustering
kmeans = KMeans(n_clusters=2, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# 5. Visualize Clusters
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segmentation')
plt.show()
