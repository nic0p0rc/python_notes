import csv

data = [
        ['Nome', 'Cognome', 'Età'],
        ['Alice', 'Rossi', 30],
        ['Bob', 'Verdi', 251],
        ['Carol', 'Bianchi', 35]
]

#mode (a)ppend fa scrivere il file aggiungendo "data" mode (w)rite 
#riscrive il file ogni volta
with open('output.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)

