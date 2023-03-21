# crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiusculas 
# O nome com todas as letras minusculas 
# Quantas letras ao todo sem considerar os espacos
# Quantas letras tem o primeiro nome 

nome = input('Digite seu nome completo: ')
nome_separado = nome.split()
print('Seu nome em Maiusculo e {}'.format (nome.upper()))
print('Seu nome em Minusculo e {}'.format (nome.lower()))
print('Seu nome tem ao todo {} letras'.format (len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome e {} e ele tem {} letras'.format(nome_separado [0], len(nome_separado[0])))


