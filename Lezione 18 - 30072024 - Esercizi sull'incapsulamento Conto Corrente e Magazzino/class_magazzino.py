class Magazzino: 
    def __init__(self, codice, descrizione, quantitaM, scorta = 0):
        self.setCodice(codice) 
        self.setDescrizione(descrizione)
        self.__quantitaM = quantitaM
        self.__scorta = scorta
    
    def __str__(self):
        return f"codice: {self.getCodice()} \ndescrizione: {self.getDescrizione()} \nquantità: {self.getQuantitaM()} \nscorta: {self.getScorta()}"
        
    def setCodice(self, codice):
        if len(codice) <= 12:
            self.__codice = codice 
        else: 
            print("deve essere di massimo 12 caratteri")
            
    def setDescrizione(self, descrizione):
        if len(descrizione) <= 50:
            self.__descrizione = descrizione
        else: 
            print("deve essere di massimo 12 caratteri")
            
    def ordine(self):
        if self.__quantitaM <= self.__scorta:
            return f"Devi ordinare: {self.__scorta-self.__quantitaM}"
        else:
            return "tutto ok"
            
    def cliente(self, ordine):
        if self.__quantitaM < ordine:
            return f"mancano: {ordine-self.__quantitaM}"
        else:
            self.__quantitaM -= ordine 
            return "ordine eseguito"
    
    def acquisto(self, rifornimento):
        self.__quantitaM += rifornimento
        return self.__quantitaM
    
    def getCodice(self):
        return self.__codice 
    
    def getDescrizione(self):
        return self.__descrizione
        
    def getQuantitaM(self):
        return self.__quantitaM
    
    def setQuantitaM(self, quantitaM):
        self.__quantitaM = quantitaM
    
    def getScorta(self):
        return self.__scorta
    
    def setScorta(self, scorta):
        self.__scorta = scorta