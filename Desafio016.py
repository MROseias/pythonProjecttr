import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjascente:'))
hp = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hp))



