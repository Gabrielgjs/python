distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}km.')
if distancia <= 200:
    print(f'O preço da sua passagem será R${distancia * 0.50}')
elif distancia > 200:
    print(f'O preço da sua passagem será R${distancia * 0.45}')

#preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45