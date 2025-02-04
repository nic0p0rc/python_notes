"""
Su python.org --> https://docs.python.org/3/library/socket.html

Il modulo `socket` in Python fornisce un'interfaccia per la comunicazione di rete utilizzando i socket. 
È utile per creare server e client di rete che possono comunicare su vari protocolli, come TCP e UDP.

Ecco alcuni degli utilizzi più comuni del modulo `socket`:

1. Creare un client TCP.
2. Creare un server TCP.
3. Creare un client UDP.
4. Creare un server UDP.
"""

import socket

# 1. Creare un client TCP
"""
Un client TCP si connette a un server e scambia dati con esso utilizzando il protocollo TCP.
Ecco un esempio di un client TCP che si connette a un server, invia un messaggio e riceve una risposta.
"""
def client_tcp():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, server')
        data = s.recv(1024)
    
    print(f"Risposta dal server: {data.decode()}")

# client_tcp()  # Decommentare per eseguire il client TCP

# 2. Creare un server TCP
"""
Un server TCP accetta connessioni dai client e scambia dati con essi utilizzando il protocollo TCP.
Ecco un esempio di un server TCP che accetta connessioni, riceve messaggi dai client e risponde.
"""
def server_tcp():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server in ascolto su {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connessione accettata da {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Ricevuto: {data.decode()}")
                conn.sendall(data)

# server_tcp()  # Decommentare per eseguire il server TCP

# 3. Creare un client UDP
"""
Un client UDP invia dati a un server e riceve risposte utilizzando il protocollo UDP.
Ecco un esempio di un client UDP che invia un messaggio a un server e riceve una risposta.
"""
def client_udp():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'Hello, server', (host, port))
        data, server = s.recvfrom(1024)
    
    print(f"Risposta dal server: {data.decode()}")

# client_udp()  # Decommentare per eseguire il client UDP

# 4. Creare un server UDP
"""
Un server UDP riceve dati dai client e invia risposte utilizzando il protocollo UDP.
Ecco un esempio di un server UDP che riceve messaggi dai client e risponde.
"""
def server_udp():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Server UDP in ascolto su {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"Ricevuto da {addr}: {data.decode()}")
            s.sendto(data, addr)

# server_udp()  # Decommentare per eseguire il server UDP

"""
Questi sono alcuni degli utilizzi più comuni del modulo `socket`. Questo modulo offre molte funzioni
per la comunicazione di rete, permettendo di creare sia server che client per diversi protocolli di comunicazione.
"""
