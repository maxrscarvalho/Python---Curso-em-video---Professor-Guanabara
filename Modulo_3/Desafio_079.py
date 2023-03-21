'''Crie um programa onde o usuario possa ditar varios valores numericos e cadastre-os em uma lista. 
Caso o numero ja exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados, em ordem crescente.'''

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else: 
        print('Valor ja cadastrado, nao irei adicionar')

    r = str(input('Deseja continuar [S/N]: '))
    if r in 'Nn':
        break

print('-=-'*20)
numeros.sort()
print(f'Voce digitou os valores {numeros}')



    


