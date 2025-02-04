#calcolo dei primi 10 numeri da 0 a 9
'''num1 = 10
somma = 0
for i in range(num1):
    somma += i

print("La somma dei primi", num1, "numeri da 0 a", num1-1, "è:", somma)'''


#quadrato di asterischi
'''numeroRighe = int(input("Inserisci il numero di righe del lato: "))

for i in range(numeroRighe):
    for y in range(numeroRighe):
        print("*", end=" ")
    print() '''

#Primo esercizio VOLTA
'''Calcola l'area di un cerchio utilizzando la costante PI=3.14. Chiedi
all'utente di inserire il raggio del cerchio e stampa l'area calcolata.'''
'''import math

def calcolo_cerchio():
    raggio= float(input("enserisci il valore del raggio: "))
    
    area= math.pi* math.pow(raggio, 2)
    print("il tuo cerchio di raggio {} ha l'area pari a {:.2f}".format(raggio, area))

calcolo_cerchio()'''

#Secondo esercizio VOLTA
'''Scrivi un programma che converta una temperatura da Celsius a
Fahrenheit. Chiedi all'utente di inserire una temperatura in gradi
Celsius e stampa la temperatura equivalente in gradi Fahrenheit con
la seguente formula: (gradi*9/5)+32.'''

'''gradiCelsius = float(input("inserisci i gradi Celsius: "))
gradiFahrenheit = (gradiCelsius*9/5)+32
print(f"{gradiCelsius} gradi celsius in fahrenheit sono: {gradiFahrenheit}")'''

#Terzo esercizio VOLTA
'''Scrivi un programma che prenda in input il raggio di un cerchio e
calcoli l'area e la circonferenza del cerchio.'''
'''import math 

def calcola_permietro_cerchio():
    raggio = float(input("inserisci il valore del raggio: "))
    
    perimetro = "{:.2f}".format(math.pi*2*raggio)
    print(f"il perimtreo del cerchio di raggio {raggio} vale: {perimetro}")

def calcolo_cerchio():
    raggio= float(input("enserisci il valore del raggio: "))
    
    area= "{:.2f}".format(math.pi* math.pow(raggio, 2))
    print(f"il tuo cerchio di raggio {raggio} ha l'area pari a {area}")

scelta = int(input("1. Calo perimetro cerchio\n"
                   "2. Calcola area cerchio\n"))
if scelta == 1:
    calcola_permietro_cerchio()
elif scelta ==2:
    calcolo_cerchio()
else:
    print("devi scelgere un numero da 1 a 2")'''
    
#Quarto esercizio VOLTA
'''Scrivi un programma che calcoli l'area di un triangolo. Chiedi
all'utente di inserire la base e l'altezza del triangolo.'''
'''def calcolo_triangolo(base, altezza):
    return (base*altezza)/2

base_triangolo = float(input("inserisci il valore della base: "))
altezza_triangolo = float(input("inserisci il valore dell'altezza: "))
area = calcolo_triangolo(base_triangolo, altezza_triangolo)
print("l'area del triangolo di base {} e altezza {} è: {:.2f}".format(base_triangolo, altezza_triangolo, area))'''

#Quinto esercizio 
'''Scrivi un programma che prenda un numero decimale in input e stampi 
la sua parte intera e la sua parte frazionaria separatamente'''
'''
numero_decimale = float(input("inserisci un numero decimale: "))

parte_intera = numero_decimale // 1
parte_frazionaria = numero_decimale % 1

print(parte_intera)
print("{:.2f}".format(parte_frazionaria))'''

#Quinto esercizio V.2
'''Scrivi un programma che prenda un numero decimale in input e stampi 
la sua parte intera e la sua parte frazionaria separatamente'''
'''
numero_decimale = float(input("inserisci un numero decimale: "))

parte_intera = int(numero_decimale)
parte_frazionaria = numero_decimale - parte_intera

print(parte_intera)
print("{:.2f}".format(parte_frazionaria))'''

#sesto esercizio
'''Scrivi un programma che calcoli il prezzo finale di un prodotto dopo l'applicazione 
    di uno sconto del 20%.Chiedi all'utente di inserire il prezzo originale del prodotto'''
''' 
prezzo_originale = float(input("inserisci il prezzo originale del prodotto: "))
 
sconto = prezzo_originale *0.20
prezzo_finale= prezzo_originale - sconto
 
print("il prezzo finale del prodotto dopo 20% di sconto è: ", prezzo_finale)'''
