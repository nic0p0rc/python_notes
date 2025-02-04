class Car: 
    def __init__(self, resa ,livello = 0):
        self.resa = resa
        self.__livello = livello
    
    def __str__(self):
        return f"livello: {self.getGas("nik")} resa: {self.resa}"
    def addGas(self, rifornimento):
        self.__livello += rifornimento
        
    def getGas(self, password):
        if password == "nik":
            return self.__livello
        else: 
            return "non hai accesso a questa risorsa"
    
    def drive(self, distanza):
        if distanza/self.resa >= self.getGas("nik"):
            return "Non puoi partire per il viaggio, devi fare rifornimento"
        else: 
            self.__livello -= (distanza/self.resa)
            return f"Puoi partire per il tuo viaggio, nel serbatoio ci sono {self.getGas("NIK")}"