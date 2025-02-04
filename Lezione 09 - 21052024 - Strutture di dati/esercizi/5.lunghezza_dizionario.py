import csv

informazioni={"nome": "nome1", "cognome": "cognome1", "eta": "eta1"}

nome=input("inserisci il tuo nome: ")
informazioni["nome"]=nome

cognome=input("inserisci il tuo cognome: ")
informazioni["cognome"]=cognome

eta=input("inserisci la tua età: ")
informazioni["eta"]=eta

print(f"ci sono {len(informazioni)} paramentri")

'''
with open('output2.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    dati=["nome", "cognome", "eta"]
        
    for i in range(3):
        writer.writerow(dati[i])
        writer.writerow(informazioni[dati[i]])
        
print("Informazioni salvate nel file output.csv")
'''