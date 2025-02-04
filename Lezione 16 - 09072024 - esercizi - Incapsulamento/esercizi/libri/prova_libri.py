import csv
import re
import Libri

def pulisci_parole(categorie):
    parole_pulite = []
    for categoria in categorie:
        parole = re.findall(r'\b([a-zA-Z]+)\b', categoria)
        parole_pulite.extend(parole)
    return parole_pulite


with open('libri.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    lista = []
    for row in reader:     
        for row in row:
            lista.append(row)

# 1 titolo 2autore 3 anno 4 caratteristiche
#trova gli indici per trovare titoli autori anni ecc
indici_titoli = [indice for indice in range(1,300, 6)]
indici_autori = [indice for indice in range(2,300, 6)]
indici_anni = [indice for indice in range(3,300, 6)]
indici_categoria = [indice for indice in range(4,300, 6)]

titoli = [lista[titolo] for titolo in indici_titoli] 
autori = [lista[autore] for autore in indici_autori] 
anni = [lista[anni] for anni in indici_anni] 
#categorie ripeture con parentesi e trattini
categorie = [lista[categoria] for categoria in indici_categoria]
#categorie ripetute pulite
categorie_pulite = pulisci_parole(categorie)
#categorie pulite e uniche
categorie_pulite_uniche = {categoria.strip().lower() for categoria in set(categorie_pulite)}

while True: 
    print("Ecco a te le categorie più famose presenti in libreria:")
    for categoria in categorie_pulite_uniche:
        print(categoria)

    while True:
        scelta = input("inserisci la categoria che preferisci: ").strip().lower()
        print(scelta)
        if scelta in categorie_pulite_uniche:
            break
        else:
            print("categoria non trovata")

    
    libri_trovati = [trovati for trovati in categorie_pulite if trovati.strip().lower() == scelta]
    print(f"\nci sono {len(libri_trovati)} libri della categoria {scelta}")
    scelta_ = input("vuoi visualizzarli? (si/no): ").strip().lower()

    if scelta_ == "si":
        indici_libri = []
        for i,libro in enumerate(categorie_pulite):
            libro=libro.strip().lower()
            if scelta == libro:
                indici_libri.append(i)
        #print(indici_libri)
        
        for indice in indici_libri:
            titolo = titoli[indice]
            autore = autori[indice]
            anno = anni[indice]
            categoria = categorie_pulite[indice]
            libro = Libri.Libro(titolo, autore, anno, categoria)
            print(libro.caratteristiche())