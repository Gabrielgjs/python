valores = list()
for c in range(0,5):
    n = int(input('Digite um valor : '))
    valores.append(n)
    r = str(input('Quer continuar [S/N] ?'))
    if r in 'Nn':
        break
print(f'você digitou {len(valores)} elementos ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')