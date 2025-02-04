"""
Le lambda functions in Python sono funzioni anonime e senza nome definite in modo conciso in una singola espressione.
Sono utilizzate per definire funzioni di supporto semplici che non richiedono una dichiarazione di funzione formale.
"""

# Esempio di lambda function per calcolare il quadrato di un numero
"""
La lambda function 'quad' prende un argomento 'x' e restituisce 'x * x', cioè il quadrato di 'x'.
"""
quad = lambda x: x * x
print(quad(5))  # Output: 25

# Utilizzo di map con una lambda function per calcolare i quadrati di una lista
"""
La funzione 'map' applica la lambda function a ciascun elemento della lista 'lista' per calcolarne i quadrati.
"""
lista = [1, 2, 3, 4, 5]
quadrati = list(map(lambda x: x * x, lista))
print(quadrati)  # Output: [1, 4, 9, 16, 25]

# Lambda function per verificare se un numero è pari, utilizzata con filter
"""
La lambda function controlla se un numero 'x' è pari utilizzando l'operatore modulo '%'.
Viene utilizzata con 'filter' per filtrare solo i numeri pari dalla lista 'lista'.
"""
pari = list(filter(lambda x: x % 2 == 0, lista))
print(pari)  # Output: [2, 4]

# Lambda function per filtrare parole in maiuscolo da una lista, utilizzata con filter
"""
La lambda function verifica se una parola 'x' è completamente in maiuscolo con il metodo 'isupper()'.
Viene utilizzata con 'filter' per selezionare solo le parole in maiuscolo dalla lista 'parole'.
"""
parole = ["cane", "GATTO", "ciao"]
parole_maiuscole = list(filter(lambda x: x.isupper(), parole))
print(parole_maiuscole)  # Output: ['GATTO']

# Lambda function per convertire tutte le parole in maiuscolo, utilizzata con map
"""
La lambda function 'lambda x: x.upper()' converte una parola 'x' in maiuscolo utilizzando il metodo 'upper()'.
Viene utilizzata con 'map' per applicare la conversione a tutte le parole nella lista 'parole'.
"""
parole_upper = list(map(lambda x: x.upper(), parole))
print(parole_upper)  # Output: ['CANE', 'GATTO', 'CIAO']

# Lambda function per calcolare la somma di una lista di numeri, utilizzata con reduce
"""
La lambda function 'lambda x, y: x + y' prende due argomenti 'x' e 'y' e restituisce la loro somma.
Viene utilizzata con 'reduce' dalla libreria 'functools' per calcolare la somma di tutti gli elementi nella lista 'numeri'.
"""
from functools import reduce
numeri = [1, 2, 3, 4, 5]
somma = reduce(lambda x, y: x + y, numeri)
print(somma)  # Output: 15
