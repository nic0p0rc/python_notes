
informazioni={}

nome=input("inserisci il tuo nome: ")
informazioni["nome"]=nome

cognome=input("inserisci il tuo cognome: ")
informazioni["cognome"]=cognome

eta=input("inserisci la tua età: ")
informazioni["eta"]=eta

print(f"ci sono {len(informazioni)} paramentri")

indice=input("\ninserisci 'nome', 'cognome', 'eta' in base a cio che vuoi visualizzare: ")
print(informazioni[indice])


