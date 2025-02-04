import csv

while True:
    scelta=input("""\nbenvenuto nella tua rubbrica, cosa vuoi fare:
    1. aggiungi nuova persona alla rubbrica
    2. trova persona nella rubbrica
    3. Esci
    """)

    if scelta == "1":
            #creazione dizionario con input
        informazioni={}
        
        nome=input("\ninserisci il nome: ")
        informazioni["nome"]=nome
        cognome=input("inserisci il cognome: ")
        informazioni["cognome"]=cognome
        
        while True:
            tipo_di_informazione=input("inserisci quale tipo di informazione vuoi aggiungere (es. eta,numero di telefono ecc):")
            dato=input("inserisci il dato: ")
            informazioni[str(tipo_di_informazione)]=dato
            continuo=input("altre informazioni: si/no: ").upper()
            if continuo == "NO":
                break
                
        #scrittura su file csv
        with open('output.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(informazioni.keys())
            writer.writerow(informazioni.values())
            writer.writerow(" ")
        print("Informazioni salvate nel file output.csv\n")
        
    elif scelta == "2":
        #lettura file 
        with open('output.csv', mode='r') as file: 
            reader = csv.reader(file)
            
            lista= []
            for row in reader:
                lista.append(row)

        #risultati

        dato= input("\nInserisci un dato (nome, cognome o eta) per cercare la persona: ")
        ricerca = [riga for riga in lista if dato in riga]
        print(ricerca)
    
    elif scelta == "3":
        print("Arrivederci!")
        break
        
    else:
        print("Scelta non valida, per favore riprova.")
