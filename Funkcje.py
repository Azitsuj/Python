# -*- coding: utf-8 -*-
from random import randint
import pymysql

res = 0

def dodawanie(a, b):
    global res
    res = a + b
    print(res)

def odejmowanie(a, b, c = 0, d = 0):
    res = a - b - c - d
    print(res)
    return res
'''
@overload
def odejmowanie(a, b):
    res = a - b
    print(res)

odejmowanie(1, 2)
odejmowanie(1, 3, 4)
'''

def wypisz(sekwencja):
    for x in sekwencja:
        print(str(sekwencja) + ': ' + str(x))
        
def baza(imie, nazwisko, wiek, imie2 = 'b/d', fajowy = False):
    rekord = []
    rekord.append(imie.capitalize())
    rekord.append(imie2.capitalize())
    rekord.append(nazwisko.capitalize())
    if(imie[len(imie) - 1] == 'a'):
        rekord.append("K")
    else:
        rekord.append("M")
    rekord.append(wiek)
    rekord.append(fajowy)
    return rekord

'''
print(res)
dodawanie(3, 4)
dodawanie(3.25, 5)
print(res)
del(dodawanie)
wynik = odejmowanie(2, 3)
print(wynik)

K = (1, 2, 3, 4, 5)
L = [5, 4, 3, 2, 1]
wypisz(L)
wypisz(K)
# dodawanie(1, 2)
print('Wynik odejmowania: ' + str(odejmowanie(5, 2, 3)))
print('Wynik odejmowania: ' + str(odejmowanie(5, 2)))
print('Wynik odejmowania: ' + str(odejmowanie(a = 5, b = 2, d = 1)))
print('Wynik odejmowania: ' + str(odejmowanie(5, 2, d = 1)))

print(baza(imie = 'Konrad', nazwisko = 'J', wiek = 123))
print(baza(imie = 'Katarzyna', nazwisko = 'J', wiek = 123, fajowy = True, imie2='abc'))
wynik = baza(imie = 'Katarzyna', nazwisko = 'J', wiek = 123, fajowy = True, imie2='abc')
print(wynik[:3])

'''

def silnia(a):
    wynik = 1
    a = int(a)
    while (a > 0):
        wynik *= a
        a -= 1
    return wynik
        
print(silnia(5))
print(silnia(10))
print(silnia(8.12))

# P70
# ciąg Fibonacciego

def fib(a):
    i = 2
    F = [0, 1]
    while(i < a):
        F.append(F[i-1] + F[i -2])
        i += 1
    return F

def fibres(L):
    suma = 0
    for x in L:
        suma += x
    print('Suma ciągu Fibonacciego: ' + str(suma))
    print('Wartość dla wybranego elementu: ' + str(L[len(L) - 1]))

print(fib(10))
print(fibres(fib(10)))

# P71 zdanie z losowych wyrazów

def randSent(n = 5):
    Words = ['Ala', 'ma', 'kota', 'a', 'kot', 'ma', 'Alę']
    sentence = ""
    i = 0
    while (i < n):
        sentence += Words[randint(0, 6)] + ' '
        i += 1
    sentence = sentence[:1].upper() + sentence[1:len(sentence) - 1] + '.'
    return sentence

print(randSent())

# P74 srednia z dowolnej ilosci argumentow
def srednia(*arg):
    x = 0
    i = 0
    if len(arg) == 0:
        return 0
    elif arg == 0:
        return 0
    else:
        for v in arg:
            x += v
            i += 1
        return(x/i)

print(srednia(10, 2, 3))
print(srednia(0))
print(srednia())

# to był mój pomysł
def zdanie(a):
    W = ['Ala', 'kot', 'ma', 'kota', 'Ale']
    E = []
    while(a > 0):
        E.append(W[randint(0, len(W) - 1)])
        a -= 1
    i = 0
    print(E)
    while i < len(E):
        if i == 0:
            print(E[i].capitalize(), end=' ')
            i += 1
        elif i < len(E) - 1:
            print(E[i], end = ' ')
            i +=1
        else:
            print(E[i] + '.')
            break
      
zdanie(5)

