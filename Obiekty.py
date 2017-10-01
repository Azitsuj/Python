# -*- coding: utf-8 -*-

class Testowa:
    # __init__ to konstruktor
    def __init__(self, zmienna1, zmienna2):
        # self oznacza, że zmienna jest globalna
        print('jestem w konstruktorze')
        self.zmienna1 = zmienna1
        self.zmienna2 = zmienna2
        self.info()
        
    def info(self):
        print('jestem w info')
        print(self.zmienna1, self.zmienna2)
    
    # __str__ metoda określa co ma być pokazane w metodzie 'print' dla obiektu    
    def __str__(self):
        return str(self.zmienna1) + ', ' + str(self.zmienna2)

o1 = Testowa(12, 10)
o2 = Testowa(1, 2)
print(o1)

# Tworzymy klasę Pracownik, która będzie przechowywać kolejnych pracowników z inputa, a po wyjściu z inputa poda tych pracowników
class Pracownik:
   
    def __init__(self, imie = "Adam", nazwisko = "Kowalski", stanowisko = "Tester", pensja = 100):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja
    
    def __str__(self):
        return 'Imię : ' + self.imie + ', Nazwisko: ' + self.nazwisko + ', Stanowisko: ' + self.stanowisko + ', Pensja: ' + str(self.pensja)
    
    def info(self, L):
        print('-'* 58)
        print('| {:^10s}'.format('Imię') + ' | {:^15s}'.format('Nazwisko') + ' | {:^10s}'.format('Stanowisko') + ' | {:^10s}'.format('Pensja') + ' |')
        print('-'* 58)
        for v in L:
            print('| {:<10s}'.format(v.imie) + ' | {:<15s}'.format(v.nazwisko) + ' | {:<10s}'.format(v.stanowisko) + ' | {:>10.2f}'.format(v.pensja) + ' |')
        print('-'* 58)
        
L = []
while (True):
    imie = input("Podaj imie pracownika ('q' aby wyjść): ")
    if(imie == 'q'):
        break       
    nazwisko = input("Podaj nazwisko pracownika ('q' aby wyjść): ")
    if(nazwisko == 'q'):
        break       
    stanowisko = input("Podaj stanowisko pracownika ('q' aby wyjść): ")
    if(stanowisko == 'q'):
        break
    elif(stanowisko == ''):
        stanowisko = "Stażysta"
    pensja_tmp = input("Podaj pensje pracownika (0 aby wyjść): ")
    if(pensja_tmp == 0):
        break       
    elif(pensja_tmp == ''):
        pensja = 1000
    else:
        pensja = float(pensja_tmp)
     
    a = Pracownik(imie, nazwisko, stanowisko, pensja)
    print(a)
    L.append(a)

b = Pracownik()
L.append(b)
# b = Pracownik()
# L.append(b)
print(L)
a.info(L)
# for v in L:
#    print(v)