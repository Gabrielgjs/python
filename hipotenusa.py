'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
calc = (co**2 + ca**2) **(1/2)
print(f'a hipotenusa vai medir {calc:.2f}')'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
calc = hypot(co, ca)
print(f'a hipotenusa vai medir {calc:.2f}')