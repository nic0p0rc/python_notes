'''
#esercizio 1
try:
    dizionario = {"nome": "mario","eta": 30 ,"città":"Roma"}
    chiave = input("inserisci la chiave giusta: ")
    print(chiave,dizionario[chiave])

except KeyError:
    print("Errore: hai sbagliato la chiave")
    
#esercizio 2  
try:
    stringa = input("inserisci una stringa: ")
    indice_inizio = int(input("inserisci l'indice di inizio: "))
    indice_di_fine = int(input("inserisci l'indice di fine: "))
    print(stringa[indice_inizio:indice_di_fine])
    
except ValueError:
    print("inserisci un indice intero")



import datetime
try:
    data_input = input("inserisci una data (gg/mm/aaaa): ")
    data = datetime.datetime.strptime(data_input, "%d/%m/%Y").date()
    print(data)

except ValueError:
    print("inserisci una data corretta")
''' 

try:
    lista = [10, 30, 20, 5]
    somma = sum(lista)
    print(somma)

except TypeError:
    print("tutti gli elementi devono essere numerici")