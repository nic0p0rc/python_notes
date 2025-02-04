import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Creazione di un DataFrame di esempio
data = {'ore_studio': [1,2,3,4,5,6,7,8,9,10],
        'punteggio': [1, 4, 9, 16, 25, 36, 49, 64, 31, 100]}
df = pd.DataFrame (data)

#Suddivisione dei dati in allenamento e test
X = df[['ore_studio']]
y = df ['punteggio']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

#Trasformazione polinomiale dei dati
poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

#Creazione e addestramento del modello di regressione polinomiale
model = LinearRegression()
model.fit(X_poly_train, y_train)

#Previsione sui dati di test
y_pred  = model.predict(X_poly_test)

#Visualizzazione dei risultati
plt.scatter (X_test, y_test, color='blue', label='Dati reali')
plt.plot (X_test, y_pred, color='red', linewidth=2, label='Predizioni')
plt.xlabel('Ore di studio')
plt.ylabel('Punteggio')
plt.title('Regressione Polinomiale')
plt.legend()
plt.show()