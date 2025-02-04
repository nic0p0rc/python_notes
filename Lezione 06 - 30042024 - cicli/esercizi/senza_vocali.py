
stringa = input("inserisci una stringa: ")
vocali = "aeiouAEIOU"
parola_finale = ""

for carattere in stringa: 
    if carattere not in vocali:
        parola_finale += carattere
        
print(parola_finale)