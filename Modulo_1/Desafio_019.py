# Um profesor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo no nome do escolhido.

import random
nome_1 = str(input('Digite o primeiro nome: '))
nome_2 = str(input('Digite o segundo nome: '))
nome_3 = str(input('Digite o terceiro nome: '))
nome_4 = str(input('Digite o quarto nome: '))
lista = (nome_1, nome_2, nome_3, nome_4)
escolhido = random.choice(lista)
print ('O nome selecionado aleatoriamente foi: {} '.format(escolhido))