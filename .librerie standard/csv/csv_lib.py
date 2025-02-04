"""
Su python.org --> https://docs.python.org/3/library/csv.html

La libreria `csv` in Python è utilizzata per leggere e scrivere file CSV (Comma-Separated Values). I file CSV 
sono file di testo semplice che contengono dati tabulari, in cui ogni riga rappresenta un record e ogni campo 
è separato da una virgola o da un altro delimitatore.

Ecco alcuni degli utilizzi più comuni della libreria `csv`:

1. Leggere un file CSV.
2. Scrivere un file CSV.
3. Utilizzare un delimitatore diverso.
4. Utilizzare `DictReader` e `DictWriter` per leggere e scrivere file CSV come dizionari.
5. Gestire la codifica UTF-8 nei file CSV.
"""

import csv

# Creazione di un file CSV di esempio
dati = [
    ['Nome', 'Età', 'Città'],
    ['Alice', '30', 'Roma'],
    ['Bob', '25', 'Milano'],
    ['Charlie', '35', 'Napoli']
]

# Scrivere i dati in un file CSV
"""
La funzione `csv.writer(file)` crea un oggetto writer che converte i dati in formato CSV.
Il metodo `writer.writerow(row)` scrive una singola riga nel file CSV.
Il metodo `writer.writerows(rows)` scrive più righe nel file CSV.
"""
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dati)
print("File CSV 'example.csv' creato con successo.")

# 1. Leggere un file CSV
"""
La funzione `csv.reader(file)` crea un oggetto reader che itera sulle righe del file CSV.
"""
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2. Scrivere un file CSV
"""
La funzione `csv.writer(file)` crea un oggetto writer che converte i dati in formato CSV.
Il metodo `writer.writerow(row)` scrive una singola riga nel file CSV.
"""
nuovi_dati = [
    ['Nome', 'Età', 'Città'],
    ['David', '28', 'Torino'],
    ['Eva', '22', 'Firenze']
]
with open('example2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(nuovi_dati)
print("File CSV 'example2.csv' creato con successo.")

# 3. Utilizzare un delimitatore diverso
"""
È possibile specificare un delimitatore diverso, ad esempio un punto e virgola, utilizzando il parametro `delimiter`.
"""
with open('example_semicolon.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(dati)
print("File CSV 'example_semicolon.csv' creato con successo.")

# 4. Utilizzare DictReader e DictWriter per leggere e scrivere file CSV come dizionari
"""
`csv.DictReader(file)` legge il file CSV come un elenco di dizionari, con le chiavi del dizionario prese dalla prima riga.
`csv.DictWriter(file, fieldnames)` scrive i dati in formato CSV da un elenco di dizionari.
"""
# Scrivere utilizzando DictWriter
dati_dict = [
    {'Nome': 'Alice', 'Età': '30', 'Città': 'Roma'},
    {'Nome': 'Bob', 'Età': '25', 'Città': 'Milano'},
    {'Nome': 'Charlie', 'Età': '35', 'Città': 'Napoli'}
]
with open('example_dict.csv', 'w', newline='') as file:
    fieldnames = ['Nome', 'Età', 'Città']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dati_dict)
print("File CSV 'example_dict.csv' creato con successo.")

# Leggere utilizzando DictReader
with open('example_dict.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# 5. Gestire la codifica UTF-8 nei file CSV
"""
Per garantire che i file CSV possano contenere caratteri speciali e non ASCII, è importante gestire correttamente
la codifica UTF-8. Utilizzare il parametro `encoding='utf-8'` durante la lettura e la scrittura dei file CSV.
"""

# Scrivere un file CSV con codifica UTF-8
dati_utf8 = [
    ['Nome', 'Età', 'Città'],
    ['André', '40', 'Parigi'],
    ['Björk', '35', 'Reykjavik'],
    ['Zoë', '28', 'Londra']
]
with open('example_utf8.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(dati_utf8)
print("File CSV 'example_utf8.csv' creato con successo.")

# Leggere un file CSV con codifica UTF-8
with open('example_utf8.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
Questi sono alcuni degli utilizzi più comuni della libreria `csv`. Questa libreria offre un modo semplice e 
potente per lavorare con file CSV, che sono ampiamente utilizzati per la memorizzazione e lo scambio di dati tabulari.
"""
