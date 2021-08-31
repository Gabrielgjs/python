'''numero = int(input('Me diga um número qualquer: '))
parimpar = numero % 2
if parimpar == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')'''


numero=int(input('Dê um número qualquer:  '))

if numero//2 == numero/2:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))
