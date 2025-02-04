import csv
import re

def pulisci_parole(categorie):
    parole_pulite = []
    for categoria in categorie:
        parole = re.findall(r'\b([a-zA-Z]+)\b', categoria)
        parole_pulite.extend(parole)
    return parole_pulite

# Leggi il file CSV e crea una lista di dizionari per memorizzare i dati del libro
libri = []
with open('libri.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        libro = {
            "titolo": row[1],
            "autore": row[2],
            "anno": row[3],
            "categoria": row[4]
        }
        libri.append(libro)

# Estrai le categorie pulite e uniche
categorie_raw = [libro["categoria"] for libro in libri]
categorie_pulite = pulisci_parole(categorie_raw)
categorie_pulite_uniche = {categoria.strip().lower() for categoria in set(categorie_pulite)}

# Stampa le categorie uniche
for categoria in categorie_pulite_uniche:
    print(categoria)

# Richiedi la scelta dell'utente fino a quando non viene trovata una categoria valida
while True:
    scelta = input("Inserisci la categoria che preferisci: ").strip().lower()
    if scelta in categorie_pulite_uniche:
        break
    else:
        print("Categoria non trovata")

# Filtra i libri in base alla categoria scelta
libri_trovati = [libro for libro in libri if scelta in pulisci_parole([libro["categoria"]])]

# Stampa i risultati
print(f"Ci sono {len(libri_trovati)} libri della categoria '{scelta}':")
for libro in libri_trovati:
    print(f"Titolo: {libro['titolo']}, Autore: {libro['autore']}, Anno: {libro['anno']}")

if not libri_trovati:
    print("Nessun libro trovato nella categoria scelta.")
