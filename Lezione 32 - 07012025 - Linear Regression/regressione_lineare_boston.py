import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caricamento dei dati
boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
                     sep='\\s+', usecols=[5, 13], names=["RM", "MEDV"])
print(boston.head())

# Separazione delle variabili indipendenti e dipendenti
X = boston.drop("MEDV", axis=1).values
Y = boston["MEDV"].values

# Divisione in training set e test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Importazione del modello LinearRegression
from sklearn.linear_model import LinearRegression

# Creazione e allenamento del modello
ll = LinearRegression()
ll.fit(X_train, Y_train)

# Predizione sul test set
Y_pred = ll.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

# Calcolo MSE
mse = mean_squared_error(Y_test, Y_pred)
print(f"Errore quadratico medio (MSE): {mse:.2f}")

# Calcolo R²
r2 = r2_score(Y_test, Y_pred)
print(f"Coefficiente di determinazione (R²): {r2:.2f}")

# Grafico per visualizzare i risultati
plt.figure(figsize=(8, 6))

# Scatter plot per i valori reali e predetti
plt.scatter(Y_test, Y_pred, color='orange', edgecolor='k', alpha=0.6, label='Predetti')
plt.scatter(Y_test, Y_test, color='blue', edgecolor='k', alpha=0.6, label='Dati di Test')

# Linea di riferimento ideale (Y_test = Y_pred)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--', linewidth=2, label='Ideale')

# Etichette e legenda
plt.xlabel("Valori Realizzati (Y_test)")
plt.ylabel("Valori Predetti (Y_pred)")
plt.title("Confronto tra Valori Reali e Predetti")
plt.legend()
plt.show()



