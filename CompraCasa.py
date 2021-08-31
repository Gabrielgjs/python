valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos1 = int(input('Em quantos anos você irá pagar ?'))
anos = anos1*12
financiamento = valor_casa / anos
minimo = salario * 30 / 100
print(f'para pagar uma casa de {valor_casa} em {anos1} anos a prestação será de {financiamento:.2f}')
print(f'O valor do financioamento é {financiamento:.2f}')
if financiamento <= minimo:
    print('Emprestimo Concedido')
else:
    print('Emprestimo Negado')

