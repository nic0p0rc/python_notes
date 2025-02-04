try:
    numero = int(input("Inserisci un numero per vedere la sua tabellina: "))
    i=1

    while i <= 10:
        risultato = numero * i
        print(f"{numero} x {i} = {risultato}")
        i += 1
        
except ValueError:
    print("puoi inserire soltanto un valore numerico")

