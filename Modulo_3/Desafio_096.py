'''
Faca um programa que tenha uma funcao chamada area(), que receba as dimensoes de um terreno 
retangular (largura e comprimento) e mostre a area do terreno. '''


def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} X {comp} e de {a} m2')

print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)