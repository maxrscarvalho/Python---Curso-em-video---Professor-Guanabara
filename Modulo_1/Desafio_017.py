# Faca um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

# from math import pow, sqrt
# co = int(input('Digite o comprimento do cateto oposto: '))
# ca = int(input('Digite o comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('o cateto oposto e {}, o cateto adjacente e {}, e o comprimento da hipotenusa do triangulo e {:.2f}'.format(co,ca,hi))

import math
co = int(input('Digite o comprimento do cateto oposto: '))
ca = int(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot (co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))