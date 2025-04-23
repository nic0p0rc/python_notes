import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Creazione di un DataFrame di esempio
df = pd.read_csv('iris.csv')

#Creazione e addestramento del modello
kmeans = KMeans(n_clusters = 3, random_state=42)
df['cluster'] = kmeans.fit_predict(df.drop(columns=['species']))

from sklearn.metrics import silhouette_score,calinski_harabasz_score,davies_bouldin_score
silhouette = silhouette_score(df.drop(columns=['species', 'cluster']), df['cluster'])
calinski = calinski_harabasz_score(df.drop(columns=['species', 'cluster']), df['cluster'])
davies = davies_bouldin_score(df.drop(columns=['species', 'cluster']), df['cluster'])

print(f"silhouette_score : {silhouette}")
print(f"calinski: {calinski}")
print(f"davies : {davies}")


#Visualizzazione dei risultati
plt.scatter(df['sepal_length'], df['sepal_width'], c=df['cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering con K-Means')
plt.show()