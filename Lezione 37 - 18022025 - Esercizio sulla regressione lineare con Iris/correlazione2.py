# Ricaricare il dataset e correggere eventuali errori nel formato
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Caricare il dataset Iris
iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris["species"] = iris.target # Aggiungere la colonna delle classi

# Creare uno scatterplot matrix (pairplot) per visualizzare la correlazione tra le variabili
sns.pairplot(df_iris, hue="species", markers=["o", "s", "D"], diag_kind="hist", palette="husl")

# Mostrare il grafico
plt.suptitle("Scatter Plot delle Correlazioni - Dataset Iris", y=1.02)
plt.show()
