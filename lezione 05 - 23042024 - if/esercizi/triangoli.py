
lato1 = input("inserisci il valore del primo lato: ")
lato2 = input("inserisci il valore del secondo lato: ")
lato3 = input("inserisci il valore del terzo lato: ")

if lato1 == lato2 == lato3: 
     print("Il triangolo è equilatero.")
elif lato1 == lato2 or lato2== lato3 or lato1 == lato3:
    print("Il triangolo è isoscele.")
else:
    print("Il triangolo è scaleno.")
