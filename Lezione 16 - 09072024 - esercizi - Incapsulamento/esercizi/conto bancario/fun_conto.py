import csv

def scelta():
    try:
        scelta = int(input("""\nScegli l'operazione che vuoi eseguire:
        1.Crea il tuo conto bancario
        2.Accedi al tuo conto bancario\n"""))
        if scelta in [1,2]:
            return scelta
        else:
            print("immettere solamente numero 1 o 2")
            
    except ValueError:
        print("non puoi inserire lettere, scegli tra 1 o 2")
        
def scrittura(nome, dati, soldi):
    with open(f"{nome}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for riga in dati:
                writer.writerow([riga])
            writer.writerow(["totale conto bancario",soldi])
            
def salva_password(lista):
    with open("password.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(lista)
            
def verifica_password(nome, password):
    try:
        with open('password.csv', 'r') as file:
            reader = csv.reader(file)
            lista = []
            for row in reader:
                lista.append(row)
    
        if [riga for riga in lista if nome and password in riga]:
            return True
            
    except FileNotFoundError: 
        print("non esistono accout, creane uno")
        scelta()
        
def scelta_admin():
    try:
        scelta = int(input("""\nScegli l'operazione che vuoi eseguire:
        1.Deposito denaro nel tuo conto
        2.Preleva denaro dal tuo conto
        3.Controllo
        4.Esci e salva\n"""))
        if scelta in [1,2,3,4]:
            return scelta
        else:
            print("immettere solamente numero 1, 2, 3 o 4")
            
    except ValueError:
        print("non puoi inserire lettere, scegli tra 1, 2, 3 o 4")
        
def verifica_conto(nome_file):
    with open(f'{nome_file}.csv', 'r') as file:
        reader = csv.reader(file)
        lista = []
        for row in reader:
            lista.append(row)
    return lista