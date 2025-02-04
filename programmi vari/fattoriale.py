# Informazioni sul programmatore, versione e data di rilascio
print("Sviluppato da: Porcelluzzi Nicolo'")
print("Versione: 1.0")
print("Data di rilascio: 27/02/2024")
print("Scopo: Questo programma calcola il fattoriale di un numero e lo confronta con un secondo numero.\n")

print('''
   _____      _           _         ______    _   _             _       _      
  / ____|    | |         | |       |  ____|  | | | |           (_)     | |     
 | |     __ _| | ___ ___ | | __ _  | |__ __ _| |_| |_ ___  _ __ _  __ _| | ___ 
 | |    / _` | |/ __/ _ \| |/ _` | |  __/ _` | __| __/ _ \| '__| |/ _` | |/ _ \ 
 | |___| (_| | | (_| (_) | | (_| | | | | (_| | |_| || (_) | |  | | (_| | |  __/ 
  \_____\__,_|_|\___\___/|_|\__,_| |_|  \__,_|\__|\__\___/|_|  |_|\__,_|_|\___| 
''')

# Funzione per calcolare il fattoriale di un numero
def calcolo_fattoriale(numero):
    risultato = 1
    # Ciclo che calcola il fattoriale
    for i in range(1, numero + 1):
        risultato *= i
    return risultato

Numero = int(input("Inserisci il numero di cui calcolare il fattoriale: "))
N_Confronto = int(input("Inserisci il valore di confronto: "))

# Calcolo del fattoriale
fattoriale = calcolo_fattoriale(Numero)
print(f"Il risultato di {Numero} e': {fattoriale}")

# Confronto tra il fattoriale e il valore di confronto
if fattoriale < N_Confronto:
    print(f"{Numero}! e' minore di {N_Confronto}")
elif fattoriale > N_Confronto:
    print(f"{Numero}! e' maggiore di {N_Confronto}")
else:
    print(f"{Numero}! e' uguale a {N_Confronto}")
