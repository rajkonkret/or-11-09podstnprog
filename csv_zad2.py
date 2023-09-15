import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    # wyszukanie automatyczne znaku podziału dla pliku csv
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.quotechar)
    print(dialect.delimiter)
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x00000221237372E0>
    print(type(csvreader))  # <class '_csv.reader'>
    csv_f.seek(0)  # ponowne ustawienie odczytu na początek pliku
    fields = next(csvreader)  # iterator, pobiera element i ustawia wskaźnik na nastepny

    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)
