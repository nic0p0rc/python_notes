
while True:
    numero = input("inserisci i numeri che vuoi sommare(scrivi i numeri con uno spazio fra di loro: ").split()
    interi=[int(i) for i in numero]
    print("la somma vale: {} ".format(sum(interi)))
    
    scelta=input("vuoi continuare? si/no: ").upper()
    if scelta == "NO":
        break


