import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#importazione del modello
df = pd.read_csv('iris.csv')

#esplora il dataset
#pandas data serie una var, Data Frame(df) più var
print(df.head())
print(df.describe())

# Selezione delle caratteristiche per la regressione lineare
X = df[['petal_length']] # Variabile indipendente
y = df['petal_width'] # Variabile dipendente

#divisiane dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione e addestramento del modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Predizione sul test set
y_pred = model.predict(X_test)

# Valutazione del modello
# Calcolo MSE
mse = mean_squared_error(y_test, y_pred)
print(f"Errore quadratico medio (MSE): {mse:.2f}")

# Calcolo R²
r2 = r2_score(y_test, y_pred)
print(f"Coefficiente di determinazione (R²): {r2:.2f}")


# Visualizzazione della regressione lineare
plt.figure(figsize=(8,5))
sns.scatterplot(x=X_test['petal_length'], y=y_test, label='Dati reali')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regressione Lineare')
plt.xlabel('Lunghezza Sepalo (cm)')
plt.ylabel('Lunghezza Petalo (cm)')
plt.title('Regressione Lineare su Iris Dataset')
plt.legend()
plt.show()