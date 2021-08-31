velocidade = float(input('Qaul é a velocidade atual do carro? '))
if velocidade > 80:
   print('você foi multado, excedeu o limite permitido que é 80km/h')
   multa = (velocidade - 80)  * 7
   print(f'Você deve pagar uma multa de {multa:.2f}')

print('Parábens, continue dirigindo com segurança')


