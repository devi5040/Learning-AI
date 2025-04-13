import pandas as pd
from sklearn.neighbors import NearestNeighbors

data = pd.DataFrame({
    'Movie': ['Avengers', 'Iron Man', 'Captain America', 'Thor'],
    'Action': [1, 1, 1, 1],
    'Sci-Fi': [1, 1, 0, 1],
    'Comedy': [0, 0, 0, 0]
})

x = data[['Action','Sci-Fi','Comedy']]

model = NearestNeighbors(n_neighbors=2,metric='cosine')
model.fit(x)

distances, indices = model.kneighbors(x.iloc[[1]])


print("Recommended Movies:")
for i in indices[0][1:]:
    print(data.iloc[i]['Movie'])