
numeri = input("inserisci i numeri che vuoi verificare (scrivi i numeri con uno spazio fra di loro:  ").split()
numeri_pari=[int(i) for i in numeri if int(i)%2 == 0]
print(f"i numeri pari sono {numeri_pari}")