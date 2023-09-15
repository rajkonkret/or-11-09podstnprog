import chardet

# pip install chardet

file_path = 'test.log'

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
