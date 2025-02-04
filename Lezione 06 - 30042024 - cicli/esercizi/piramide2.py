
numero_righe = int(input("inserisci il numero di righe: "))

for i in range(1, numero_righe+1):
    riga= ""
    for y in range(i):
        riga+= "#"
    print(riga)