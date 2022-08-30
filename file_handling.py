import csv

with open('CACA000.0_0900s.csv') as file:
    rows = csv.reader(file)
    for row in rows:
        print(row)