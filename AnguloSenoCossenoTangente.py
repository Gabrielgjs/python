import math
an = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print(f'O angulo de {an} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(an))
print(f'O angulo de {an} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(an))
print(f'o angulo de {an} tem a TANGENTE de {tangente:.2f} ')