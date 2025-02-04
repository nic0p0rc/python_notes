
numero = int(input("inserisci il numero: "))
somma = 0

for i in range(0, numero+1 ,2):
    somma+=i
    
print(f"la somma dei numeri pari da 0 a {numero} è {somma}")