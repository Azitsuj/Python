# -*- coding: utf-8 -*-

class Bazowa:
    
    def __init__(self, imie):
        self.imie = imie
        print('Jestem w bazowej')
    
    def info123(self):
        self.a = 1
        print('Jestem w info bazowej')
    
class Potomna(Bazowa):
    # super() wywołuje inita z klasy nadrzednej
    def __init__(self, imie, nazwisko):
        super().__init__(imie)
        self.nazwisko = nazwisko
        print('Jestem w potomnej')
        print(self.imie, self.nazwisko)
    def info(self):
        super().info123()
        print('Jestem w info potomnej')
        
class PoPotomona(Potomna):
    
    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko)
        super().info()
        self.stanowisko = stanowisko
        print('Jestem w popotomnej')
        print(self.imie, self.nazwisko, self.stanowisko)
        
# pot1 = Potomona('Jan', 'Kowalski')
# pot1.info()
pot2 = PoPotomona('Jan', 'Kowalski', 'dev')
pot2.info()