from datetime  import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    print(f'Essa pessoa tem {idade} anos')
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'ao todo tivemos {totmenor} pessoas menores de idade')