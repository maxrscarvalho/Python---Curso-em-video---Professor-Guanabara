'''Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele 
foi multado.

A multa vai custar R$ 7.00 por cada km acima do limite.'''

vel_carro = float(input('Digite a velocidade alcancada: '))

if vel_carro > 80:
    multa = (vel_carro - 80) * 7.00
    print('MULTADO, Voce excedeu o limite de 80km/h')
    print('Voce foi multado no valor de R$ {:.2f}'.format(multa))

else:

    print('Tenha um bom dia, dirija com seguranca!')