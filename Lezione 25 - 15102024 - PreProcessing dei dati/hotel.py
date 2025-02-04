import pandas as pd

# Simulazione di un dataset
data = {
    'Nome Ospite': ['Alice', 'Bob', 'Carla', 'David'],
    'Data Soggiorno': ['2020-07-01', '2020-07-02', None, '2020-07-04'],
    'Durata': [3, None, 1, 2],
    'Recensione Testuale': ['Ottimo servizio', 'Camera sporca', 'Tutto ok', 'Pessimo'],
    'Valutazione': [5, None, 3, 1]
}

df = pd.DataFrame(data)

# Pulizia dei dati
'''
Problema: Quando diverse feature (caratteristiche) hanno scale molto diverse, alcune di esse possono avere un impatto maggiore sulla formazione del modello 
rispetto ad altre. Ad esempio, se stai usando un dataset con una caratteristica che varia da 1 a 10 e un'altra che varia da 1.000 a 10.000, 
il modello potrebbe dare più importanza alla seconda caratteristica solo a causa della sua scala.
Soluzione: Normalizzare le feature porta tutte le variabili su una scala simile, consentendo al modello di trattare ogni caratteristica in modo equo.
'''
df.dropna(subset=['Valutazione'], inplace=True)  # Rimuove righe con valutazioni mancanti
#df['Durata'].fillna(df['Durata'].mean(), inplace=True)  # Imputazione della durata mancante con la media
df['Durata'] = df['Durata'].fillna(df['Durata'].mean())

# Normalizzazione
df['Durata Normalizzata'] = (df['Durata'] - df['Durata'].min()) / (df['Durata'].max() - df['Durata'].min())

# Visualizza il DataFrame preprocessato
print(df)