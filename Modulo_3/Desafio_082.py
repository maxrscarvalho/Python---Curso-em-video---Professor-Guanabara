'''Crie um programa que vai ler varios numeros e colocar em uma lista.

DEpois disso crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados, respectivamente.

Ao final, mostre o conteudo das tres listas geradas.'''

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um numero: ')))
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break 
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa e {lista}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}')




