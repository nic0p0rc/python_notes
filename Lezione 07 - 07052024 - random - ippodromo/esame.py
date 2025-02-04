#funzione per verifica bocciatura   
def calcolo_risultato(teor, prat):
    totale=teor+prat
    
    #verifica bocciatura
    if teor <= 0 or totale <=18:
        return "Bocciato"
    elif totale >= 31:
        return "Congratulazioni: 30 e lode"

    return f"Promosso con voto: {totale}"
    
#inserimento voti  
teoria = int(input("Inserisci il voto della prova di teoria (-8 a +8): "))
pratica = int(input("Inserisci il voto della prova pratica (0 a 24): "))

print(calcolo_risultato(teoria,pratica))

