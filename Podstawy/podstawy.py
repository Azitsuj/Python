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

imie = 'Konrad'
print((imie + ' ') * 3)

# P16 konwersja liczby do wartosci logicznej
liczba = 7
flaga = bool(liczba)
print(flaga)

# P25 stawka netto/brutto pracownika
wynagrodzenieN = 5500
godziny = 168
podatek = 0.19
stawkaZaGodzineN = round(wynagrodzenieN / godziny, 2)
stawkaZaGodzineB = round((wynagrodzenieN * (1 + podatek)) / godziny, 2)
print('stawka za godzine brutto: ' + str(stawkaZaGodzineB) + ' zl')
print('stawka za godzine netto: ' + str(stawkaZaGodzineN) + ' zl')
print('stawka za godzine netto:', str(stawkaZaGodzineN), 'zl')

# P26 prawo de Morgana
"""q = bool(input('podaj q '))

dM1 = not( p and q )
dM2 = not p or not q
print(dM1 == dM2)
"""

# P27
print('a' and 'b')
print('' and 'a')
a = 0
b = 1
c = 0
G1 = not a and not b and not c
G2 = not a and not b and c
G3 = not a and b and not c
G4 = a and not b and not c

GRes = G1 or G2 or G3 or G4
print('not a', not a)
print('not b', not b)
print('not c', not c)
print('a or b or c =', a or b or c)
print('G1',G1)
print('G2',G2)
print('G3',G3)
print('G4',G4)
print('GRes',GRes)

znak = 'a'
# ord - przejscie ze znaku na kod ASCII
kod = ord(znak)
print(znak, kod)
# chr - przejscie z ASCII na znak
print(chr(kod))

# P28 pierwiastek ntego stopnia
x = -17
pierwiastek = x ** (1/2)
print(pierwiastek)
print(type(pierwiastek))
im = 1j
multi = (-17) ** (1/2)
liczba = multi * im
print(liczba)

# P29 17 / 7
Z = 17 % 7
print(Z)
print('Wynik:',Z ** 2 + 3 * Z)

# P30
print((str(1.2e+3+24.5)+';')*20)
print((str(1.2e+3+24.5)+';')*19 + str(1.2e+3+24.5))

print('C:\\Dokumenty\\nowy dokument')
print(' text \' text \"b dsad')
# print('\a')

# P35
# imie = input('Podaj imie: ')
print('Hello '+imie+'!')

# P38
"""
P = float(input('Podaj stopę procentową: '))
N = float(input('Podaj liczbę miesięcy: '))
res = round(SPK * (1 + P/100) ** (N/12),2)
print('Do spłaty: ' + str(res) + ' zł')
"""
txt = 'napis'
print(txt[0])
print(txt[4])
print(txt[len(txt)-1])
""" to polecenie zwroci blad
txt[1] = b """
print(txt.capitalize())
txt2 = 'ala ma kota a kot ma ale'
print(txt2.count('kot'))
print(txt2.count(' kot '))

"""
wiek = input('Podaj wiek: ')
if(wiek.isdigit()):
    print('jest ok')
    wiek = int(wiek)
else:
    print('błędny wiek')
"""
napis = 'abc'
lista = ['1','2','3','4','5']
print(napis.join(lista))
txt2 = txt2.replace('kot','pies')
print(txt2)
print(txt2.split('pies'))
data='2010-02-05'
lista = data.split('-')
print(lista)
print(lista[1])

#
# Listy
#

lista = [2,3.14,'a','abc']
print(lista)
print(lista[3])
lista.append('nowy element')
print(lista)
print(lista[1:])
print(lista[:4])
print(lista[1:3])
lista[2] = 'a2'
print(lista)

ola = ['O', 'L', 'A']
imiona = ['Ala', ola, 'Ela']
nazwiska = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
ListaList = [imiona, nazwiska]
print(str(ListaList[0][1][0:]) + ListaList[1][1])
print(nazwiska[0 :: 2])

nazwiska *= 2
print(nazwiska)
# nazwiska.clear()
print(nazwiska)
# del(nazwiska)
print(len(nazwiska))
print(len(ListaList[0]))
print(nazwiska[0])
del(nazwiska[0])
print(nazwiska[0])
nazwiska.insert(1, 'wartość')
print(nazwiska)
print(('A' or 'B') in nazwiska)

print(list('napis'))
print(str(list('napis')))
L = ['a', 2, 3, 2]
print(L.index(2))
print(L)
L.reverse()
print(L)
num = [11, 3, 5, 6, 2, 9, 4, 8]
num.sort()
print(num)

# P lista trzech produktow
"""
Arty = ['chleb', 'mleko']
Ceny = [3.14, 10]
iloscCh = float(input('Ile chleba: '))
iloscM = float(input('Ile mleka: '))
Ilosc = [iloscCh, iloscM]
doZaplaty = Ceny[0] * Ilosc[0] + Ceny[1] * Ilosc[1]
print('Do zaplaty:', round(doZaplaty, 2), 'zł')
"""
#
# Krotki / tuple
#

# nie polecany sposob tworzenia krotki/tuple
krotka = 1, 2, 3
print(krotka)

krotka = (1, 'abc', True)
print(krotka)
print(len(krotka))
print(krotka[1])
# krotka[1] = 2 - nie mozna przypisywac do krotek
A = list(krotka)
A[1] = 2
print(A)
krotka = krotka[:2]
print(krotka)

