import csv

try:

    with open('libri2.csv', mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            
except FileNotFoundError:
    print("nome file non corretto o impossibile da trovare")
    
'''   
   
with open('libri.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''