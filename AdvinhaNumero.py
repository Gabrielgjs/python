from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
jogador = int(input('Qual seu palpite? '))
chance = 2
while jogador != computador:
    while chance >= 0:
        if computador > jogador:
            print('mais... tente mais uma vez ', end='')
            jogador = int(input('Qual seu palpite? '))
            chance -= 1
        elif computador < jogador:
            print('menos... tente mais uma vez ', end='')
            jogador = int(input('Qual seu palpite? '))
            chance -= 1
    if jogador != computador:
        print(f'Acabaram suas chances, fim de jogo! o computador jogou {computador}')
    break
if jogador == computador:
    print(f'Acertou, o computador jogou {computador}')
print(f'Fim')

'''from random import randint
computador = randint(0,10)
'print(''Sou seu computador...
'Acabei de pensar em um número entre 0 e 10.
''Sera que você consegue advinhar qual foi ?'''
'''print(computador)
palites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palites += 1
    if jogador == computador:
        acertou = True
    elif jogador > computador:
        print('menos... tente novamente', end='')
    elif jogador < computador:
        print('mais... tente novamente', end='')
print(f'Acertou! com {palites} tentativas')'''
