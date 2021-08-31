print('PESQUISA ESCOLA TRÂNSITO SEGURO')
contador = 0
r1 = input('Se o farol está vermelho. você pode avançar com o carro ? (sim ou não)')
if r1 == 'sim':
    print('Errou, pesquise o assunto!')
elif r1 == 'não' :
    print('Acertou, vamos para a proxima pergunta')
    contador += 1
r2 = (input('se o farol está amarelo, você deve acelerar o carro para passar ? (sim ou não)'))
if r2 == 'sim':
    print('Errou, pesquise o assunto!')
elif r2 == 'não':
    print('Acertou, vamos para a proxima pergunta')
    contador += 1
r3 = input('se o farol está verde e não há nenhum pedestre atravessando, você pode avançar ? ( sim ou não)')
if r3 == 'sim':
    print('Acertou, vamos para a proxima pergunta')
    contador += 1
elif r3 == 'não':
    print('Errou, pesquise o assunto! ')
r4 = input('se o farol está verde e há pedestre atravessando, você pode avançar ? (sim ou não)')
if r4 == 'sim':
    print('Errou, pesquise o assunto!')
elif r4 == 'não':
    print('Acertou, vamos para a proxima pergunta')
    contador += 1
r5 = input('se o farol está vermelho, você deve parar o carro ? (sim ou não)')
if r5 == 'sim':
    print('Acertou, vamos para a proxima pergunta')
    contador += 1
elif r5  == 'não':
    print('Errou, pesquise o assunto!')
if contador > 3:
    print('Parabéns! você conhece as leis de trânsito!')
print('FIM')
