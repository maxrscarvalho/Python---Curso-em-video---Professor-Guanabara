'''Desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preco da passagem, cobrando R$ 0.50 por km para viagem de ate 200 km 
e R$ 0.45 para viagens mais longas.'''

from time import sleep
dist = float(input('Digite a distancia percorrida: '))
print('Processando...')
sleep (3)
print('Voce esta prestes a fazer uma viagem de {:.2f} km'.format(dist))

if dist <= 200:
   
    print('O valor a ser cobrado pela viagem e de R$ {:.2f}'.format(dist*0.50))

else:

    print('O valor a ser cobrado pela viagem e de R$ {:.2f}'.format(dist*0.45))