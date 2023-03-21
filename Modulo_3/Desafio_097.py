'''
Faca um programa que tenha uma funcao chamada de escreva(), que receba
um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel

ex: escreva('Ola, Mundo')

saida:
--------------------------
Ola, mundo
--------------------------
'''


def escreva(msg):
    tam = len(msg)
    print('-'* tam)
    print(msg)
    print('-'* tam)

escreva('Ola, mundo')
escreva('Max')
escreva('Mariana')