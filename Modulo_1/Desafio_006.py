# Crie u algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um numero: '))

print('O dobro do numero digitado e {}, o triplo {}, \n a raiz quadrada {}'.format(numero*2, numero*3, pow(numero,(1/2))))