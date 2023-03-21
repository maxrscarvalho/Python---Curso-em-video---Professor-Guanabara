'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao.
Mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve ser
perguntar ao usuario se ele quer ou nao continuar a digitar valores.'''

# num = cont = soma = 0
# num = int(input('Digite um numero  [999 para parar]: '))
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input('Digite um numero  [999 para parar]: '))
# print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1: 
        maior = menor = num
    else: 
        if num > maior:
            maior == num
        if num < menor:
            menor == num
    

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print('Voce digitou {} numeros e a media entre eles foi {}.'.format(soma, media))
print('O maior valor foi de {} e o menor foi {}.'.format(maior, menor))



