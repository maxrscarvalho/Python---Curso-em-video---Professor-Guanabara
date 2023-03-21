'''Faca umm programa que leia 5 valores numericos e guarde-os em uma lista.

No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.'''

'''Minha resolucao'''

# numeros = [ int(input('Digite o primeiro numero: ')),
#             int(input('Digite o segundo numero: ')),
#             int(input('Digite o terceiro numero: ')),
#             int(input('Digite o quarto numero: ')),
#             int(input('Digite o quinto numero: '))]

# for n in enumerate(numeros):
#     print(f'{n} ', end='')

# print(f'\n O maior valor digitado foi {max(numeros)} na posicao {n}')
# print(f' \n O menor valor digitado foi {min(numeros)} na posicao {n}')            # O {min} escolhe o menor numero

'''Resolucao Professor'''

lista_numeros = []
maior = 0
menor = 0 
for c in range (0,5):
    lista_numeros.append(int(input(f'Digite um valor para a posicao {c}: ')))

    if c == 0:
        maior = menor = lista_numeros[c]
    else:
        if lista_numeros[c] > maior:
            maior = lista_numeros[c]
            
        if lista_numeros[c] < menor:
            menor = lista_numeros[c]

print('-=-'*20)
print(f'Voce digitou os valores {lista_numeros}')
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')

for i, v in enumerate(lista_numeros):
    
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')

for i, v in enumerate(lista_numeros):
    if v == menor: 
        print(f'{i}...', end='')
print()
