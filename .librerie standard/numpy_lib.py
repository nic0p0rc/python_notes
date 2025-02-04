"""
La libreria `numpy` è una delle più importanti librerie in Python per il calcolo numerico e la manipolazione di array multidimensionali.
Offre strumenti potenti per l'analisi numerica e scientifica. Numpy fornisce supporto per array, funzioni matematiche, algebra lineare,
statistiche e altro ancora.

Ecco alcuni degli utilizzi più comuni della libreria `numpy`:

1. Creare array.
2. Operazioni matematiche sugli array.
3. Funzioni universali (funzioni vettorializzate).
4. Operazioni logiche e di filtro.
5. Algebra lineare e matrici.
"""

import numpy as np

# 1. Creare array
"""
La funzione `np.array()` viene utilizzata per creare array multidimensionali in Numpy. Gli array possono avere uno o più dimensioni.
"""
# Array 1D
array_1d = np.array([1, 2, 3, 4, 5])
print(f"Array 1D: {array_1d}")

# Array 2D (matrice)
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array 2D:\n{array_2d}")

# Creazione di array di numeri consecutivi (arange) o spaziatura uniforme (linspace)
array_arange = np.arange(0, 10, 2)  # Numeri da 0 a 10 con passo di 2
print(f"Array creato con arange: {array_arange}")

array_linspace = np.linspace(0, 1, 5)  # 5 numeri equidistanti tra 0 e 1
print(f"Array creato con linspace: {array_linspace}")

# 2. Operazioni matematiche sugli array
"""
Gli array Numpy permettono di eseguire operazioni matematiche vettorializzate in modo efficiente.
"""
# Operazioni element-wise
array_sum = array_1d + 5  # Aggiunge 5 a ogni elemento
print(f"Aggiunta di 5 a ogni elemento: {array_sum}")

array_mul = array_1d * 2  # Moltiplica ogni elemento per 2
print(f"Moltiplicazione per 2 di ogni elemento: {array_mul}")

# Operazioni tra array
array_addition = array_1d + np.array([5, 4, 3, 2, 1])
print(f"Somma di due array: {array_addition}")

# 3. Funzioni universali (funzioni vettorializzate)
"""
Le funzioni universali (ufunc) sono funzioni che operano elemento per elemento sugli array.
"""
# Esempi di funzioni universali
array_sqrt = np.sqrt(array_1d)  # Radice quadrata di ogni elemento
print(f"Radice quadrata di ogni elemento: {array_sqrt}")

array_sin = np.sin(array_1d)  # Calcola il seno di ogni elemento
print(f"Seno di ogni elemento: {array_sin}")

# 4. Operazioni logiche e di filtro
"""
Le operazioni logiche possono essere utilizzate per creare maschere booleane e filtrare gli array.
"""
# Creare una maschera per filtrare elementi maggiori di 3
mask = array_1d > 3
print(f"Maschera booleana per elementi > 3: {mask}")

filtered_array = array_1d[mask]  # Filtra gli elementi maggiori di 3
print(f"Elementi maggiori di 3: {filtered_array}")

# 5. Algebra lineare e matrici
"""
Numpy fornisce funzioni per l'algebra lineare come moltiplicazione di matrici, determinante e autovalori.
"""
# Moltiplicazione di matrici
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)  # Moltiplicazione di matrici
print(f"Prodotto di matrici:\n{matrix_product}")

# Determinante di una matrice
determinant = np.linalg.det(matrix_a)
print(f"Determinante della matrice: {determinant}")

# Autovalori e autovettori
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
print(f"Autovalori: {eigenvalues}")
print(f"Autovettori:\n{eigenvectors}")

"""
Questi sono alcuni degli utilizzi più comuni della libreria `numpy`. Grazie alla sua efficienza e alle sue funzionalità avanzate,
`numpy` è la base di molte altre librerie scientifiche in Python come `pandas`, `scipy` e `tensorflow`.
"""
