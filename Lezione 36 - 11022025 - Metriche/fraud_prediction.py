# II Versione (aggiunto grafico di confronto e valutazione della matrice di correlazione)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score
import seaborn as sns

# Caricamento dataset reale (Credit Card Fraud Detection)
df = pd.read_csv('creditcard.csv')

# Analisi preliminare
print(df.head())
print(df.info())
print(df.describe())

print(f"Shape del dataset: {df.shape}")  # Dovrebbe mostrare (n_righe, n_colonne)
print(df.head())  # Controlla se ci sono dati
print(df.columns)  # Controlla i nomi delle colonne

print("Valori NaN nel dataset:")
print(df.isnull().sum())

# Istogramma delle classi
sns.countplot(x=df['Class'])
plt.title("Distribuzione delle classi")
plt.show()

# Analisi della correlazione
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
plt.title("Matrice di correlazione")
plt.show()

# Feature e Target
X = df.drop(columns=['Class'])  # Feature, ovvero elimina la colonna Class
y = df['Class']  # Target

# Normalizzazione delle feature
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Separazione Feature-Target
X = df.drop(columns=['Class'])  # Feature
y = df['Class']  # Target

# Normalizzazione delle feature
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Divisione in dati di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definizione del modello
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),  # Primo strato nascosto
    layers.Dense(32, activation='relu'),  # Secondo strato nascosto
    layers.Dense(1, activation='sigmoid')  # Strato di output
])

# Compilazione del modello
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Addestramento del modello
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Valutazione del modello
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')

# Predizioni sul test set
y_pred = (model.predict(X_test) > 0.5).astype('int32')

# Predizioni sul test set
y_pred = (model.predict(X_test) > 0.5).astype('int32')



# Calcolo metriche avanzate
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Precision: {precision}, Recall: {recall}, F1-score: {f1}')

# Visualizzazione del modello
model.summary()

# Alternativa a plot_model: Grafico della perdita e accuratezza
plt.figure(figsize=(12, 5))

# Grafico della perdita
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Andamento della Perdita')

# Grafico dell'accuratezza
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Andamento Accuratezza')

# Grafico delle predizioni vs reali
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Valori reali')
plt.scatter(range(len(y_pred)), y_pred, label='Predizioni')
plt.xlabel('Indice dei dati')
plt.ylabel('Classe')
plt.legend()
plt.title('Confronto tra valori reali e predetti')

plt.show()