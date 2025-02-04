import re

# Leggi il file come byte
with open("libri.csv", 'rb') as file:
    content = file.read()

# Pattern regex per trovare parentesi iniziali e finali di ogni riga
pattern = re.compile(rb'^\(|\),?\s*$', re.MULTILINE)

# Sostituisci il contenuto rimuovendo le parentesi
new_content = re.sub(pattern, b'', content)

# Salva il file modificato
with open("nuovo_libri.csv", 'wb') as new_file:
    new_file.write(new_content)

print("File salvato correttamente come nuovo")

