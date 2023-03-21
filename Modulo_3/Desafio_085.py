'''
Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica 
que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem
crescente.'''


numero = [[], []]                       # Cria-se duas listas dentro de uma lista.
valor = 0

for c in range(1,8):
    valor = int(input(f'Digite {c}°. numero: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

print('-=-' * 30)
numero[0].sort()
numero[1].sort()
print(f'Todos os valores sao: {numero}')
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores impares digitados foram: {numero[1]}')
