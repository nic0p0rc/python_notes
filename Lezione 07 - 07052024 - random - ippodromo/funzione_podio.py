import random

def podio_fun():
    podio = []
    i=0
    while i<3:
        numero_casuale = random.randint(1,10)
        if numero_casuale not in podio:
            podio+= [numero_casuale]
            i+=1
    return podio
    
print(podio_fun())