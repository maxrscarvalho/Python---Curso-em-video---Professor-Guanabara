'''
Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e somaPar().
A primeira funcao vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao vai mostrar
a soma entre todos os valores PARES sorteados pela funcao anterior.'''

from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia(numeros)
somaPar(numeros)