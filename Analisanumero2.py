'''num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 %  10
c = num // 100 % 10
m = num // 1000 % 10
print (f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'cetena: {c}')
print(f'Milhar: {m}')'''

num = int(input('informe um número: '))
print(f'analisando o número {num}')
print(f'Unidade: {num // 1 % 10}')
print(f'dezena: {num // 10 % 10}')
print(f'centena: {num // 100 % 10 }')
print(f'milhar: {num // 1000 % 10}')