# P43 Data waznosci artykulu
"""
DataW1 = ('01', '01', 2017)
DataW2 = ('23', '10', 2018)
DataW3 = ('15', '12', 2019)
Produkty = (DataW1, DataW2, DataW3)
nrProd = int(input('Podaj numer produktu: ')) - 1
if nrProd < 0 or nrProd > 2:
    print('Zły numer produktu!')
else:
    print('Data ważności artykułu:', str(Produkty[nrProd][0])+ '-' + str(Produkty[nrProd][1]) + '-' + str(Produkty[nrProd][2]))
"""

#
# Slowniki
#

S = {'a': 1, 1: 'jeden'}
print(S['a'])
S['a'] = 3
print(S['a'])
print(S)
S1 = S.copy()
print(S1)
print(1 in S.values())

listaX = ['a', 'b', 'c', 'd']
romanCov = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
"""
dec = int(input('Podaj cyfrę dziesiętną: '))
if dec in romanCov.keys():
    print(romanCov[dec])
else:
    print('Zła cyfra!')
"""
romanCov = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
romanCov2 = {0:'0', 1:'X'}
romanCov.update(romanCov2)
print(romanCov)
print('0' in romanCov.values())

a = True
print(not a)

a = 3.14
pi = 'Pi = ' + str(a)
print(type(pi))
a='3'
b = int(a)
print(type(a))
print(type(b))

A = set([1, 2])
B = set([1, 3])
C = A & B
D = A | B
print(C)
print(D)

#
# Python D2
#

# Zbiory
zbior1 = set(['k', 1, False])
zbior2 = frozenset([1, 2, 3])
zbior1.add(21)
zbior1.add('k')
print(zbior1)
print('k' in zbior1)
print(set([1, False, 2]) <= zbior1)
print(len(zbior1))

A =set([1, 2, 3, 4, 5])
B = set([2, 4, 6, 8, 10])
print(A | B) # suma
print(A & B) # czesc wspolna
print(A - B) # roznica
print(A ^ B) # roznica symetryczna

#import random
from random import randint
print(randint(1, 49))

losowanie = set()
i = len(losowanie)
print(i)
while i < 6:
    los = randint(1, 49)
    losowanie.add(los)
    print(los)
    i = len(losowanie)
print(losowanie)


wylosowane = set()
los1 = randint(1, 49)
wylosowane.add(los1)
los2 = randint(1, 49)
wylosowane.add(los2)
los3 = randint(1, 49)
wylosowane.add(los3)
los4 = randint(1, 49)
wylosowane.add(los4)
los5 = randint(1, 49)
wylosowane.add(los5)
los6 = randint(1, 49)
wylosowane.add(los6)

if(len(wylosowane) == 6):
    print(wylosowane)
elif(len(wylosowane) == 5):
    los7 = randint(1, 49)
    wylosowane.add(los7)
    print(wylosowane)
elif(len(wylosowane) == 4):
    los8 = randint(1, 49)
    wylosowane.add(los8)
    los9 = randint(1, 49)
    wylosowane.add(los9)
    print(wylosowane)
else:
    print("Masz pecha!")

a = randint(1, 100)
dzielnik = randint(2, 5)
print("Liczba " + str(a) + " jest podzielna przez " + str(dzielnik)) if (a % dzielnik == 0) else print("Liczba " + str(a) + " nie jest podzielna przez " + str(dzielnik))

# P54

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# index = int(input("Podaj numer indeksu wiekszy od 0: "))
index = randint(1, 12)
print(index)
index -= 1
if ((index <= len(lista) - 1) and (index >= 0)):
    print(lista[index])
else:
    print("Zly numer indeksu, podaj jeszcze raz!")
    
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# index = int(input("Podaj numer indeksu wiekszy od 0: "))
index = randint(1, 12)
print(index)
if ((index <= len(lista)) and (index > 0)):
    print(lista[index -1])
else:
    print("Zly numer indeksu, podaj jeszcze raz!")

# P55
lista = [1, 2, 5, 7]
if lista[0] > 0 and lista[1] > 0:
    print("Pierwszy i drugi element jest dodatni")
elif lista[0] > 0 and lista[1] <= 0:
    print("Pierwszy element jest dodatni, a drugi nie")
elif lista[0] <= 0 and lista[1] > 0:
    print("Pierwszy element nie jest dodatni, a drugi jest")
else:
    print("Oba elementy sa niedodatnie")
    
# P56
#liczba =int(input("Podaj liczbe: "))
liczba = randint(1, 100)
print("Liczba " + str(liczba) + " jest parzysta") if (liczba % 2 == 0) else print("Liczba " + str(liczba) + " jest nieparzysta")

# P56
flaga = True
napis1 = str(input("Podaj pierwszy napis: "))
napis1L = napis1.lower()
napis2 = str(input("Podaj drugi napis: "))
napis2L = napis2.lower()
print("Napis1: " + str(napis1L) + ", napis2: " + str(napis2L))
if (not napis1.isdigit()):
    print('ok')
else:
    flaga = False
if (not napis2.isdigit()):
    print('ok')
else:
    flaga = False

if flaga:
    """
    if napis1L > napis2L:
        print(napis1L + " jest wiekszy niz " + napis2L)
    elif napis1L == napis2L:
        print(napis1L + " = " + napis2L)
    else:
        print("2 jest wiekszy niz 1")
    """
    if napis1.lower() > napis2.lower():
        print("A > B")
    elif napis1.lower() == napis2.lower():
        print("A = B")
    else:
        print("A < B")
else:
    print('błąd')

