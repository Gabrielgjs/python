v1 = input('Primeiro valor: ')
v2 = input('segundo valor: ')
v3 = input('terceiro valor: ')
'''if v1 > v2:
    print(f'o maior valor foi {v1}')
elif v2 > v3:
    print(f'O maior valor foi {v2}')
else:
    print(f'o maior valor foi {v3}')
if v1 < v2:
    print(f'O menor valor foi {v1}')
elif v2 < v3:
    print(f'O menor valor foi {v2}')
else:
    print(f'O menor valor foi {v3}')'''

menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v1 and v3<v2:
    menor = v3
maior = v1
if v2>v1 and v2>v3:
    maior=v2
if v3>v1 and v3>v2:
    maior=v3
print(f'O maior número vaior {maior}')
print(f'O menor número foi {menor}')




