class Studente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        
    def informazioni(self):
        print(f"Lo studente {self.matricola} si chiama {self.nome} {self.cognome}")
    
    