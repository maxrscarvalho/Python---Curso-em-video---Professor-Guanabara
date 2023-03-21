# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro = Ana 
# Ultimo = Souza

n = input('Digite seu nome: ').strip()
nome = n.split()
print('O seu Primeiro nome e: {}'.format(nome[0]))
print('O seu Ultimo nome e: {}'.format(nome[len(nome)-1]))