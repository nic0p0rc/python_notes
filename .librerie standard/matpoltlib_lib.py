"""
La libreria `matplotlib` è una libreria Python utilizzata per creare grafici e visualizzazioni di dati. È ampiamente utilizzata
in ambiti scientifici, statistici e analitici grazie alla sua flessibilità e facilità d'uso.

Ecco alcuni degli utilizzi più comuni della libreria `matplotlib`:

1. Creare grafici lineari.
2. Creare grafici a dispersione (scatter).
3. Creare istogrammi.
4. Creare grafici a barre.
5. Personalizzare grafici (etichette, titoli, legende, ecc.).
6. Salvare grafici come immagini.
"""

import matplotlib.pyplot as plt
import numpy as np

# 1. Creare grafici lineari
"""
La funzione `plt.plot()` viene utilizzata per creare grafici lineari. 
È possibile aggiungere etichette, titoli e una griglia al grafico.
"""
x = np.linspace(0, 10, 100)  # Crea 100 punti equidistanti tra 0 e 10
y = np.sin(x)

plt.figure(figsize=(8, 5))  # Imposta la dimensione del grafico
plt.plot(x, y, label='sin(x)', color='blue')  # Traccia sin(x) con etichetta
plt.title("Grafico Lineare di sin(x)")  # Aggiungi un titolo
plt.xlabel("x")  # Etichetta per l'asse X
plt.ylabel("sin(x)")  # Etichetta per l'asse Y
plt.legend()  # Mostra la legenda
plt.grid(True)  # Aggiungi una griglia
plt.show()

# 2. Creare grafici a dispersione (scatter)
"""
La funzione `plt.scatter()` viene utilizzata per creare grafici a dispersione. 
Può essere utile per rappresentare relazioni tra due variabili.
"""
x = np.random.rand(50)  # Genera 50 valori casuali per l'asse X
y = np.random.rand(50)  # Genera 50 valori casuali per l'asse Y

plt.scatter(x, y, color='red', label='Punti casuali')  # Crea un grafico scatter
plt.title("Grafico a Dispersione")  # Aggiungi un titolo
plt.xlabel("x")  # Etichetta per l'asse X
plt.ylabel("y")  # Etichetta per l'asse Y
plt.legend()  # Mostra la legenda
plt.show()

# 3. Creare istogrammi
"""
La funzione `plt.hist()` viene utilizzata per creare istogrammi, utili per rappresentare distribuzioni di dati.
"""
data = np.random.randn(1000)  # Genera 1000 numeri casuali da una distribuzione normale

plt.hist(data, bins=30, color='purple', edgecolor='black')  # Crea un istogramma con 30 intervalli
plt.title("Istogramma della Distribuzione Normale")  # Aggiungi un titolo
plt.xlabel("Valore")  # Etichetta per l'asse X
plt.ylabel("Frequenza")  # Etichetta per l'asse Y
plt.show()

# 4. Creare grafici a barre
"""
La funzione `plt.bar()` viene utilizzata per creare grafici a barre, utili per rappresentare dati categorici.
"""
categorie = ['A', 'B', 'C', 'D', 'E']
valori = [5, 7, 3, 8, 4]

plt.bar(categorie, valori, color='orange', edgecolor='black')  # Crea un grafico a barre
plt.title("Grafico a Barre")  # Aggiungi un titolo
plt.xlabel("Categoria")  # Etichetta per l'asse X
plt.ylabel("Valore")  # Etichetta per l'asse Y
plt.show()

# 5. Personalizzare grafici
"""
Matplotlib offre molte opzioni per personalizzare i grafici, inclusi colori, stili di linea e annotazioni.
"""
plt.plot(x, y, linestyle='--', marker='o', color='green', label='sin(x)')  # Personalizza lo stile
plt.title("Grafico Personalizzato")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.annotate('Punto massimo', xy=(0.5, 0.8), xytext=(1.5, 0.9),
             arrowprops=dict(facecolor='black', arrowstyle='->'))  # Aggiungi un'annotazione
plt.legend()
plt.show()

# 6. Salvare grafici come immagini
"""
La funzione `plt.savefig()` permette di salvare i grafici in vari formati come PNG, PDF, ecc.
"""
plt.plot(x, y, label='sin(x)', color='blue')
plt.title("Grafico Salvato")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.savefig("grafico_lineare.png", dpi=300)  # Salva il grafico come immagine PNG con alta risoluzione
plt.show()

"""
Questi esempi coprono i principali utilizzi di `matplotlib`. La libreria è altamente personalizzabile e può essere 
combinata con altre librerie come `numpy` e `pandas` per analisi e visualizzazioni più avanzate.
"""
