print('='*40)
print('10 TERMOS DE UMA PA')
print('='*40)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' ')
print('acabou')

