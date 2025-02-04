"""
Su python.org --> https://docs.python.org/3/library/time.html

Il modulo `time` in Python fornisce varie funzioni per la manipolazione del tempo. 
È utile per ottenere il tempo corrente, misurare la durata di esecuzione del codice, 
ritardare l'esecuzione del programma e formattare date e orari.

Ecco alcuni degli utilizzi più comuni del modulo `time`:

1. Ottenere il tempo corrente.
2. Ritardare l'esecuzione del programma.
3. Misurare la durata di esecuzione del codice.
4. Formattare date e orari.
"""

import time

# 1. Ottenere il tempo corrente
"""
La funzione `time.time()` restituisce il tempo corrente in secondi dall'epoca (1 gennaio 1970).
La funzione `time.localtime()` restituisce un oggetto `struct_time` che rappresenta l'ora locale corrente.
La funzione `time.gmtime()` restituisce un oggetto `struct_time` che rappresenta l'ora UTC corrente.
"""
tempo_corrente = time.time()
print(f"Tempo corrente in secondi dall'epoca: {tempo_corrente}")

ora_locale = time.localtime()
print(f"Ora locale corrente: {time.strftime('%Y-%m-%d %H:%M:%S', ora_locale)}")

ora_utc = time.gmtime()
print(f"Ora UTC corrente: {time.strftime('%Y-%m-%d %H:%M:%S', ora_utc)}")

# 2. Ritardare l'esecuzione del programma
"""
La funzione `time.sleep(seconds)` sospende l'esecuzione del programma per il numero di secondi specificato.
"""
print("Attendere 2 secondi...")
time.sleep(2)
print("2 secondi trascorsi.")

# 3. Misurare la durata di esecuzione del codice
"""
Le funzioni `time.perf_counter()` e `time.process_time()` sono utilizzate per misurare intervalli di tempo.
`time.perf_counter()` restituisce un valore ad alta risoluzione del tempo del contatore, adatto per misurare intervalli brevi.
`time.process_time()` restituisce il tempo del processore utilizzato dal programma.
"""
start = time.perf_counter()
# Esegui qualche operazione
time.sleep(1)
end = time.perf_counter()
print(f"Durata dell'operazione: {end - start} secondi")

# 4. Formattare date e orari
"""
La funzione `time.strftime(format, t)` restituisce una stringa che rappresenta l'ora, formattata secondo il parametro `format`.
La funzione `time.strptime(string, format)` analizza una stringa che rappresenta un'ora secondo il parametro `format` e restituisce un oggetto `struct_time`.
"""
formattazione = time.strftime('%Y-%m-%d %H:%M:%S', ora_locale)
print(f"Data e ora formattata: {formattazione}")

data_stringa = '2024-06-21 15:30:00'
data_oggetto = time.strptime(data_stringa, '%Y-%m-%d %H:%M:%S')
print(f"Oggetto struct_time: {data_oggetto}")

"""
Questi sono alcuni degli utilizzi più comuni del modulo `time`. Questo modulo offre molte funzioni per la manipolazione del tempo,
che sono utili per una varietà di compiti, come la misurazione delle prestazioni del codice, la gestione dei ritardi
nell'esecuzione del programma e la formattazione di date e orari.
"""
