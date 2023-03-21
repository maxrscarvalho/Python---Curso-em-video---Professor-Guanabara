'''Refaca o Desafio 035 dos triangulos, acrescentando o recurso de 
mostrar que tipo de triangulo sera formado:

- Equilatero: todos os lados iguais
- Isoceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

r1 = int(input('Digite o comprimento do primeiro segmento: '))
r2 = int(input('Digite o comprimento do segundo segmento: '))
r3 = int(input('Digite o comprimento do terceiro segmento: '))

if r1<r2 + r3 and r2<r1 + r3 and r3<r1 + r2:
    print('Os segmentos acima podem formar triangulo ', end='')
    if r1 == r2 == r3: 
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles') 
else: 
    print('Os segmentos NAO PODEM formar triangulo')
