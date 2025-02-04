import random

cassa = 100

while cassa >0:
    #scelta_puntata
    print(f"\nhai {cassa} euro in cassa")
    while True:
        puntata = int(input("Quanto vuoi puntare? Minimo 5€: "))
        if puntata >= 5 and puntata <= cassa:
            cassa -= puntata
            print(f"la tua cassa adesso è di {cassa} euro")
            break
        else:
            print("la puntata deve essere almeno di 5 euro e non superiore alla cassa")

    #scelta_scomessa
    while True: 
        tipo_scommessa = input("Vuoi scommettere sul piazzato (P) o sul vincente (V)? ")
        if tipo_scommessa in ["P","V"]:
            break
        else:
            print("Scegli tra P piazzamento o V per vincente")

    #scelta_cavallo
    while True:
        cavallo = int(input("\nscegli un cavallo con un numero da 1 a 10: "))
        if cavallo <= 10 and cavallo >= 1:
            break
        else:
            print("scegli solamente un cavallo tra 1 a 10")

    #simulazione_corsa
    vincente = random.randint(1, 10)
    piazzati=[]
    i=0
    while i<3:
        nuovo_numero = random.randint(1,10)
        if nuovo_numero not in piazzati:
            piazzati += [nuovo_numero]
            i+=1

    #verifiche_risultato
    if tipo_scommessa == "V":
        if cavallo == vincente:
            vincita = 5 * puntata
            cassa+=vincita
            print(f"complimenti hai vinto, hai scelto il cavallo {cavallo}\n" 
                  f"il cavallo vincente è proprio il {vincente}\n"
                  f"hai vinto {vincita} euro e ora hai un totale di {cassa} euro\n")
        else:
            print(f"Hai perso, hai scelto il cavallo {cavallo}\n" 
                  f"il cavallo vincente è {vincente}\n")
    elif tipo_scommessa == "P":
        if cavallo in piazzati:
            vincita = 2 * puntata
            cassa+=vincita
            print(f"complimenti hai vinto, hai scelto il cavallo {cavallo}\n" 
                  f"i cavalli vincenti sono {piazzati}\n"
                  f"hai vinto {vincita} euro e ora hai un totale di {cassa} euro\n")
        else:
            print(f"Hai perso, hai scelto il cavallo {cavallo}\n" 
                  f"i cavalli vincenti sono {piazzati}\n")
    
    #scelta continuo gioco
    if cassa > 0:
        continua = input("Vuoi continuare a giocare? (si/no): ")
        if continua != "si":
            break

print("grazie per aver giocato!")
