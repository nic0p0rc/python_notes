class Conto:
    def __init__(self, saldo = 0):
        self.movimenti = []
        self.__saldo = saldo
        
    def __str__(self):
        return f"Nel saldo hai {self.getSaldo()}"
    
    def addSoldi(self, deposito):
        self.movimenti.append("d" + str(deposito))
        self.__saldo += deposito
    
    def prelievo(self, ritiro):
        self.movimenti.append("p" + str(ritiro))
        self.__saldo -= ritiro
    
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, nuovo_saldo):
        self.__saldo=nuovo_saldo
