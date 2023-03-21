# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere 
# US$ 1.00 = R$ 3.27
dinheiro_carteira = float(input('Quanto vc tem na sua carteira: '))

print('Voce tem US$ {:.2f}, em sua carteira!'.format(dinheiro_carteira / 3.27))
