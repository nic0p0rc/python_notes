import fun_conto
import csv

class Conto_bancario:
    def __init__(self, soldi = 0):
        self.soldi = soldi
        self.transazioni = []
        self.nomeconto = ""
        self.password = ""
        
    def nome(self, nome, password):
        self.nomeconto = nome
        self.password = password
        fun_conto.salva_password([self.nomeconto, self.password])
        
    def deposito(self, soldi_depositati):
        self.soldi += soldi_depositati
        self.transazioni.append(("+" + str(soldi_depositati)))
        
    def prelevare(self, soldi_prelevati):
        if self.soldi > soldi_prelevati:
            self.soldi -= soldi_prelevati
            self.transazioni.append(("-" + str(soldi_prelevati)))
        else:
            print("soldi sul conto insufficienti")
    
    def controllo(self):
        print(f"hai {self.soldi} euro nel tuo conto bancario")
        print(f"le tue ulime transasioni: {self.transazioni}")
    
    def salvataggio(self, nome):
        self.nomeconto = nome
        fun_conto.scrittura(self.nomeconto, self.transazioni, self.soldi)
        print(f"salvataggio avvenuto")
        
    def verifica_entrate(self, nome):
        self.nomeconto = nome
        lista = fun_conto.verifica_conto(self.nomeconto)       
        try:
            for entrata in lista: 
                entrata=entrata
                self.soldi += float(entrata[0])
                self.transazioni.append(entrata[0])
                
        except ValueError:
            pass
        