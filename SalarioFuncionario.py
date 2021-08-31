salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 0.10
aumento1 = salario * 0.15
if salario <= 1250:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+aumento1:.2f} agora')
else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+aumento:.2f} agora')


'''if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)'''