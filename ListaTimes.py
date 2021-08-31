times = ('Corinthians', 'Palmeairas', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-Pr', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atlético-GO')
print('-=' *15)
print(f'Lista de times: {times}')
print('-=' *15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' *15)
print(f'os 4 ultimos colocados são {times[-4:]}')
print('-=' *15)
print(f'Times em aordem alfabetica {sorted(times)}')
print('-=' *15)
print(f'a posição da chapecoense é {times.index("Chapecoense")+1}')