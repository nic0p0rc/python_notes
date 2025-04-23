import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Caricamento del dataset Iris in un DataFrame Pandas
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
                     sep='\\s+')

# Calcolo della matrice di correlazione
correlation_matrix = df.corr()

# Visualizzazione della matrice di correlazione con una heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matrice di Correlazione - Dataset Iris")
plt.show()
