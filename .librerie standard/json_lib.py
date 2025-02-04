"""
Su python.org --> https://docs.python.org/3/library/json.html

Il modulo `json` in Python è utilizzato per la codifica e la decodifica di dati JSON (JavaScript Object Notation), 
un formato di scambio dati leggero e facile da leggere/scrivere per le macchine. JSON è ampiamente utilizzato 
per la comunicazione tra client e server e per la serializzazione dei dati.

Ecco alcuni degli utilizzi più comuni del modulo `json`:

1. Codificare oggetti Python in JSON.
2. Decodificare JSON in oggetti Python.
3. Gestire file JSON.
"""

import json

# 1. Codificare oggetti Python in JSON
"""
La funzione `json.dumps(obj)` converte oggetti Python in stringhe JSON.
"""
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(f"Dati codificati in JSON: {json_string}")

# 2. Decodificare JSON in oggetti Python
"""
La funzione `json.loads(json_string)` converte stringhe JSON in oggetti Python.
"""
json_string = '{"name": "Alice", "age": 25, "city": "San Francisco"}'
decoded_data = json.loads(json_string)
print(f"Dati decodificati da JSON: {decoded_data}")

# 3. Gestire file JSON
"""
È possibile leggere e scrivere dati JSON da e verso file utilizzando `json.dump()` e `json.load()`.
"""
# Scrivere dati JSON in un file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Dati JSON scritti nel file 'data.json'")

# Leggere dati JSON da un file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(f"Dati letti dal file JSON: {loaded_data}")

"""
Questi sono alcuni degli utilizzi più comuni del modulo `json`. Questo modulo è estremamente utile per 
la serializzazione e deserializzazione dei dati, facilitando la comunicazione e lo scambio di dati strutturati 
tra diverse applicazioni e sistemi.
"""
