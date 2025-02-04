import csv
 
with open('output.csv', mode='r') as file: 
    reader = csv.reader(file)

    for row in reader:
        print(row)