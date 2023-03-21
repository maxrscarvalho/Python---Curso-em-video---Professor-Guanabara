# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nome_1 = str(input('Digite o primeiro nome: '))
nome_2 = str(input('Digite o segundo nome: '))
nome_3 = str(input('Digite o terceiro nome: '))
nome_4 = str(input('Digite o quarto nome: '))
lista = (nome_1, nome_2, nome_3, nome_4)
shuffle(lista)
print ('A sequencia aleatoria foi:')
print (lista)