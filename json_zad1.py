# json  - {"name" : "Radek"}
# json obiekt typu klusz-wartosć
import json

person_dict = {'name': 'Radek', 'age': 50, 'czy_pali': None}
print(person_dict)
print(type(person_dict))  # <class 'dict'>
dane = json.dumps(person_dict)  # zamiana słownika na json
print(dane)  # {"name": "Radek", "age": 50, "czy_pali": null}
print(json.loads(dane))  # {'name': 'Radek', 'age': 50, 'czy_pali': None} - zamiana jsona na słownik

#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
# with - kontekst menadzer
with open('nasze_dane.json', 'w') as fh:
    json.dump(person_dict, fh, indent=4, sort_keys=True)
# {
#     "age": 50,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 50, 'czy_pali': None, 'name': 'Radek'}
print(type(data))

# wypisac ze słownika klucze, wartosci, pary

print(data.keys())
print(data.values())
print(data.items())

# <class 'dict'>
# dict_keys(['age', 'czy_pali', 'name'])
# dict_values([50, None, 'Radek'])
# dict_items([('age', 50), ('czy_pali', None), ('name', 'Radek')])