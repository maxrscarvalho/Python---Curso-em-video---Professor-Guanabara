'''Desenvolva um programa que leia o comprimento de tres retas e diga
ao usuario se elas podem ou nao formar um triangulo.'''

print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)

a = int(input('Digite o comprimento da reta 1: '))
b = int(input('Digite o comprimento da reta 2: '))
c = int(input('Digite o comprimento da reta 3: '))

if (a+b > c) or (a+c > b) or (b+c > a): 
    print('E possivel formar um triangulo')

else: 
    print('Nao e possivel formar um triangulo')

