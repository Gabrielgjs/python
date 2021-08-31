print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)

total = totamil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto:'))
    preço = float(input('Preço R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totamil +=1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Progama'))
print(f'o total da compra foi R${total:.2f}')
print(f'temos {totamil} produtos custando mais de mil reais ')
print(f'o produto mais barato custa R${menor:.2f}')