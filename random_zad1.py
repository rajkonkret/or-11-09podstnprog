# random - generowanie liczb pseudolosowych
import random

print(random.randint(1, 6))  # int 1..6
print(random.random())  # 0.1520810875812425 float 0..0.9999999
print(random.random() * 6)  # float od 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # 1..49
print(lista2)
# print(help(range))  - wydrukowanie podręcznej dokumentacji

# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)

print(random.choices(lista2, k=6))  # [30, 18, 18, 39, 27, 49] - losuje z powtórzeniami
print(random.sample(lista2, 6))  # losuje bez powtórzeń
