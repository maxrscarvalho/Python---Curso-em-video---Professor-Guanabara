'''Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequencia de fibonacci.

exemplo:
0 1 1 2 3 5 8'''


n = int(input('Digite um numero: '))
penultimo = 1
ultimo = 1

if n == 1 or n==2:
    print('1')

else:
    count = 3

while count <= 3:
    termo = ultimo + penultimo
    ultimo = termo 
    count += 1

print(termo)



