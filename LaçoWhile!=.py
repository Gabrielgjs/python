n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    #if n == 999:
    #   soma -= 999
    n = int(input('Digite um número [999 para parar]: '))
print(f'Voê digitou {cont} números. e a soma entre eles é {soma}')
