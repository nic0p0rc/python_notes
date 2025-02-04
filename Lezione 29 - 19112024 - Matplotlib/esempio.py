import matplotlib.pyplot as plt
import numpy as np

mq = np.random.randint(100,size=50) # generiamo 50 valori casuali compresi tra 0 e 100
price = np.power(mq,2)*10 # generiamo i valori del prezzo come il quadrato dei metri quadri moltiplicato per 10
noise = np.random.rand(50)*25000 # creiamo un po' di rumore...
price = (price+noise) # ...e aggiungiamolo al prezzo

plt.title("Rapporto dimensione-valore di monolocali")
plt.xlabel("Dimensione in metri quadri")
plt.ylabel("Valore in euro")
plt.grid()

mq_center = np.random.randint(100,size=10)
price_center = np.power(mq_center,2)*1.5
noise = np.random.rand(10)*2500
price_center = (price_center+noise)*10

plt.scatter(mq,price,marker='o', c='blue',label='Appartamenti in periferia')
'''
marker= 's' sta per quadrato
marker * sta per stellina
marker ^ sta per triangolino
marker x per x'''
plt.scatter(mq_center,price_center, marker='x' ,c='red', s=100, label='Appartamenti in centro')#colore o in nome o in esadecimale
plt.legend()

plt.savefig("scatter.png")
plt.show()




