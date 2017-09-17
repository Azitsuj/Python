# -*- coding: utf-8 -*-

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
r = 5
# r = int(input('Podaj promien kola '))
polePowierzchniKola = pi * (r ** 2)
print('Pole kola o promieniu ' + str(r) + ' = ' + str(polePowierzchniKola))

# P7 Proba przypisania zmiennej do slowa kluczowego
"""and = 3
print(and)"""

a = None
print(a)
print(type(a))

liczbaZesp1 = 2 + 3j
liczbaZesp2 = 1 + 1j
print(liczbaZesp1 + liczbaZesp2)
print(type(liczbaZesp1))

a = 3.4e+5
print(a)

# zrzucenie dziesietnej czesci z dzielenia
a = 3.0 // 2.0
print(a)

# P10 cena brutto netto
imie = 'Adam'
nazwisko = 'Kowalski'
rokUrodzenia = '1950-06-15'
stanowisko = 'dyrektor'
placaB = 5050.50
placaN = round(placaB/1.23,2)
print(imie + '\t' + nazwisko + ';' + rokUrodzenia + ';' + stanowisko + ';' + str(placaN) + ';' + str(placaB))

# P11
chleb = 1.99
mleko = 2.50
cukierki = 12.99
# zamowienie to 2 szt. chleba, 0.5 l mleka, 300 g cukierkow
zamowienie = round(2 * chleb + 0.5 * mleko + 0.3 * cukierki, 2)
print('zamowienie kosztuje ' + str(zamowienie) + ' zl')

a = 12
b = 1 -1j
# b = 1 + (-1)j - bledna definicja liczby zespolonej, j musi byc bezposrednio przy liczbie
print(a*b)

""" wejscie = input('Podaj napis: ')
flaga = bool(wejscie)
print(flaga) """
quote = '"ecie pecie"'
quote2 = "'pecie ecie'"
print(quote)
print(quote2)
print('Ten napis'+'\n'+'ma'+'\n'+'wiele'+'\n'+'linii')
print('Ten napis \tma \twiele \ttabulatorow')
print('''abc
cda
koniec''')
# zmienia typ zakonczenia printa, zamiast nowej linii jako domyslnej, ustawia '...'
print('abc'+'\n'+'csa', end='...')
print('kolejny napis')
print('abc'+'\n'+'csa', end='')
print('kolejny napis')
koniec = 'abc'
print('abc'+'\n'+'csa', end=koniec)
print('kolejny napis')

