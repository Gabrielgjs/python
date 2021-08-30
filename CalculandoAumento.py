#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual é o salario do funcionario? R$'))
aumento = sal * 0.15
novo =  sal + aumento
aumento = novo * 0.15
proxaumento = novo + aumento
print(f'Um funcionário que ganhava {sal}, com 15% de aumento, passa a receber {novo:.2f} e no proximo ano o salário será {proxaumento}')
