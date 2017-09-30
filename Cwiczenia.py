# 4
'''
L = ''
imie = input('Podaj imie: ')
L + imie
nazwisko = input('Podaj nazwisko: ')
L + nazwisko

print(L)
'''

# 6 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
'''
dane = input('Podaj sekwencje liczb: ')
list = dane.split(',')
print(list)
'''

# 7 Write a Python program to accept a filename from the user and print the extension of that.
# file = input('Enter file name with extension: ')
file = 'asasa.asas.exe'
i = file.rfind('.')
print(i)
print(file[i:])

# 8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], end = ' ')
print(color_list[3])

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = input('Podaj integer: ')
n1 = int(n)
n2 = int(n+n)
n3 = int(3*n)
print(n1 + n2 + n3)