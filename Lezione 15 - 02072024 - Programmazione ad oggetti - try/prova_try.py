try: 
    vab_1 = int(input("inserisci un valore: "))
    vab_2 = int(input("inserisci un altro valore: "))

    risultato = vab_1/vab_2
    print(risultato)
    
except ZeroDivisionError:
    print("non puoi mettere 0 al denominatore")
    
except ValueError:
    print("non puoi mettere una lettera")
    
else:
    print("finora te la sei scansata")

finally:
    print("hai fatto la prima operazione")
