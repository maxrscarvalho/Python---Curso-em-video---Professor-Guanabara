'''Faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor.'''
a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

#Verificando quem e menor

menor = a
if b<a and b<c:
    menor = b
if c>a and c<b:
    menor = c

#Verificando quem e maior

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'. format(maior))