# tabliczka mnożenia
T = []
for i in range(1, 11):
    for j in range(1, 11):
        T.append(i * j)
        if j != 10:
            print('{:>4d}'.format(T[(i- 1) * 10 + (j - 1)]), end= ' ')
        else:
            print('{:>4d}'.format(T[(i- 1) * 10 + (j - 1)]))
            # print('Zwykła lista wygląda tak: ' + str(T))
            

# P74 002
def wykres(i = 1, symbol='*'):
    while (i > 0):
        a = randint(1, 19)
        print('{:<20s}'.format(symbol * a) + ' | ' + '{:>20s}'.format(symbol * a))
        i -= 1

wykres(3)
wykres(5, '~')

# P74 005
def napis(color = 0000, font_size = 10, napis = 'brak napisu'):
    print('<span style="color: ' + str(color) + '; font-size: ' + str(font_size) + 'px“>' + napis + '</span>')
    
napis()
napis(12, 3, 'To jest testowy napis')

# P74 008 naprzemiennie dwa kolory, czarny i biały + licznik uruchomienia funkcji <= 5

color = 'black'
i = 0

def kolory():
    global color, i
    if (i >= 5):
        print('{:>10s}'.format('error'))
    else:
        if color == 'black':
            print('White')
            color = 'white'
            i += 1
        else:
            print('Black')
            color = 'black'
            i += 1

        
kolory()
kolory()
kolory()
kolory()
kolory()
kolory()
kolory()
kolory()

# P74 120
'''while(True):
    menu = input('Podaj co chcesz uruchomić (\'+\' / \'-\' / q): ')
    if (menu == '+'):
        a = int(input('Podaj pierwszy argument dodawania: '))
        b = int(input('Podaj drugi argument dodawania: '))
        dod = dodawanie(a, b)
        
    elif (menu == '-'):
        a = int(input('Podaj pierwszy argument odejmowania: '))
        b = int(input('Podaj drugi argument odejmowania: '))
        od = odejmowanie(a, b)
        
    else:
        print('Wyszedłeś z programu')
        break
'''

# P74 230 potegowanie liczby x do y

def potega(x, y):
    global pow
    pow = 1
    i = 0
    while(i < y):
        pow *= x
        i += 1
    return pow

print(potega(2, 4))
print(pow + 2)

def frange(start, stop, krok):
    if (stop < start):
        print('Podałeś złe parametry')
    else:
        L = []
        while start <= stop:
            L.append(start)
            start += krok
    i = 0
    print('| {:>6}'.format('C') + '  |  ' + '{:>7s} |'.format('K'))
    print('|' + 20*'-' + '|')
    while (i < len(L)):
        kel = L[i] + 273.15
        print('| {:>+6.2f}'.format(L[i]) + '  |  ' + '{:>+6.2f} |'.format(kel))
        # print('|%+8.1f|%-8.2f|' % (L[i], kel))
        i += 1

frange(-5,5,0.5)
# print(frange(-10,20,0.5))

def generator():
    L = []
    i = 0
    while (i < 1000):
        L.append(randint(0,100))
        i += 1
    return L

def cutting(treshold, L):
    Big = []
    for v in L:
        if (v >= treshold):
            Big.append(v)
    return Big, len(Big)


print(cutting(99, generator()))
print(cutting(95, generator()))

def lustrzana(liczba):
    x = str(liczba)
    i = 0
    while (i < (len(x) / 2)):
        if(x[i] == x[len(x) - 1 - i]):
            i += 1
            flag = 'lustrzana'
        else:
            flag = 'nie jest lustrzana'
            break
    print(flag)

def mirror(liczba):
    liczba = str(liczba)
    # odwracanie napisu
    if (liczba == liczba[::-1]):
        print('ok')
    else:
        print('not ok')

def mirror_rev(liczba):
    liczba = list(str(liczba))
    liczba_old = liczba
    liczba.reverse()
    # odwracanie napisu
    if (liczba_old == liczba):
        print('ok')
    else:
        print('not ok')

lustrzana(1223221)
mirror(1223221)
mirror_rev(1223221)

