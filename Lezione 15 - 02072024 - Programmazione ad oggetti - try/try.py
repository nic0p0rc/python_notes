while True:
    try:
        numeratore = int(input("inserisci il numeratore: "))
        denominatore = int(input("inserisci il denominatore: "))
        
        risultato = numeratore/denominatore
        print("Risultato:", risultato)
        
    except ZeroDivisionError:
        print("Errore, il denominatore non può essere 0")
        
    except ValueError:
        print("inserisci valori numerici validi")
      
    scelta = input("vuoi continuare? ").upper()
    if scelta == "NO":
        break