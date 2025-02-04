import pandas as pd

wines = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                    names=['class','alcol','flavonoidi'],
                    usecols=[0,1,7])
print(wines)

#normalizzazione
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
# la feature target presenta delle classi e non va normalizzata, quindi la rimuoviao dall'array
X = wines.drop("class",axis=1).values
X_norm = mms.fit_transform(X)
print(X_norm[:5])

#normalizzazione con formula
wines_norm = wines.copy()
features = ["alcol","flavonoidi"] # colonne del dataframe da normalizzare
to_norm = wines_norm[features]
wines_norm[features] = (to_norm-to_norm.min())/(to_norm.max()-to_norm.min()) #implementiamo l'algoritmo della normalizzazione
#e lo eseguiamo su tutte le colonne da normalizzare
wines_norm.head()
print(wines_norm)

#standadrizzazione
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X = wines.drop("class",axis=1).values
X_std = ss.fit_transform(X)
print(X_std[:5])

#standadrizzazione con formula
wines_std = wines.copy()
features = ["alcol","flavonoidi"]
to_std = wines_std[features]
wines_std[features] = (to_std - to_std.mean())/to_std.std()
wines_std[:5]