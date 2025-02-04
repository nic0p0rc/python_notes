def somma(n):
    #print(n)
    if n <= 2:
        return n
    elif n%2 == 0:
        return n + somma(n-2)
    
print(somma(5))


def somma(n):
    #print(n)
    if n <= 1:
        return n
    elif n%2 != 0:
        return n + somma(n-1)
    else:
        return somma(n-1)
      
print(somma(6))
