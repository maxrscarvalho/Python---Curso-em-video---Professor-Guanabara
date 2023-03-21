'''
Faca um programa que leia nome e peso de varias pessoas,
guardando tudo em uma lista. No final moste

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.'''

temp = []
princ = []
maior = menor = 0

while True: 
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])                                   # cria uma copia 
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break 

print('-=' * 30)
print(f'Ao todo, voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')

for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')

print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')

for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
