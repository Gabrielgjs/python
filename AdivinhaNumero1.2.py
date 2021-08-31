from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi ? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual e seu palpite : '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. tente mais umva vez.')
        elif jogador > computador:
            print('Menos.. tente mais umva vez.')
print(f'Acertou com {palpite} tentativas. parabens')