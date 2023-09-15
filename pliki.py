# with - kontekst menadzer
with open('test.log', 'w', encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("jeszcze jedno\n")

# w nadpisuje plik, gdy istnieje usuwa
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Radek\n")

# a append - dopisanie do istniejacego pliku
with open('test.log', 'a', encoding='utf-8') as file:
    file.write("dodane\n")
    file.write("dodane\n")
    file.write("dodane\n")
    file.write("dośdane\n")

with open('test.log', 'r', encoding='utf-8') as file:
    lines = file.read()

print(lines)