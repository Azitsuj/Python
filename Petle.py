# -*- coding: utf-8 -*-
from random import randint
from math import factorial
import time

losowanie = set()
iter = 1
while (len(losowanie) < 6):
    los = randint(1, 49)
    print('Nr iteracji: ' + str(iter) + ', liczba: ' + str(los))
    iter += 1
    losowanie.add(los)
else:
    print('Wylosowane liczby: ' + str(losowanie))

L = [1, 2, 3, 2, 1, 23]
i = 0
while (i < len(L)):
    print('Element ' + str(i) + ' to: ' + str(L[i]))
    i +=1

# lista dodająca inputy, wychodzi po dodaniu 'Q!'
'''
L = []
napis = ''
while (napis != 'Q!'):
    napis = input('Podaj napis do wprowadzenia: ')
    if (napis != 'Q!'):
        L.append(napis)
else:
    print(L)
'''
# alternatywnie rozwiązanie
'''
E = []
flaga = True
i = 0
while (flaga):
    elem = input('podaj ' + str(i) + '-ty element listy: ')
    # if (elem != 'q!' and elem != 'Q!'):
    if (elem.upper() != 'Q!'):
        E.append(elem)
        i += 1
    else:
        flaga = False
'''

# j = 0
# while (j < len(E)):
#    print(str(j) + '-ty element listy to: ' + str(E[j]))
#    j += 1

'''
for i, v in enumerate(E):
    if (len(E) == 1):
        print('[' + str(v) + ']')    
    elif (i == 0):
        print('[' + str(v), end=', ')    
    elif (i == len(E) - 1):
        print(str(v) + ']')
    else:
        print(str(v) + ',', end=' ')
'''

romanCov = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
for klucz in romanCov:
    print(klucz, romanCov[klucz])

zbior = set([1, 2, 3, 4, 'a', 'b'])
for z in zbior:
    print(z)
LZ = list(zbior)
print(LZ)
for v in LZ:
    print(v)
    
# for v in range(-10, 21, 1):
#    print(v, end = ' ')

# formatowanie liczb
temp = range(-10, 20, 1)
for v in temp:
    print('|temp: %+04i |temp^2: %-6i |temp*0.33: %-+4.2f' % (v, v **2, v*0.33))

liczby = range(101)
for x in liczby:
    if x % 3 != 0:
        continue
    if x == 99:
        print(x)
        continue
    print(x, end=' ')

for x in range(101):
    if x == 13:
        print(x)
        break
    print(x, end=' ')

"""
E = []
i = 0
while (True):
    elem = input('podaj ' + str(i) + '-ty element listy: ')
    # if (elem != 'q!' and elem != 'Q!'):
    if (elem.upper() != 'Q!'):
        E.append(elem)
        i += 1
    else:
#        while(True):
#            dec = input('na pewno? (t/n)')
#            if (dec.upper() == 'T'):
        break
for i, v in enumerate(E):
    if (len(E) == 1):
        print('[' + str(v) + ']')    
    elif (i == 0):
        print('[' + str(v), end=', ')    
    elif (i == len(E) - 1):
        print(str(v) + ']')
    else:
        print(str(v) + ',', end=' ')
"""

# P57
"""
sklep_prod = {"0x123":"mysz Logitgech", "0x124":"monitor HP 15\"", "0011":"Klawiatura Logitech"}
sklep_cena = {"0x123":100.50, "0x124":1500, "0011":250.15}
sklep_stan = {"0x123":15, "0x124":10, "0011":7}
zamowienie = []
suma = 0
while(True):
    print("Produkty:")
    for x in sklep_prod:
        print(('%6s | %-15s') % (x, sklep_prod[x]))

    choice = input('Podaj kod produktu: (Q) - wyjście')
    if (choice in sklep_prod.keys()):
        ilosc = int(input('Podaj ilość: '))
        if(ilosc > sklep_stan[choice]):
            print('Brak towaru na stanie')
        else:
            zamowienie.append(str(sklep_prod[choice]) + " " + str(ilosc) + " " + str(sklep_cena[choice] * ilosc))
            # zamowienie.append("%15s, %2i, %6.2f" % (sklep_prod[choice], ilosc, sklep_cena[choice] * ilosc))
            suma += sklep_cena[choice] * ilosc
            sklep_stan[choice] -= ilosc
    elif(choice.upper() == 'Q'):
        break
    else:
        print("Nie ma takiego produktu na liście!")
print("Do zapłaty: %6.2f zł" % (suma))
print(zamowienie)
for v in zamowienie:
    print(v)
"""

L1 = [1, 1, 3, 7, 15]
L2 = [1, 1, 2, 3, 4]
Z1 = set(L1)
Z2 = set(L2)
Z3 = Z1 & Z2
print(list(Z3))

L = []
for x in range(20):
    L.append(x)
print(L)

# losowanie totolotka
'''
start_time = time.time()
losowanie = set()
wybrane = set()
ilosc = input('Podaj ilość liczb: ')
while (len(wybrane) < int(ilosc)):
    los = randint(1, 50)
    wybrane.add(los)
print('Wybrane liczby to: ' + str(wybrane))
iter = 0
rekord = 0
while (len(losowanie) < len(wybrane)):
    los = randint(1, 50)
    if los in wybrane:
        # print('Nr iteracji: ' + str(iter) + ', liczba: ' + str(los))
        iter += 1
        losowanie.add(los)
        if len(losowanie) > rekord:
            rekord = len(losowanie)
    else:
        iter += 1
        losowanie = set()
    if iter % 100000 == 0:
        n = (iter / 100000) * 0.1
        # print('Iteracja %02.1f' % n + 'mln w toku, minęło czasu: %3.2f sekund' % (time.time() - start_time))
        print('Iteracja ' + '{:>4.1f}'.format(n) + ' mln w toku, minęło czasu: ' + '{:>8.3f}'.format(time.time() - start_time) + ' sekund, najwięcej trafionych liczb: ' + str(rekord))
        rekord = 0
else:
    print('Liczba iteracji wyniosla: %9d' % (iter))
    print('Wylosowane liczby: ' + str(losowanie))
    print("-- %s seconds --" % (time.time() - start_time))
'''
'''
b = int(input('Podaj z ilu liczb: '))
p = (factorial(b)/(factorial(a)*factorial(b-a)))
print(p)
'''
lotto = (factorial(50)/(factorial(5)*factorial(50-5)))
print('{:>10.0f}'.format(lotto))