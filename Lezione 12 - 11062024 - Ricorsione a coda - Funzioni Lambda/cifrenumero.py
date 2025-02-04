#esercizi
#2. calcolo del numero di cifre di un numero



def conta_cifre(n):
    if n < 10:
        return 1
    else:
        return 1 + conta_cifre(n // 10)


numero = int(input("inserisci un numero: "))
print(f"il numewro {numero} ha {conta_cifre(numero)} cifre")

numero=input("inserisci un numero: ")
punti=numero.count(".")
print(len(numero)-punti)