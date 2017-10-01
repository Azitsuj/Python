# -*- coding: utf-8 -*-

from random import randint

class Compare:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'

    def __add__(self, other):
        return '[' + str(self.x + other.x) + ',' + str(self.y + other.y) + ']'
    
    def __sub__(self, other):
        return '[' + str(self.x - other.x) + ',' + str(self.y - other.y) + ']'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return (pow(pow(self.x, 2) + pow(self.y, 2), 1/2) > pow(pow(other.x, 2) + pow(other.y, 2), 1/2))
    
    def __neg__(self):
        return '[' + str(-self.x) + ',' + str(-self.y) + ']'
        # return -self.x, -self.y
    
p1 = Compare(13, 5)
print(p1)

p2 = Compare(3, 4)
print(p2)
print(p1 + p2)
print(p1 - p2)
print(p2 - p1)
print(p1==p2)
print(p1>p2)
print(p2>p1)
print(p2>p2)
print(-p1)

# P75 BMI zawodnika

class Zawodnik:
    
    L = []    
    
    def __init__(self, wzrost, waga):
        self.wzrost = wzrost
        self.waga = waga
        
    def bmi(self):
        bmi = round(self.waga / pow(self.wzrost / 100, 2), 2)
        self.L.append(bmi)
        return bmi
    
    def sort(self, L):
        L = sorted(L)
        print('L posortowane: ' + str(L))

z1 = Zawodnik(165, 100)
print('BMI: ' + str(z1.bmi()))
z2 = Zawodnik(135, 102)
print('BMI: ' + str(z2.bmi()))
z3 = Zawodnik(195, 123)
print('BMI: ' + str(z3.bmi()))
print(z3.L)
z3.sort(z3.L)

class ZawodnikTest:
    
    def __init__(self):
        self.L = []
        z1 = Zawodnik(165, 100)
        print('BMI: ' + str(z1.bmi()))
        self.L.append(z1.bmi())
        z2 = Zawodnik(135, 70)
        print('BMI: ' + str(z2.bmi()))
        self.L.append(z2.bmi())
        z3 = Zawodnik(195, 123)
        print('BMI: ' + str(z3.bmi()))
        self.L.append(z3.bmi())
    '''
    # może być sort taki:
    def sort(self, L):
        L = sorted(L)
        print(L)
    '''
    def sort(self):
        self.L = sorted(self.L)
        print(self.L)
    
zt = ZawodnikTest()
# w przypadku sort 1:
# zt.sort(zt.L)
zt.sort()

class Lotto:
    
    def __init__(self):
        self.L = set()
        while len(self.L) < 6:
            i = randint(1, 49)
            # print(i)
            self.L.add(i)
        print(self.L)
        self.sort()
    
    def sort(self):
        Ls = sorted(self.L)
        return Ls

los = Lotto()
# print(los.sort())

class LottoTest:
    
    def __init__(self):
        self.T = set()
        losowanie = Lotto()
        M = losowanie.sort()
        self.Wygrana = losowanie.sort()
        while(True):
            liczba = int(input('Podaj liczbę: '))
            if (liczba >= 1 and liczba <= 49 and liczba not in self.T):
                self.T.add(liczba)
            else:
                print('Błędna liczba!')
            if len(self.T) == 6:
                break
        # print(self.T)
                
        Trafienia = self.T & set(self.Wygrana)
        print(self.Wygrana)
        self.T = sorted(self.T)
        print('-' * 59)
        print('| ' + '{:<20}'.format('Wylosowane liczby: ') + '| ', end = '')
        for i in self.Wygrana:
            print('{:>3}'.format(i), end = ' | ')
        # print('\n')
        # print('{:<20}'.format('Wybrane liczby: ') + str(self.T))
        print('\n' + '| ' + '{:<20}'.format('Wybrane liczby: '), end = '')
        print('| ', end = '')
        for i in self.T:
            print('{:>3}'.format(i), end = ' | ')
        print('-' * 59, end = '')
        print('\n| Trafiłeś: ' + str(len(Trafienia)) + 45 * ' ' + '|')
        print('-' * 59)
        
test = LottoTest()