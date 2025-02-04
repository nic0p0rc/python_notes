import random 
from class_auto import Auto

class Gara: 
    def __init__(self, n_giri, auto):
        self.giri = n_giri
        self.auto = auto
        self.griglia = []
        
    def crea_griglia(self):
        random.shuffle(self.auto)
        return self.auto
        
    def simula_gara(self):
        griglia_iniziale = self.crea_griglia()
        self.stampa_griglia(griglia_iniziale)
        
        for giro in range(1,self.giri+1):
            griglia = self.crea_griglia()
            print(f"\ngiro numero: {giro}")
            self.stampa_griglia(griglia)
        
        print("\ngriglia di arrivo:")
        self.stampa_griglia(griglia)
        print(f"il vincitore è: {griglia[0].pilota.nome} {griglia[0].pilota.cognome}")
        
    def stampa_griglia(self,griglia):
        print(f"{"posizione":<10} {"nome":<10} {"cognome":<10} {"scuderia":<10} {"numero":<10}")
        posizione =1
        for auto in griglia:
            print(f"{posizione:<10} {auto.pilota.nome:<10} {auto.pilota.cognome:<10} {auto.scuderia:<10} {auto.numero:<10}")
            posizione += 1