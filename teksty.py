tekst = "Witaj świecie"
print(tekst)  # Witaj świecie

print(tekst.upper())  # wypisze tekst dużymi literami
# WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
tekst2 = tekst.upper()
#  """ Return a copy of the string converted to uppercase. """
print(tekst2)  # WITAJ ŚWIECIE

# tekst.lower()
# teksty są niemutowalne

tekst3 = tekst.lower()
print(tekst3)
print(tekst3)  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst.replace("ś", " "))  # "Witaj  wiecie"
print(tekst)  # Witaj świecie
encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - ciąg binarny(bajtowy)
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # z lewej włacznie, z prawej zbiór niedomknięty
print(tekst.count("j", 0, 4))  # 0 razy, z lewej włacznie, z prawej zbiór niedomknięty
# Witaj
# 01234

print(len(tekst))  # 13
print(tekst)
print(len(tekst))
# 13:30

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona \b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię Pythona"
euro_sign = "\u20AC"
print(euro_sign)  # €

starszy = "Witaj %s"
print(type(starszy))  # <class 'str'>
print(starszy % imie)  # Witaj Radek

print("""
Tekst 
    wielolinijkowy """)
# "Tekst
#     wielolinijkowy
# "
print("""



""")
