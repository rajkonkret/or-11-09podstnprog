# pliki w formacie csv
# plik gdzie dane są oddzielone zankiem podziału(,;,tab)
# Radek,Maciek,Zenek
import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', 3, '9.1']

dict_x = [
    {'branch': 'COE', 'cgpa': 9.1, 'year': 3, 'name': 'Tomek'},
    {'branch': 'COE', 'cgpa': 9, 'year': 2, 'name': 'Tomek'},
    {'branch': 'COE', 'cgpa': 8.1, 'year': 1, 'name': 'Tomek'},
]

dict2 = dict(zip(fields, row))
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

filename = 'records.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(row)  # zapis pojedynczego wiersza
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter="^")
    # delimiter - wskazujemy znak odzielający elemnty w pliku csv
    csvwriter.writeheader()
    csvwriter.writerows(dict_x)
    csvwriter.writerow(dict2)
