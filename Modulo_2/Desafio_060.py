'''Faca um programa que leia um numero qualquer e mostre o seu fatorial.

exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

# from math import factorial
n = int(input('Digite um numero: '))
# f = factorial (n)
c = n
f = 1

print('Calculando {}!'.format(n), end='')
while c > 0:
    print(' {} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))
    
    # print('O fatorial de {} e {}'.format(n,f))

