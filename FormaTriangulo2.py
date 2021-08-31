print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triangulos')
    if r1 == r2 == r3:
        print('É um triângulo EQUILATERO.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('É um triângulo ISOSCELES')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('É um triângulo ESCALENO')

else:
    print('os segmentos acima não podem formar triangulos')
