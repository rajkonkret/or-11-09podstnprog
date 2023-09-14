# argumenty słownikowe

def connect(**opcje):  # ** - argumenty słownikowe tzw kwargs
    print(opcje)  # {'klucz': 'wartośc'}
    print(type(opcje))  # <class 'dict'>
    connect_paraam = {
        'host': '127.0.07',
        'port': '8080'
    }
    print(connect_paraam)
    connect_paraam['pwd'] = opcje
    print(connect_paraam)  # {'host': '127.0.07', 'port': '8080', 'pwd': {'klucz': 'wartośc'}}
    connect_paraam.update({'pwd2': opcje})
    print(connect_paraam)  # 'pwd2': {'klucz': 'wartośc'}
    print(connect_paraam['pwd'])  # {'klucz': 'wartośc'}
    print(connect_paraam['pwd']['klucz'])  # wartośc


connect(klucz="wartośc")  # {'klucz': 'wartośc'}
# connect()  # {}
connect(klucz="wartośc", root="/", port='9090')  # {'klucz': 'wartośc', 'root': '/', 'port': '9090'}
# {'host': '127.0.07', 'port': '8080', 'pwd': {'klucz': 'wartośc', 'root': '/', 'port': '9090'},
#  'pwd2': {'klucz': 'wartośc', 'root': '/', 'port': '9090'}}
connect(klucz='wartośc', a=8)  # {'klucz': 'wartośc', 'a': 8}
