#
# CRUD - create, read, update, delete
# POST, GET, PUT, DELETE
#
# komunikacja po REST Api
# API NBP - > HTTP GET
# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
# table - dostepne tabele czyli A, B, C
# code - kod iso waluty
import requests as re

# pip install requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = re.get(url)
print(response)
# <Response [200]> - ok
# 3.. błedy przekierowania
# 4.. 400 bad request, 404 - zasób nie istnieje
# 5.. wewnętrzne błedy serwera

table = response.json()
print(table)
print(type(table))  # <class 'dict'>
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '179/A/NBP/2023', 'effectiveDate': '2023-09-15', 'mid': 4.6307}]}

print(table['table'])
print(table['currency'])
print(table['code'])

print(table['rates'])  # [{'no': '179/A/NBP/2023', 'effectiveDate': '2023-09-15', 'mid': 4.6307}]
print(table['rates'][0])  # {'no': '179/A/NBP/2023', 'effectiveDate': '2023-09-15', 'mid': 4.6307}
print(table['rates'][0]['mid'])  # 4.6307, usd = 4.3418
