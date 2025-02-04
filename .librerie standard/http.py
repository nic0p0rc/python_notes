"""
Su python.org --> https://docs.python.org/3/library/http.html

Il modulo `http` in Python fornisce classi e funzioni per lavorare con il protocollo HTTP. È utile per la creazione
di server HTTP, l'invio di richieste HTTP e la gestione delle risposte HTTP. Il modulo `http` è diviso in diversi
sotto-moduli, come `http.client` per le richieste HTTP e `http.server` per la creazione di server HTTP.

Ecco alcuni degli utilizzi più comuni del modulo `http`:

1. Inviare richieste HTTP con `http.client`.
2. Creare un semplice server HTTP con `http.server`.
3. Gestire le risposte HTTP.
"""

# 1. Inviare richieste HTTP con http.client
"""
Il modulo `http.client` permette di inviare richieste HTTP e di gestire le risposte. 
Ecco un esempio di come inviare una richiesta GET e leggere la risposta.
"""
import http.client

conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")
response = conn.getresponse()

print(f"Status: {response.status}")
print(f"Reason: {response.reason}")

# Leggere il contenuto della risposta
data = response.read()
print(f"Contenuto della risposta: {data[:100]}")  # Stampa i primi 100 caratteri del contenuto

conn.close()

# 2. Creare un semplice server HTTP con http.server
"""
Il modulo `http.server` permette di creare facilmente un server HTTP. 
Ecco un esempio di come creare un semplice server che risponde con "Hello, World!" a ogni richiesta.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

# Configurare l'host e la porta
host = 'localhost'
port = 8000
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Server HTTP in esecuzione su {host}:{port}")
# Il server rimarrà in ascolto fino a quando non viene interrotto manualmente
# server.serve_forever()

# 3. Gestire le risposte HTTP
"""
Le risposte HTTP possono essere gestite leggendo i vari attributi dell'oggetto `HTTPResponse`. 
Ecco un esempio di come leggere le intestazioni della risposta.
"""
conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")
response = conn.getresponse()

print(f"Status: {response.status}")
print(f"Reason: {response.reason}")

# Leggere le intestazioni della risposta
headers = response.getheaders()
for header in headers:
    print(f"{header[0]}: {header[1]}")

conn.close()

"""
Questi sono alcuni degli utilizzi più comuni del modulo `http`. Questo modulo offre molti strumenti per lavorare
con il protocollo HTTP, dalla creazione di server HTTP all'invio e alla gestione di richieste e risposte HTTP.
"""
