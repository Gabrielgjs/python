from datetime import date
anoatual = date.today().year
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = anoatual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} Não é bissexto')