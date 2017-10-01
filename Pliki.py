# -*- coding: utf-8 -*-
import os
import fnmatch
from time import ctime, strftime, gmtime
import time

file = open('test.txt', 'w')
# w jakim trybie plik jest otwarty:
print(file.mode)

# czy plik jest zamknięty:
print(file.closed)

# jaki plik
print(file.name)

file.write('Jerzy, Kowalski, Pracownik\n')
file.write('Adam, Nowak, Student\n')
file.write('Henryk, Wielki, Specjalista')
file.close()

file_o = open('test.txt', 'r+')
print(file_o.read())
print(file_o.tell())
# file_o.seek(-1, 2)
print(file_o.tell())
file_o.close()

file_a = open('test.txt', 'a')
file_a.write('\n\nNowa linia tekstu')
# print(file_a.read())
file_a.close()

print(os.getcwd())
print(os.listdir())

for i in os.listdir():
    p = fnmatch.fnmatch(i, 'P*[ei].py')
    # print(fnmatch.fnmatch(i, '*.txt'))
    if p:
        print(i)

# os.mkdir('Nowy')
print(os.getcwd())
os.chdir('Nowy')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())


class FileOperations:
    
    def __init__(self, path):
        self.path = path
        while (True):
            # aby program działał, trzeba odkomentować linię poniżej i usunąć pytanie = 3
            # pytanie = int(input('Co chcesz zrobić? 1 - Dodaj studenta, 2 - Pokaż listę, 3 - Wyjście: '))
            pytanie = 3
            if (pytanie == 1):
                if (os.path.exists(path)):
                    f = open(path, 'a')
                    f.write(self.zapis())
                    f.close()
                else:
                    f = open(path, 'w')
                    f.write(self.zapis())
                    f.close()
                q = input('Wyjście (t/n)')
                if (q == 't'):
                    self.odczyt()
                    break
            elif (pytanie == 2):
                self.odczyt()
                break
            elif (pytanie == 3):
                break
            
    def zapis(self):
        imie = input('Podaj imię: ')
        nazwisko = input('Podaj nazwisko: ')
        grupa = input('Podaj grupę: ')
        return ('| {:^10s}'.format(imie) + ' | {:^15s}'.format(nazwisko) + ' | {:^3s}'.format(grupa) + ' |')
        # return imie + ', ' + nazwisko + ', ' + grupa + '\n'
    
    def odczyt(self):
        f = open(self.path, 'r')
        print(f.read())
        f.close()
        
f1 = FileOperations('lista.txt')

print('Wielkość: ' + str(os.path.getsize('test.txt')))
print(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime('test.txt'))))
class Sprawdzenie:
    
    def __init__(self):
        print(self.najstarszy())
        self.najwiekszy()
    
    def najstarszy(self):
        min_time_pom = time.time()
        print(min_time_pom)
        for i in os.listdir():
            czas = os.path.getctime(i)
            if czas < min_time_pom:
                # print(str(os.path.getmtime(i)) + ' < ' + str(min_time))
                min_time = time.strftime('%Y.%m.%d %H:%M', time.gmtime(os.path.getmtime(i)))
                min_time_pom = os.path.getctime(i)
                plik = i
        # print('Najstarszy plik to: ' + plik + ' oraz czas: ' + str(min_time))
        return min_time, plik
        
    
    def najwiekszy(self):
        dir = os.listdir(os.getcwd())
        a = 0
        for i in dir:
            if (os.path.getsize(i) > a):
                a = os.path.getsize(i)
                b = i
        print('Największy plik to: \'' +  b + '\' i ma rozmiar: ' + str(a))

print(os.getcwd())    
# katalog = Sprawdzenie(os.getcwd())

print(os.listdir())
A = Sprawdzenie()

