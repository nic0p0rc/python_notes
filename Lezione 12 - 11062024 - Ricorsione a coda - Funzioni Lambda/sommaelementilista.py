#esercizi
#3. somma degli elemtni di una lista

def somma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + somma(lista[1:])

numeri= [1,2,3,4,5]
print(somma(numeri))

def somma(lista):
    if len(lista) == 0:
        return "" 
    else:
        return str(lista[0]) + str(somma(lista[1:]))

parole= ["hello", "word"]
print(somma(numeri))
print(somma(parole))