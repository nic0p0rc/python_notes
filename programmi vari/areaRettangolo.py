def calcolo_area_quadrato(base, altezza):
    return base*altezza
    
def calcolo_perimetro_quadrato(base):
    return base*4
    
lato_quadrato = float(input("inserisci la lunghezza della base del triangolo: "))
altezza_quadrato = float(input("inserisci la lunghezza dell'altezza del triangolo: "))
area_quadrato = calcolo_area_quadrato(lato_quadrato, altezza_quadrato)
perimetro_quadrato = calcolo_perimetro_quadrato(lato_quadrato)
print("area del quadrato", area_quadrato)
print("perimetro del quadrato", perimetro_quadrato)