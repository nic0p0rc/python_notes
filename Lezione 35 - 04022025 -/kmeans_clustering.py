import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Creazione di un DataFrame di esempio
data = {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

#Creazione e addestramento del modello
kmeans = KMeans(n_clusters = 3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['x', 'y']])

#Visualizzazione dei risultati
plt.scatter(df['x'], df['y'], c=df['cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering con K-Means')
plt.show()