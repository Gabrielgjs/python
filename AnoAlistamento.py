from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
alistamento = 18
idade: int = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade == 18:
    print('voê tem que se alistar IMEDIATAMENTE!')
elif idade > alistamento:
    saldo = idade - alistamento
    print(f'você deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {atual - saldo}')
elif idade < alistamento:
    saldo = alistamento - idade
    print(f'Seu alistamento será em {saldo} anos')
    print(f'Seu alistamento será em {atual + saldo}')
