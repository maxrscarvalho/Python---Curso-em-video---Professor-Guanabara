'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate acertar . Mostrando no final quantos palpites foram necessarios para vencer.'''

from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
print('Sera que voce consegue adivinhar qual foi? ')

print('Processando...')
sleep(5)

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual e o seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True 

    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        
        elif jogador > computador:
            print('menos...Tente mais uma vez')

print('Parabens voce acertou com {} tentativas '.format(palpites))



