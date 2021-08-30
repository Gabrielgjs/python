'''nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiúsculas é ', nome.upper())
print('seu nome em minúsculas é ', nome.lower())
espaço = (nome.count(' '))
print(f'Seu nome tem ao todo {len(nome)-espaço} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(separa)
print(f'seu primeiro nome é {separa[0]} e elé tem {len(separa[0])} letras')
print(f'Seu segundo nome tem {len(separa[1])} letras')'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print(f'seu nome em maiúsculas é {nome.upper()}')
print(f' seu nome em minúsculas é {nome.lower()}')
print(f' seu nome tem ao todo {len(nome)-nome.count(" ")} letras')
print(f' Seu primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu segundo nome tem {len(separa[1])} letras')





