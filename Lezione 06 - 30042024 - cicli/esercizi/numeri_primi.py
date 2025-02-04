numero1 = int(input("inserisci il primo numero: "))
numero2 = int(input("inserisci il secondo numero: "))

numeri_primi = ""

for i in range(numero1, numero2+1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        numeri_primi += f"{i} "

print("I numeri primi tra", numero1, "e", numero2, "sono:", numeri_primi)       