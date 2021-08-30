import random
from time import sleep
computador = random.randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar....')
print('-=-' * 20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if computador == numero:
    print('PARABENS! você conseguiu adivinhar!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {numero}')
