from random import shuffle
n1 = input('digite o primeiro nome:')
n2 = input('O segundo:')
n3 = input('O terceiro:')
n4 = input('O quarto:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(' A ordem de apresentação será')
print(lista)

