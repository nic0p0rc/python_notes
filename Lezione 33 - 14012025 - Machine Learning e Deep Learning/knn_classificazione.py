import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Creazione di un DataFrame di esempio
data = {'altezza': [150, 160, 170, 180, 190],
        'peso': [50, 60, 70, 80, 90],
        'classe': [0, 0, 1, 1, 1]}

df = pd.DataFrame(data)

#Suddivisione dei dati in allenamento e test
X = df[['altezza', 'peso']]
Y = df['classe']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Creazione e addestramento del modello
model = KNeighborsClassifier(n_neighbors=2)
model.fit(X_train, Y_train)

#Previsione sui dati di test
Y_pred = model.predict(X_test)

#Valutazione delle prestazioni
accuracy = accuracy_score(Y_test, Y_pred)
print (f"Accuracy: {accuracy:.2f}")