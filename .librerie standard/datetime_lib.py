"""
Su python.org --> https://docs.python.org/3/library/datetime.html

Il modulo `datetime` in Python fornisce classi per la manipolazione di date e orari in modo semplice e efficace. 
È estremamente utile per operazioni che coinvolgono calcoli di date, formattazione di stringhe di data/ora e altro ancora.

Ecco alcuni degli utilizzi più comuni del modulo `datetime`:

1. Ottenere la data e l'ora correnti.
2. Creare oggetti `datetime` personalizzati.
3. Manipolare date e orari.
4. Calcolare differenze tra date e orari.
5. Sapere giorno della settimana
"""

import datetime

# 1. Ottenere la data e l'ora correnti
"""
La classe `datetime.datetime` fornisce un metodo `now()` che restituisce un oggetto `datetime` rappresentante 
la data e l'ora correnti.
"""
now = datetime.datetime.now()
print(f"Data e ora correnti: {now}")

# 2. Creare oggetti datetime personalizzati
"""
È possibile creare oggetti `datetime` specificando manualmente anno, mese, giorno, ora, minuti, secondi e microsecondi.
"""
custom_datetime = datetime.datetime(2024, 12, 31, 23, 59, 59)
print(f"Data e ora personalizzata: {custom_datetime}")
custom_datetime = datetime.date(2024, 6, 25)
print(f"Data e ora personalizzata con .date: {custom_datetime}")

# 3. Manipolare date e orari
"""
È possibile aggiungere o sottrarre giorni, ore, minuti, secondi e microsecondi da un oggetto `datetime` utilizzando
gli operatori aritmetici o il metodo `datetime.timedelta`.
"""
future_date = now + datetime.timedelta(days=7)
print(f"Data tra una settimana: {future_date}")
data_passata = now - datetime.timedelta(days=7)
print(data_passata)

# 4. Calcolare differenze tra date e orari
"""
Per calcolare la differenza tra due oggetti `datetime`, è possibile sottrarli direttamente o utilizzare il metodo `datetime.timedelta`.
"""
difference = future_date - now
print(f"Differenza tra le date: {difference}")

# Formattare le date come stringhe
"""
È possibile formattare oggetti `datetime` come stringhe utilizzando il metodo `datetime.strftime(format)`.
"""
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Data e ora formattata: {formatted_date}")

# Sapere giorno della settimana
"""
È possibile sapere il nome del giorno della settimana utilizzando il modulo .weekday() che restituisce i numeri 0,1 ecc in base al giorno 
"""
giorno_della_settimana = now.weekday()
giorno_sett=["lunedi", "mertedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
print(giorno_sett[giorno_della_settimana])

"""
Questi sono alcuni degli utilizzi più comuni del modulo `datetime`. Questo modulo offre molte funzionalità per manipolare
date e orari in modo efficiente, rendendolo essenziale per applicazioni che richiedono gestione del tempo e calcoli
relativi alle date.
"""

