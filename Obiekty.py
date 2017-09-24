# -*- coding: utf-8 -*-

class Testowa:
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
