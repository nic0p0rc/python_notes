#esercizi
'''
    1.algoritmo di euclide
    L'algoritmo effettua la divisione a:b e ne calcola il resto r.
    Se il resto è un intero positivo, divide b per r e ne calcola il resto. 
    L'algoritmo termina quando il resto è nullo ( r=0 ). 
    L'ultimo resto non nullo del processo è il Massimo Comune Divisore ( o MCD )dei due numeri.


def resto(a,b):
    r=a % b
    return algoritmo_d_euclide(b,r)
    
        
def algoritmo_d_euclide(b,r):
    if r == 0:
        return b
    else:
        return algoritmo_d_euclide(r,b%r)
    
       
print(resto(24,36))

'''

def algoritmo_d_euclide(a,b):
    if b == 0:
        return a
    else:
        return algoritmo_d_euclide(b,a%b)
    
       
print(algoritmo_d_euclide(36,48))
print(36%48)
print(48%36)