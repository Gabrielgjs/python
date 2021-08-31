numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado, não vou adicionar')
    r = str(input('Quer continuar [S/N]')).strip()
    if r in 'Nn':
        break
print(f'Os valores são {sorted(numeros)}')