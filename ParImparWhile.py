from random import randint
v = 0
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {computador}. total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você venceu')
            v +=1
        else:
            print('voce Perdeu')
            break
    print('vamos jogar novamente...')
print(f'GAMe OVER! você venceu {v} vezes')

