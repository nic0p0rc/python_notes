import math


def calcola_quadrato():
    lato_quadrato = float(input("inserisci il lato del quadrato: "))
    area = lato_quadrato**2
    perimetro = lato_quadrato*4
    
    print("l'area vale: {}, mentre il perimetro: {}" .format(area, perimetro))

def calcola_rettangolo():
    lato_rettangolo = float(input("inserisci il lato del rettangolo: "))
    altezza_rettangolo = float(input("inserisci l'altezza del rettangolo: "))
    area = lato_rettangolo*altezza_rettangolo
    perimetro = (lato_rettangolo*2)+(altezza_rettangolo*2)
    
    print("l'area vale: {}, mentre il perimetro: {}" .format(area, perimetro))
    
def calcola_cerchio():
    raggio= float(input("enserisci il valore del raggio: "))
    
    area= math.pi* math.pow(raggio, 2)
    print(f"il tuo cerchio di raggio {raggio} ha l'area pari a {area}")
 
scelta = int(input("scegli l'operazione: \n"
               "1. Calcola permitreo e area di un rettangolo\n"
               "2. Calcola area e perimetro di un quadrato\n"
               "3. Calcola area di un cerchio\n"))

if scelta == 1:
    calcola_rettangolo()
elif scelta == 2:
    calcola_quadrato()
elif scelta == 3:
    calcola_cerchio()
else:
    print("Scelta non valida")
