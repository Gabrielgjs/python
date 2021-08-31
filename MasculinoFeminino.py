'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'Mf':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')'''

sexo = ''.strip().upper()
while sexo != 'MASCULINO' and sexo != 'FEMININO':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()
print(f'Sexo {sexo.lower()} cadastrado')
print('acabou')