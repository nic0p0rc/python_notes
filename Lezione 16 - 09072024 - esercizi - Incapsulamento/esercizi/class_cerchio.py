import math

class Cerchio:
    #attributo raggio
    def __init__(self, raggio):
        self.raggio = raggio
    
    #metodi
    def area(self):
        print("L'area del cerchio di raggio {} vale: {}".format(self.raggio,math.pi*pow(self.raggio,2)))
    
    def circonferenza(self):
        print("La circonferenza del cerchio di raggio {} vale: {}".format(self.raggio,math.pi*self.raggio*2))
        
    def area_circ(self):
        self.area()
        self.circonferenza()
    
    def setRaggio(self, nuovo_raggio):
        self.raggio = nuovo_raggio
    
    def getRaggio(self):
        return self.raggio