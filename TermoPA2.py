print('Gerador de PA ')
print('='*40)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ', end='')
        print('-> ' if cont < 10 else '', end='')
        termo += r
        cont += 1
    print(' PAUSA', end='')
    mais = int(input('Quantos termos você quer mostras a mais? '))
print(f'Progressão finalizada com {total} termos mostrados ')
