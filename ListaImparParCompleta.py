valores = list()
listaimpar = list()
listapar = list()
while True:
    valores.append(int(input('Digite um valor : ')))
    r = str(input('Quer continuar [S/N] ?'))
    if r in 'Nn':
        break
for c in valores:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista completa é {valores}')
print(f'A lista ímpar é {listaimpar}')
print(f'A lista par é {listapar}')