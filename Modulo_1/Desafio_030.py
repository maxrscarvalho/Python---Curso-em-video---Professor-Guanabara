'''Crie um programa que leia um numero inteiro e  
mostre na tela se ele e par ou impar.

r1 (amarelo)
r2 (azul)
r3 (laranja)

'''

num = int(input('Digite um numero: '))
resultado = num % 2

if resultado == 0:
    print('O numero {} e PAR'.format(num))

else: 
    print('O numero {} e IMPAR'.format(num))