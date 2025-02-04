def somma(x):
    som=0
    for i in x: 
        som+=i
    return som

lista=[]
num_somma=int(input("quanti numeri vuoi sommare?: "))

for i in range (num_somma):
    numero = int(input("inserisci un numero da sommare: "))
    lista.append(numero)
    
somma=somma(lista)
print(f"la somma vale: {somma}")
