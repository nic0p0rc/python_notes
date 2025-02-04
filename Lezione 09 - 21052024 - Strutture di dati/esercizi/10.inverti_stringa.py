#trasforma str in lista e da lista usa reverse
stringa="buonasera a tutti"
stringa_lista=list(stringa)
stringa_lista.reverse()
print(stringa_lista)

stringa_nuova = ""
for i in range(len(stringa)-1,-1,-1):
    stringa_nuova+=stringa[i]
print(stringa_nuova)
    
  
stringa_nuova= stringa[::-1]
print(stringa_nuova)