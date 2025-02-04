import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Caricamento dei dati
malaysia = pd.read_csv('malaysia_house_price_data_2025.csv')
print(malaysia.head())

#Codifica della colonna Township usando one-hot encoding
categorical_cols = ['Township', 'Area', 'State', 'Tenure', 'Type']
malaysia = pd.get_dummies(malaysia, columns=categorical_cols, drop_first=True)

print(malaysia.head())

#Separazione delle variabili dipendenti e indipendenti
X = malaysia.drop("Median_Price", axis=1).values
'''Questo comando rimuove la colonna chiamata "Median_Price" (che rappresenta il valore medio della casa, 
cioè il target che vogliamo prevedere) dal DataFrame'''

Y = malaysia["Median_Price"].values
'''Questo comando seleziona solo la colonna "Median_Price" dal DataFrame boston, che rappresenta il valore medio 
delle case (target di regressione).'''

#Standardizzazione per diminuire la differenza tra scale
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Divisione in training set e test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

#Importazione modello linear regression
from sklearn.linear_model import LinearRegression

#Creazione e allenamento del modello
ll = LinearRegression()
ll.fit(X_train, Y_train)

#Predizione sul test
Y_pred = ll.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score
#Calcolo MSE
mse = mean_squared_error(Y_test, Y_pred)
print(f"Errore quadratico medio (MSE): {mse:.2f}")

#Calcolo R2
r2 = r2_score(Y_test, Y_pred)
print(f"Coefficiente di determinazione (R2): {r2:.2f}")

#Grafico per visualizzare il risultato
plt.figure(figsize=(8,6))

#Scatter plot per i valori reali e predetti
plt.scatter(Y_test,Y_pred, color='red',edgecolor='k', alpha=0.6, label='Predetti')
plt.scatter(Y_test, Y_test, color='blue', edgecolor='k', alpha=0.6, label='Dati di Test')

# Linea di riferimento ideale (Y_test = Y_pred)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--', linewidth=2, label='Ideale')

# Etichette e legenda
plt.xlabel("Valori Realizzati (Y_test)")
plt.ylabel("Valori Predetti (Y_pred)")
plt.title("Confronto tra Valori Reali e Predetti")
plt.legend()
plt.show()