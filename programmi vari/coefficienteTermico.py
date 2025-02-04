''' programma realizzato da Nicolò Porcelluzzi 
    in data 11/04/2024
    permette di calcolare il coefficiente termico dei materiali '''
    
def calcolo_coefficiente_termico(delta_l, lunghezza_iniziale, delta_t):
    return delta_l/(lunghezza_iniziale*delta_t)

#dati di input

delta_lunghezza = float(input("inserisci la variazione di lunghezza del materiale (m): "))
delta_temperatura = float(input("inserisci la variazione di temperatura del materiale (°C): "))
l0 = float(input("inserisci la lunghezza iniziale del materiale (m): "))
nome_materiale = input("inserisci il nome del materiale: ")
#colcolo coefficiente termico con funzione
lambda_risultato = calcolo_coefficiente_termico(delta_lunghezza, l0, delta_temperatura)

#Stampa il risultato in notazione scientifica
print("\nIl coefficiente termico (λ) del {} è {:.2e}".format(nome_materiale, lambda_risultato))