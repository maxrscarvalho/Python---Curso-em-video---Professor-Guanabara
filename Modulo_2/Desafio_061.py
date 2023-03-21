'''Refaca o desafio 051, lendo o primeiro termos da progressao usando a estrutura while.'''

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro +  (10 - 1) * razao

for c in range (primeiro, decimo, razao):
    print('{}'.format(c), end=' ')

print('Acabou')