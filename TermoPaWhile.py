print('Gerador de PA ')
print('='*40)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
while cont <= 10:
    print(f'{termo} ', end='')
    print('-> ' if cont < 10 else 'Pausa', end='')
    termo += r
    cont += 1
print('FIM')