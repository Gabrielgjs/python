listanum = []
mai = 0
men = 0
for c in range(0, 5):
   listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
   if c == 0:
       mai = men = listanum[c]
   else:
       if listanum[c] > mai:
           mai = listanum[c]
       if listanum[c] < men:
           men = listanum[c]
print(f'O maior valor foi {mai} nas posiões ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
'''print(f'você digitou os valores {listanum}')
print(f'O maior valor foi {max(listanum)}')
print(f'O menor valor foi {min(listanum)}')
print(f'Na posição 4 temos o valor {listanum[-1]}')'''