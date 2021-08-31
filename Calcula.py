from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] soma
    [ 2 ] multiplica
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa ''')
    opção  = int(input('Qual sua opção ? '))
    if opção == 1:
        print(f' O resultado  de {n1} + {n2} é {n1+n2}')
    elif opção == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção invalida, tente novamente')
    sleep(2)
    print('=-=' *10)
print('Fim do programa ! volte sempre!')
