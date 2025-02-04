
giorni = 0
panini_mangiati = 0
pastine_mangiate = 0
print("Benvenuto! Al bar della scuola, la pastina costa 1 euro, mentre il panino costa 1.5 euro.")

while True:
    soldi_mario = input("Inserisci la quantità di soldi di Mario: ")
    if soldi_mario.isdigit():
        soldi_mario = float(soldi_mario)
        break

while soldi_mario >= 1:
    scelta = input("Cosa vuole mangiare Mario oggi? (pastina / panino): ")
    
    if scelta == "panino":
        if soldi_mario >= 1.5:
            soldi_mario-=1.5
            panini_mangiati+=1
            giorni+=1
            print(f"ora hai {soldi_mario} euro a disposione")
        else:
            print("non hai abbastanza soldi per il panino")
            
    elif scelta == "pastina":
        soldi_mario-=1
        pastine_mangiate+=1
        giorni+=1
        print(f"ora hai {soldi_mario} euro a disposione")
    else:
     print("scegli tra pastina e panino")
     
print("\nRisultati:")
print("Numero di giorni in cui Mario ha mangiato:", giorni)
print("Numero di pastine consumate:", pastine_mangiate)
print("Numero di panini consumati:", panini_mangiati)

    