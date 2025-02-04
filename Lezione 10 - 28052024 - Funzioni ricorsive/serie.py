# a*b**0+a*b**o+...+a*b**n

def serie(a,b,n):
    if n < 0:
        return 0 
    else:
        return a*(b**n) + serie(a,b,n-1)

numero_a=int(input("inserisci il valore del numero a: "))
numero_b=int(input("inserisci il valore del numero b: "))
numero_n=int(input("inserisci il valore del numero n: "))
print(serie(numero_a,numero_b,numero_n))

def potenza(n,m,a):
    if n < 0:
        return 0 
    else:
        return a*(m**n) + potenza(n-1,m,a)
print(potenza(5,2,2))

def serieg(a,r,n,ris=0):
    if n < 0:
        return ris
    else:
        ris += a*r**n
        return serieg(a,r,n-1,ris)
print(serieg(2,2,5))

#esercizi
'''
    1.algoritmo di euclide
    2.calcolare il numero di cifre di un numero intero
    3.piccolo menu 
    