n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = {n*c}')

while c <= 10:
    tabuada = n * c
    print(f'{n} x {c} = {tabuada}')
    c += 1
print('FIM')
