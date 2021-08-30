dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
calcd = dias*60
calckm = km*0.15
valor = calcd + calckm
#pago (dias * 60) + (km * 0.15)
print(f'O total a pagar é de {valor:.2f}')
