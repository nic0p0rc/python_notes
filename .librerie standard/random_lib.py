"""
La libreria `random` in Python è utilizzata per generare numeri casuali e per effettuare operazioni randomiche 
come la selezione di elementi da una lista, la miscelazione di una sequenza e la generazione di numeri casuali 
secondo diverse distribuzioni statistiche.

Ecco alcuni degli utilizzi più comuni della libreria `random`:

1. Generare numeri casuali interi.
2. Generare numeri casuali in virgola mobile.
3. Selezionare un elemento casuale da una lista.
4. Mescolare una lista.
5. Generare numeri casuali secondo una distribuzione specifica.
6. Generare numeri casuali in un intervallo con step specifico.
"""

import random

# 1. Generare numeri casuali interi
"""
La funzione `random.randint(a, b)` restituisce un numero intero casuale N tale che a <= N <= b.
"""
intero_casuale = random.randint(1, 10)
print(f"Numero intero casuale tra 1 e 10: {intero_casuale}")

# 2. Generare numeri casuali in virgola mobile
"""
La funzione `random.random()` restituisce un numero casuale in virgola mobile compreso tra 0.0 e 1.0.
La funzione `random.uniform(a, b)` restituisce un numero casuale in virgola mobile compreso tra a e b.
"""
virgola_mobile_casuale = random.random()
print(f"Numero casuale in virgola mobile tra 0.0 e 1.0: {virgola_mobile_casuale}")

#utilizzo con un ciclo che fa 50 numeri casuali
'''
for i in range(50):
    print(random.random())
'''

virgola_mobile_casuale_interval = random.uniform(1.0, 10.0)
print(f"Numero casuale in virgola mobile tra 1.0 e 10.0: {virgola_mobile_casuale_interval}")

# 3. Selezionare un elemento casuale da una lista
"""
La funzione `random.choice(seq)` restituisce un elemento casuale dalla sequenza non vuota `seq`.
"""
lista = [1, 2, 3, 4, 5]
elemento_casuale = random.choice(lista)
print(f"Elemento casuale dalla lista {lista}: {elemento_casuale}")

# 4. Mescolare una lista
"""
La funzione `random.shuffle(seq)` mescola la sequenza `seq` in loco.
"""
random.shuffle(lista)
print(f"Lista mescolata: {lista}")

# 5. Generare numeri casuali secondo una distribuzione specifica
"""
La libreria `random` fornisce diverse funzioni per generare numeri casuali secondo distribuzioni specifiche.
Ad esempio, `random.gauss(mu, sigma)` genera un numero casuale secondo una distribuzione normale (gaussiana)
con media `mu` e deviazione standard `sigma`.
"""
numero_gaussiano = random.gauss(0, 1)
print(f"Numero casuale secondo una distribuzione gaussiana con media 0 e deviazione standard 1: {numero_gaussiano}")

# 6. Generare numeri casuali in un intervallo con step specifico
"""
La funzione `random.randrange(start, stop[, step])` restituisce un numero casuale selezionato da `range(start, stop, step)`.
"""
range_casuale = random.randrange(0, 11, 2)
print(f"Numero casuale tra 0 e 10 con step di 2: {range_casuale}")


"""
Altre funzioni utili includono `random.sample(population, k)` che restituisce una lista di `k` elementi unici
scelti dalla popolazione, `random.choices(population, weights=None, k=1)` che restituisce una lista di `k` elementi
scelti dalla popolazione con possibilità di ripetizione, e `random.seed(a=None)` che inizializza il generatore di
numeri casuali.
"""

# Esempio di `random.sample`
campione = random.sample(lista, 3)
print(f"Campione di 3 elementi dalla lista {lista}: {campione}")

# Esempio di `random.choices`
scelte = random.choices(lista, k=3)
print(f"3 elementi casuali dalla lista {lista} (con ripetizione): {scelte}")

# Inizializzare il generatore di numeri casuali con un seme specifico
"""
La funzione `random.seed(a)` inizializza il generatore di numeri casuali. Utilizzare un seme specifico permette 
di ottenere una sequenza di numeri casuali riproducibile.
"""
random.seed(42)
print(f"Numero intero casuale con seed 42: {random.randint(1, 10)}")

"""
Questi sono alcuni degli utilizzi più comuni della libreria `random`. Questa libreria offre molte altre funzioni
per la generazione di numeri casuali e operazioni randomiche, utili in vari contesti come giochi, simulazioni,
e test statistici.
"""

