# Zmienne napisowe
zmienna1 = 'abc'
zmienna2 = "Konrad"

# Znmienna liczbowa
num1 = 15
num2 = 15.8
num3 = num1 + 14


# Zmienna znakowa
znak = 'A'
print(type(znak))
znak = 3
print(type(znak))
del(znak)

# Zmienna logiczna
log1 = True
log2 = log1

print('Tekst na ekran')
print(num1)
print(num2)
print(num3)
print(log1, log2)

""" Poczatek
komentarza
wielowierszowego
"""

''' Komentarz
wieloblokowy '''

print(type(num1))
print(type(num1), type(num2), type(zmienna1), type(log1))

# P1
a = 1
b = 2.4
c = 'w1'
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))

# P2
print('Przypisanie nowych wartosci zmiennym a, b, c')
a = 2.1
b = 'abc'
c = 0
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))

# P4
del(a)
# del(c)
c = str(c)
c += 'abc'
print(c)

# P5
imie = 'Adam'
nazwisko = 'Kowalski'
rokUrodzenia = '1950-06-15'
stanowisko = 'dyrektor'
placa = 1000000.1
print(imie + '\t' + nazwisko + ';' + rokUrodzenia + ';' + stanowisko + ';' + str(placa)+'\n')

# P6 Pole powierzchni kola
pi = 3.14
# r = 5
r = int(input('Podaj promien kola '))
polePowierzchniKola = pi * (r ** 2)
print('Pole kola o promieniu ' + str(r) + ' = ' + str(polePowierzchniKola))

# P7 Proba przypisania zmiennej do slowa kluczowego
"""and = 3
print(and)"""