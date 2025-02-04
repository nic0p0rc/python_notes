import Conto_bancario
import fun_conto
#import os

contobancario = Conto_bancario.Conto_bancario()
def verifica_scelta(intestatario):
    while True:  
        scelta= fun_conto.scelta_admin()
        if scelta == 1:
            while True:
                try:
                    soldi_da_depositare = float(input("inserisci l'importo da depositare: "))
                    contobancario.deposito(soldi_da_depositare)
                except ValueError:
                    print("errore nel valore da depositare")
                else:
                    break
                        
        elif scelta == 2:
            while True:
                try:
                    soldi_da_prelevare = float(input("inserisci l'importo da prelevare: "))
                    contobancario.prelevare(soldi_da_prelevare)
                except ValueError:
                    print("errore nel valore da depositare")
                else:
                    break
                        
        elif scelta == 3:
                contobancario.controllo()
                    
        elif scelta == 4:
            contobancario.salvataggio(intestatario)
            exit()
        
while True:
    
    scelta = fun_conto.scelta()
    
    if scelta == 1:
        print("Benvenuto nella banca più famosa al mondo,crea il tuo conto bancario in pochi clik")
        
        intestatario = "contobancariodi"+ input("inserisci il nome dell'intestatario del conto: ")
        password = input("inserisci la password: ")
        contobancario.nome(intestatario, password)
        
        print("benvenuto nel tuo conto bancario")
        verifica_scelta(intestatario)
            
    elif scelta == 2:
        #path = r"C:\Users\Utente\Desktop\Cosrsi di formazione\volta\python e IA\pythonEsempi\16 oggetti\esercizi\conto bancario\database"
        #nomi_file = os.listdir(path)
        #if intestatario in nomi_file:
        #    print("inserisci la password: ")
        while True:
            intestatario = "contobancariodi"+ input("inserisci il nome dell'intestatario del conto: ")
            password = input("inserisci la password: ") 
            if not fun_conto.verifica_password(intestatario, password):
                print("nome o password errati")
            else:
                break
        
        contobancario.verifica_entrate(intestatario)
        print("benvenuto nel tuo contobancario")
        #fun_conto.verifica_conto(intestatario)
        contobancario.controllo()
        verifica_scelta(intestatario)