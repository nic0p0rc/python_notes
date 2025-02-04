#fattoriale a coda
def coda(n, ac=1):
    if n==0:
        return ac
    else:
        return coda(n-1,ac*n)
        
print(coda(5))

#fattoriale non a coda
def fat(n):
    if n == 0:
        return 1
    else:
        return n*fat(n-1)
        
print(fat(5))


def somma(x, y=3):
    return x+y

print(somma(5))
print(somma(5,6))

#somma dei primi n numeri (ricorsione a coda)
def somma(n, ac=0):
    if n==0:
        return ac
    else:
        return somma(n-1,ac+n)

n=int(input("inserisci un numero: "))
print("la somma dei primi {} numeri è {}".format(n, somma(n)))

#somma dei primi n numeri (senza ricorsione)
def somma1(n):
    somma=0
    for elemento in range(1,n+1):
        somma+=elemento
    print(somma)
    return somma
print(somma1(5))

#somma dei primi n numeri (ricorsione normale)
def somma2(n):
    if n == 0:
        return n
    else:
        return n+somma2(n-1)
print(somma2(5))