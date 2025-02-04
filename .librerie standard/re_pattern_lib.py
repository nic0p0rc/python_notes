import re  # Importa il modulo delle espressioni regolari

# Pattern di ricerca con espressioni regolari
pattern = r'\d'  # Cerca una cifra (equivalente a [0-9])
pattern = r'\D'  # Cerca un carattere non numerico (equivalente a [^0-9])
pattern = r'\s'  # Cerca uno spazio bianco (equivalente a [\t\n\r\f\v])
pattern = r'\S'  # Cerca un carattere non bianco (equivalente a [^\s])
pattern = r'\w'  # Cerca un carattere alfanumerico o underscore (equivalente a [a-zA-Z0-9_])
pattern = r'\W'  # Cerca un carattere non alfanumerico (equivalente a [^\w])

# Quantificatori nelle espressioni regolari
"""
.: Corrisponde a qualsiasi carattere tranne una nuova linea.
^: Corrisponde all'inizio della stringa.
$: Corrisponde alla fine della stringa.
[]: Raggruppamento di caratteri: corrisponde a uno qualsiasi dei caratteri elencati all'interno delle parentesi quadre.
Quantificatori:
    *: Corrisponde a zero o più occorrenze del carattere o gruppo precedente.
    +: Corrisponde a una o più occorrenze del carattere o gruppo precedente.
    ?: Corrisponde a zero o una occorrenza del carattere o gruppo precedente (opzionale).
    {n}: Corrisponde esattamente a n occorrenze del carattere o gruppo precedente.
    {n,}: Corrisponde ad almeno n occorrenze del carattere o gruppo precedente.
    {n,m}: Corrisponde da n a m occorrenze del carattere o gruppo precedente.
"""

# Esempio di utilizzo di espressioni regolari con il modulo re
stringa = "123 abc DEF !@#"

# Cerca tutte le cifre nella stringa usando il pattern '\d'
risultato = re.findall(r'\d', stringa)
print(f"Cifre trovate: {risultato}")  # Output: ['1', '2', '3']

# Cerca tutti i caratteri non numerici nella stringa usando il pattern '\D'
risultato = re.findall(r'\D', stringa)
print(f"Caratteri non numerici trovati: {risultato}")  # Output: [' ', 'a', 'b', 'c', ' ', 'D', 'E', 'F', ' ', '!', '@', '#']

# Cerca tutti gli spazi bianchi nella stringa usando il pattern '\s'
risultato = re.findall(r'\s', stringa)
print(f"Spazi bianchi trovati: {risultato}")  # Output: [' ', ' ']

# Cerca tutti i caratteri non bianchi nella stringa usando il pattern '\S'
risultato = re.findall(r'\S', stringa)
print(f"Caratteri non bianchi trovati: {risultato}")  # Output: ['1', '2', '3', 'a', 'b', 'c', 'D', 'E', 'F', '!', '@', '#']

# Cerca tutti i caratteri alfanumerici o underscore nella stringa usando il pattern '\w'
risultato = re.findall(r'\w', stringa)
print(f"Caratteri alfanumerici o underscore trovati: {risultato}")  # Output: ['1', '2', '3', 'a', 'b', 'c', 'D', 'E', 'F']

# Cerca tutti i caratteri non alfanumerici nella stringa usando il pattern '\W'
risultato = re.findall(r'\W', stringa)
print(f"Caratteri non alfanumerici trovati: {risultato}")  # Output: [' ', ' ', ' ', '!', '@', '#']

# Esempio di utilizzo dei quantificatori con espressioni regolari
test_stringa = "abccc abbc abc"

# Cerca 'abc' seguito da zero o più caratteri 'c'
risultato = re.findall(r'abc*', test_stringa)
print(f"Cerca 'abc*' trovato: {risultato}")  # Output: ['abc', 'abbc', 'abc']

# Cerca 'abc' seguito da uno o più caratteri 'c'
risultato = re.findall(r'abc+', test_stringa)
print(f"Cerca 'abc+' trovato: {risultato}")  # Output: ['abc', 'abbc']

# Cerca 'abbc' oppure 'abc'
risultato = re.findall(r'ab{1,2}c', test_stringa)
print(f"Cerca 'ab{{1,2}}c' trovato: {risultato}")  # Output: ['abbc', 'abc']

# Cerca 'abc' seguito da zero o una volta
risultato = re.findall(r'abc?', test_stringa)
print(f"Cerca 'abc?' trovato: {risultato}")  # Output: ['abc', 'abc', 'abc']

# Cerca 'abc' seguito da esattamente 2 volte
risultato = re.findall(r'abc{2}', test_stringa)
print(f"Cerca 'abc{{2}}' trovato: {risultato}")  # Output: ['abccc']

# Cerca 'abc' seguito da almeno 1 volta fino a 3 volte
risultato = re.findall(r'abc{1,3}', test_stringa)
print(f"Cerca 'abc{{1,3}}' trovato: {risultato}")  # Output: ['abc', 'abbc', 'abc']
