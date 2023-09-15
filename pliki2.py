import chardet
import os

# pip install chardet

# file_path = 'test.log'
file_path = 'C:\\Users\\CSComarch\\PycharmProjects\\or-11-09podstnprog\\test.log'

file_path_2 = os.path.abspath('test.log')
# C:\Users\CSComarch\PycharmProjects\or-11-09podstnprog\test.log

print(file_path_2)
# wb - odczyt binarny (wymagania biblioteki)
# binarnie poniewaz przy odczycie tekstowym system interpretuje bajty a przy binarnym
# dostarcza bibliotece dokłądnie to co jest w pliku
with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)  # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
kodowanie = result['encoding']  # wyciagamy ze słownika wartosc dla klucza 'encoding'
confidence = result['confidence']

print(raw_data.decode(encoding=kodowanie))

print(kodowanie)  # utf-8 po zwiekszeniu próbki
print(confidence)  # 0.99
print(result)  # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
