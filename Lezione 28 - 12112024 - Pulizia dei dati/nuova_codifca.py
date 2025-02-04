import pandas as pd
import numpy as np

shirts = pd.read_csv("https://raw.githubusercontent.com/ProfAI/ml00/master/2%20-%20Datasets%20e%20data%20preprocessing/data/shirts.csv",index_col=0)

#da etichette a numero (variabili ordinarie)
X = shirts.values
size_mapping = {"S":0,"M":1,"L":2,"XL":3} #dizionario che ordina le misure
fmap = np.vectorize(lambda t:size_mapping[t])
X[:,0] = fmap(X[:,0])
print(X[:5])

#one-hot encoder (variabili categoriche)
shirts_copia = shirts.copy()
dati_codificati = pd.get_dummies(shirts_copia, columns=['colore'])
print(dati_codificati)