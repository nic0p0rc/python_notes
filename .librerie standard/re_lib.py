"""
Su python.org --> https://docs.python.org/3/library/re.html

La libreria `re` in Python è utilizzata per eseguire operazioni di matching delle espressioni regolari. 
Le espressioni regolari (regex) sono potenti strumenti per la ricerca, la sostituzione e la manipolazione 
di stringhe secondo modelli specifici.

Ecco alcuni degli utilizzi più comuni della libreria `re`:

1. Trovare una corrispondenza con `re.match` e `re.search`.
2. Trovare tutte le corrispondenze con `re.findall`.
3. Sostituire le sottostringhe con `re.sub`.
4. Suddividere una stringa con `re.split`.
5. Utilizzare gruppi di cattura.
"""

import re

# 1. Trovare una corrispondenza con re.match e re.search
"""
La funzione `re.match(pattern, string)` cerca una corrispondenza all'inizio della stringa.
La funzione `re.search(pattern, string)` cerca la prima corrispondenza in tutta la stringa.
"""
pattern = r'\d+'  # Pattern che cerca una o più cifre
"""
pattern = r'\d'  # Cerca una cifra
pattern = r'\D'  # Cerca un carattere non numerico
pattern = r'\s'  # Cerca uno spazio bianco
pattern = r'\S'  # Cerca un carattere non bianco
pattern = r'\w'  # Cerca un carattere alfanumerico o underscore
pattern = r'\W'  # Cerca un carattere non alfanumerico

.: Qualsiasi carattere eccetto una nuova linea.
^: Inizio della stringa.
$: Fine della stringa.
[]: Raggruppamento di caratteri.
Quantificatori:
    *: Zero o più occorrenze.
    +: Una o più occorrenze.
    ?: Zero o una occorrenza.
    {n}: Esattamente n occorrenze.
    {n,}: Almeno n occorrenze.
    {n,m}: Da n a m occorrenze.
"""

# Utilizzo di re.match
match = re.match(pattern, '123abc')
if match:
    print(f"re.match ha trovato: {match.group()}")

# Utilizzo di re.search
search = re.search(pattern, 'abc123')
if search:
    print(f"re.search ha trovato: {search.group()}")

# 2. Trovare tutte le corrispondenze con re.findall
"""
La funzione `re.findall(pattern, string)` restituisce una lista di tutte le corrispondenze del pattern nella stringa.
"""
stringa = 'Ci sono 3 mele e 10 banane'
corrispondenze = re.findall(pattern, stringa)
print(f"re.findall ha trovato: {corrispondenze}")

# 3. Sostituire le sottostringhe con re.sub
"""
La funzione `re.sub(pattern, repl, string)` sostituisce tutte le corrispondenze del pattern nella stringa con `repl`.
"""
stringa_sostituita = re.sub(pattern, '#', stringa)
print(f"Stringa dopo re.sub: {stringa_sostituita}")

# 4. Suddividere una stringa con re.split
"""
La funzione `re.split(pattern, string)` divide la stringa attorno alle corrispondenze del pattern e restituisce 
una lista delle sottostringhe risultanti.
"""
stringa_divisa = re.split(r'\s+', stringa)  # Divide la stringa attorno agli spazi bianchi
print(f"Stringa divisa con re.split: {stringa_divisa}")

# 5. Utilizzare gruppi di cattura
"""
I gruppi di cattura permettono di isolare parti della stringa che corrispondono a sotto-pattern specifici. 
Si definiscono racchiudendo il sotto-pattern tra parentesi.
"""
pattern_gruppi = r'(\d+) (\w+)'  # Pattern che cerca una o più cifre seguite da una o più lettere
match_gruppi = re.search(pattern_gruppi, stringa)
if match_gruppi:
    print(f"Gruppo 1: {match_gruppi.group(1)}")
    print(f"Gruppo 2: {match_gruppi.group(2)}")

"""
Questi sono alcuni degli utilizzi più comuni della libreria `re`. Le espressioni regolari sono strumenti 
estremamente potenti per la manipolazione delle stringhe e, sebbene possano sembrare complesse all'inizio, 
offrono grande flessibilità e precisione per compiti di ricerca e manipolazione del testo.
"""
