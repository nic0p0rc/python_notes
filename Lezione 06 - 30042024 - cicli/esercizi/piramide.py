
numero_righe = int(input("inserisci il numero di righe: "))

for i in range(numero_righe):
    riga= ""
    for y in range(numero_righe - i):
        riga+= "*"
    print(riga)