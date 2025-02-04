import pandas as pd

iris = pd.read_csv('iris.csv')
species = iris['species']

dati_finali = pd.get_dummies(species)
print(dati_finali)