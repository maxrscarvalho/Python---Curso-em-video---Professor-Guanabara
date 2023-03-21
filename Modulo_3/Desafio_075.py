'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os 
em uma tupla, No final mostre: 

A) Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.'''


num = (int(input('Digite o primeiro numero: ')),
        int(input('Digite o segundo numero: ')),
        int(input('Digite o terceiro numero: ')),
        int(input('Digite o quarto numero: ')))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}° posicao ')
else:
    print('O valor 3 nao foi digitado em nenhuma vez!')

for n in num: 
    if n % 2 == 0:
        print(n, end='')
