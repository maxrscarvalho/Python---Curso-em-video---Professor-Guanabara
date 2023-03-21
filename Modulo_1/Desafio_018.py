# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.



import math
an = float(input('Digite o angulo que vc deseja: '))
sen = math.sin(math.radians(an))
print('O angulo de {} tem o SENO de {:.2f}'. format(an,sen))
co = math.cos(math.radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'. format(an,co))
tang = math.tan(math.radians(an))
print('O angulo de {} tem o TANGENTE de {:.2f}'. format(an,tang))

