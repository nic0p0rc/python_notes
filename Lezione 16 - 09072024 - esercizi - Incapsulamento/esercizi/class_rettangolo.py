class Rettangolo:
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
    
    def area(self):
        return self.larghezza*self.altezza
    
    def perimetro(self):
        return (self.larghezza*2)+(self.altezza*2)

rettangolo_di_prova = Rettangolo(5,10)
print(rettangolo_di_prova.area(), rettangolo_di_prova.perimetro())