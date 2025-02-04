
class Auto:
    def __init__(self,scuderia, pilota, numero):
        self.scuderia = scuderia
        self.pilota = pilota 
        self.numero = numero 
    
    def __str__(self):
        return f"{self.scuderia} {self.pilota} {self.numero}"