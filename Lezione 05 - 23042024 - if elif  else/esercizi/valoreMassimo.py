
num_1 = int(input("inserisci il primo numero: "))
num_2 = int(input("inserisci il secondo numero: "))
num_3 = int(input('inserisci il terzo numero: '))

if num_1 >= num_2 and num_1 >= num_3:
    valore_massimo = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    valore_massimo = num_2
else:
    valore_massimo = num_3
    
print(f"il valore massimo è uguale a: {valore_massimo}")