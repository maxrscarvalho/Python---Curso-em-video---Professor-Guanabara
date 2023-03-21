# Faca um programa que leia uma frase pelo teclado  e mostre:

# Quantas vezes aparece a letra "A"
# Em que posicao ela aparece pela primeira vez.
# Em que posicao ela aparece pela ultima  vez.

frase = input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira Letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima Letra A apareceu na posicao {}'.format(frase.rfind('A')+1))
