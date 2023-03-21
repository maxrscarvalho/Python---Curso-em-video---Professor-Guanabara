'''Escreva um programa que faca o computador "Pensar" em um numero inteiro entre 0 e 5 e peca 
para o usuario tentar descobrir qual foi o numero escolhido pelo computador.

O programa devera escrever na tela se o usuario venceu ou perdeu. '''

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)

jogador = int(input('Em que numero eu pensei: ')) # Jogador tenta advinhar

print('Processando...')
sleep(5)

if jogador == computador:

    print('PARABENS ! Voce conseguiu me vencer!')

else:

    print('GANHEI! Eu pensei no numero {}, e nao no {}'.format(computador, jogador))


