
stringa = input("inserisci una parola: ")
vocali = ["a", "e", "i", "o", "u"]
conteggio_vocali = 0

for carattere in stringa: 
    #print(carattere)
    for lettere in vocali:
        if carattere == lettere:
            #print("vocale")
            conteggio_vocali += 1

print(f"Nella parola {stringa} sono contenute {conteggio_vocali} vocali")
       