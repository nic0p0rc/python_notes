
# Preprocessing dei Dati con Python

La **pre-elaborazione dei dati** è una fase cruciale nel ciclo di vita di un progetto di *machine learning* o *data analysis*. Prepara i dati grezzi per l'analisi o la modellazione, migliorando la qualità e l'efficacia dei risultati. Di seguito una panoramica dei passaggi comuni di preprocessing e alcuni esempi di codice Python utilizzando librerie popolari come `pandas`, `numpy` e `scikit-learn`.

## 1. Importare i Dati
Il primo passo è caricare i dati da un file o una fonte. Questo può essere un file CSV, Excel, un database SQL, o un'API web.

```python
import pandas as pd

# Carica dati da un file CSV
df = pd.read_csv('dataset.csv')

# Visualizza le prime righe
print(df.head())
```

## 2. Gestire i Valori Mancanti
I dati reali spesso contengono valori mancanti o nulli. È possibile gestirli eliminando le righe o colonne con valori mancanti, oppure sostituendoli con valori appropriati.

- **Rimuovere valori mancanti:**
```python
# Elimina righe con valori mancanti
df_cleaned = df.dropna()

# Elimina colonne con valori mancanti
df_cleaned = df.dropna(axis=1)
```

- **Sostituire valori mancanti:**
```python
# Sostituisce valori mancanti con la media della colonna
df['colonna'].fillna(df['colonna'].mean(), inplace=True)
```

## 3. Codifica delle Variabili Categoriali
Se hai variabili categoriali (es. colori, città), possono essere convertite in numeri usando tecniche come la **label encoding** o **one-hot encoding**.

- **Label Encoding (Scikit-learn):**
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['categoria_encoded'] = le.fit_transform(df['categoria'])
```

- **One-Hot Encoding (Pandas):**
```python
df_encoded = pd.get_dummies(df, columns=['categoria'])
```

## 4. Normalizzazione o Standardizzazione dei Dati
La normalizzazione e la standardizzazione sono tecniche utilizzate per ridimensionare i dati numerici. La **standardizzazione** trasforma i dati per avere media 0 e deviazione standard 1, mentre la **normalizzazione** li trasforma in un intervallo specifico, come [0, 1].

- **Standardizzazione (Z-score):**
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
```

- **Normalizzazione (Min-Max Scaling):**
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
```

## 5. Rimozione delle Colonne Irrilevanti o Duplicate
Alcune colonne possono essere ridondanti o non rilevanti per l'analisi. Puoi rimuoverle facilmente.

```python
# Rimuove colonne specifiche
df = df.drop(['colonna1', 'colonna2'], axis=1)

# Rimuove colonne duplicate
df = df.loc[:,~df.columns.duplicated()]
```

## 6. Suddivisione del Dataset in Training e Test Set
Per allenare un modello, è importante dividere i dati in un **training set** e un **test set**.

```python
from sklearn.model_selection import train_test_split

# Dividi il dataset in 80% training e 20% test
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2, random_state=42)
```

## 7. Rimozione o Trattamento degli Outlier
Gli outlier possono distorcere le analisi e i modelli di machine learning. Un metodo semplice per rilevare outlier è l'uso di **Z-score** o **Interquartile Range (IQR)**.

- **Rilevamento degli outlier con Z-score:**
```python
from scipy import stats

# Identifica gli outlier in base a Z-score > 3 o < -3
df_no_outliers = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
```

- **Rilevamento degli outlier con IQR:**
```python
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Filtra i dati all'interno dell'IQR
df_no_outliers = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
```

## 8. Riduzione della Dimensionalità
Per dataset con molte feature, puoi ridurre il numero di variabili usando tecniche come la **PCA (Principal Component Analysis)**.

```python
from sklearn.decomposition import PCA

# Applica PCA per ridurre a 2 componenti
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(df), columns=['PC1', 'PC2'])
```

## 9. Bilanciamento del Dataset (Optional)
Se il tuo dataset è sbilanciato (per esempio, ci sono più istanze di una classe rispetto a un'altra), puoi usare tecniche come **oversampling** o **undersampling**.

- **Oversampling con SMOTE (Synthetic Minority Over-sampling Technique):**
```python
from imblearn.over_sampling import SMOTE

smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
```

---

### Conclusione
La pre-elaborazione dei dati è un passo essenziale per ottenere modelli robusti e risultati accurati. Una preparazione corretta ti aiuterà a migliorare le prestazioni del tuo modello.
