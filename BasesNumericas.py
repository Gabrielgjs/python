num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BÍNARIO
[ 2 ] Converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua Opção:'))
if opção == 1:
    print(f'{num} convertido para BÍNARIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAl é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida, tente novamente')


