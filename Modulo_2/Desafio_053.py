'''Crie um programa que leia uma frase qualquer e diga se ela e um polidromo
descosiderando os espacos.

ex: Apos a sopa.
a sacada da casa 
A torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''


text = str(input('Digite uma frase: ')).strip().upper()
palavras = text.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
print('O inverso de {} e {}'.format(junto, inverso))

'''for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]'''

if  inverso == junto:
    print('Temos um palindromo!')

else: 
    print('A frase digitada nao e um palindromo!')



