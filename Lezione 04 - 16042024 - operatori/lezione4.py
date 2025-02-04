#input da tastiera
'''
nome=input("inserisci il tuo nome: ") 
anni=input("inserisci la tua età: ")
print(f"{nome}, {anni}")'''


#casting dei dati
'''
lato=float(input("inserisci il lato del quadrato: "))
area= lato**2
print(area)'''


#operatori aritmetici
'''numero1=44
numero2=6
risultato=numero1+numero2
print(risultato)
risultato=numero1-numero2
print(risultato)
risultato=numero1*numero2
print(risultato)
risultato=numero1/numero2
print(risultato)
risultato=numero1//numero2
print(risultato)
risultato=numero1%numero2
print(risultato)
risultato=numero1**numero2
print(risultato)'''


#operatori di assegnazione
'''prima=27
print(prima)
dopo=prima
dopo+=30
print(dopo)
dopo-=12
print(dopo)
dopo*=2
print(dopo)
dopo/=10
print(int(dopo))
dopo//=2
print(int(dopo))
dopo%=3
print(dopo)'''


#operatori di confronto
'''num1=23
num2=23
risultato=num1==num2
print(risultato)
risultato=num1!=num2
print(risultato)
risultato=num1<num2
print(risultato)
risultato=num1>num2
print(risultato)
risultato=num1<=num2
print(risultato)
risultato=num1>=num2
print(risultato)'''


#operatori logigici
'''var1=True
var2=0
risultato = var1 & var2 #possiamo utilizzare and oppure &
print(risultato)
risultato = var1 | var2 #possiamo utilizzare or oppure |
print(risultato)
risultato = var1 or var2 
print(risultato)
risultato = not var2 
print(risultato)'''

#operatori di identità
'''var1=10
var2=10
var3="10"
risultato=var1 is var2
print(risultato)
risultato=var1 is var3
print(risultato)
risultato=var1 == var2
print(risultato)
risultato=var1 is not var2
print(risultato)

var4 = [1,2,3] #lista (struttura di dati)
var5 = [1,2,3]
ris=var4 is var5
print(ris)'''


#operatori di appartenenza
'''var1="corso python"
var2="python"
var3=[1,2,3]
ris= var2 in var1
print(ris)
ris= 4 in var3
print(ris)
ris= 4 not in var3
print(ris)'''

#operatori di bitwise
a=5
b=7
ris= a & b
print(ris)