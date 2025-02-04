
class Studente:
    def __init__(self, nome, cognome, matricola):
        self.__nome = nome
        self.cognome = cognome
        self.matricola = matricola
        
    def __str__(self):
        return f"Lo studente {self.matricola} si chiama {self.__nome} {self.cognome}"
        
    def getNome(self, password = ""):
        if password == "nik":
            return self.__nome
        else:
            return "accesso negato"
    
    def setNome(self, nuovo_nome): 
        self.__nome = nuovo_nome
    