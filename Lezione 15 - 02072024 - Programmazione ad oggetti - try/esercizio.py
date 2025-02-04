try: 
    lista = [10,20,30,40,50]
    indice = int(input("inserisci l'indice delll'elemento da stampare: "))
    print(lista[indice])

except IndexError:
    print("indice non valido")

except ValueError:
    print("non puoi inserire una lettera")
    
else:
    print("è stato bello")

finally:
    print("bravo")

