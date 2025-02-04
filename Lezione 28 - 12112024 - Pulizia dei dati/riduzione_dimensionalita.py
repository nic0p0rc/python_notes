#Importare PCA dalla libreria sklearn.decomposition
from sklearn.decomposition import PCA
#Importare pandas per lavorare con i DataFrame
import pandas as pd

#Creare un DataFrame di esempio
dati = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 4, 6, 8, 10],
    'Feature3': [3, 6, 9, 12, 15]
})

#Inizializzare l'oggetto PCA con il numero desiderato di componenti principali (nel nostro esempio, 2)
pca = PCA(n_components=2)

#Ridurre la dimensionalità dei dati utilizzando PCA
dati_ridotti = pca.fit_transform(dati)

#Visualizzare i dati ridotti
print("Dati ridotti:")
print(dati_ridotti)