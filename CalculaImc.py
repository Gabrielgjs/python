peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura ? (m)'))
imc = peso / (altura * altura)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Seu IMC está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu IMC está ideal !')
elif 25 <= imc <= 30:
    print('Seu IMC está um pouco acima, indicando Sobrepeso')
elif 30 <= imc <= 40:
    print('Seu imc está acima do ideal, você esta com obesidade')
else:
    print('Você está com Obesidade Mórbida')