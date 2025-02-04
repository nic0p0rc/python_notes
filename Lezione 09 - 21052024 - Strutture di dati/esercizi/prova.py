
stringa="ciao"
lista = [10 for i in stringa]
print(lista)

stringa="CiIaAoO"
lista = [str(i) for i in stringa if i.isupper()]
print(lista)

stringa="C1i2I3a4A5o6O7"
lista = [str(i) for i in stringa if i.isdigit()]
print(lista)