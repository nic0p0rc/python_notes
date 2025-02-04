lista = [10, 5, "ciao", 210, "python", 15]
print(lista)

lista.append("ciccio")
print(lista)

lista.remove(10)
print(lista)

elemento = lista[0]
print(elemento)

sottolista = lista[2:4]
print(sottolista)

sottolista = lista[:4]
print(sottolista)

sottolista = lista[2:]
print(sottolista)

lista2 = lista + sottolista
print(lista2)

lista3 = lista2*2
print(lista3)

print(len(lista3))

#for con liste
for elemento in lista3:
    print(elemento)
    
for elemento in lista3:
    lista3.remove(elemento)
print(lista3)

#rimuovere elementi da una lista con for
#esempio con rimozione di lista totale
lista_nuova=[1,3,5,6,"ciao"]
lista_di_prova=lista_nuova[:]
print(lista_di_prova)

for elemento in lista_nuova[:]:
    lista_nuova.remove(elemento)
print(lista_nuova)

#rimozione di una sottolista da una lista
lista_nuova=[1,3,5,6,"ciao"]
sottolista_di_prova= lista_nuova[2:3]
print(sottolista_di_prova)

for elemento in sottolista_di_prova:
    lista_nuova.remove(elemento)
print(lista_nuova)

lista_nuova.reverse()
print(lista_nuova)