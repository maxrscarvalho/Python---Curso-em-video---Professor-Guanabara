# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira.


# Ex: Digite um numero:
# o numero  6.127 tem a parte inteira 6

# from math import trunc
# num = float(input('Digite um valor: '))
# print ('O valor digitado foi {} e a sua parte inteira e {}'.format(num, trunc(num)))

num = float(input('Digite um valor: '))
print('O valor digitado foi {}, e a sua parte inteira e {}'.format(num, int(num)))
