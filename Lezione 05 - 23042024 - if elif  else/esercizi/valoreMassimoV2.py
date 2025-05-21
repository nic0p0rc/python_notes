
numeri = [0, 0, 0]
valore_massimo = 0

numeri[0] = int(input("Inserisci il primo numero: "))
numeri[1] = int(input("Inserisci il secondo numero: "))
numeri[2] = int(input("Inserisci il terzo numero: "))

for numero in numeri:
    if numero > valore_massimo:
        valore_massimo = numero
    
print(f"il valore massimo è uguale a: {valore_massimo}")