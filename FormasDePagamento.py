print('{:=^40}'.format('LOJAS GABRIEL'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    desc = preço - (preço * 10 / 100)
    print(f'O valor a vista é de {desc}')
elif opção == 2:
    desc = preço - (preço * 5 / 100)
    print(f'O valor a vista no cartão é {desc}')
elif opção == 3:
    print(f' O valor em 2x no cartão é {preço} em parcelas de {preço/2}')
elif opção == 4:
    juros = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parcela = juros / totalparc
    print(f'O valor em 3x ou mais vezes no cartão é {juros} em {totalparc} parcelas de {parcela}')