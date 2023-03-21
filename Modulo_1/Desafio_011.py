# Faca um programa que leia a largura e a altura de um parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2 m2.
largura = float(input('Digite a largura da sua parede em metros: '))
altura = float(input('Digite a altura da sua parede em metros: '))
area = largura * altura
litros_de_tintas = area / 2
print('Sua parede tem a dimensao de {} x {} e sua area e de {}'.format(largura, altura, area))
print('Para pintar completamente a sua parede vc precisara de {:.2f} litros de tintas'.format(litros_de_tintas))
