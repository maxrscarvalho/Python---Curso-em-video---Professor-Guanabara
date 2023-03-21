'''Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor e maior 
- O segundo valor e maior 
- Nao existe valor maior, os dois sao iguais'''

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o primeiro numero: '))

if num1 > num2: 
    print('O numero {}, e maior que o numero {}'. format(num1, num2))

elif num2 > num1:
    print('O numero {}, e maior que o numero {}'.format(num2, num1))

else: 
    print('Nao existe valor maior, os dois sao iguais')