'''Crie um programa que faca o computador jogar Jokenpo com voce.'''

from random import randint
from time import sleep 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opcoes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('qual e a sua jogada? '))

print ('JO')
sleep(2)

print ('KEN')
sleep(2)

print('PO')
sleep(2)

print('-='*10)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*10)

if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Joagdor Vence')

    elif jogador == 2:
        print('Jogada Invalida')

elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print('Computador Vence')

    elif jogador ==1:
        print('Empate')

    elif jogador ==2:
        print('Jogador Vence')

    else: 
        print('Jogada Invalida')

elif computador == 2: # Computador jogou Tesoura
    if jogador ==0:
        print('Jogador Vence')

    elif jogador ==1:
        print('Computador Vence')

    elif jogador ==2:
        print('Empate')

    else:
        print('Jogada Invalida')