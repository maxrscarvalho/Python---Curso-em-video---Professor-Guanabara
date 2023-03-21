# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

km_percorridos = float(input('Digite a quantidade de km percorridos: '))
qtde_dias_usados = int(input('Digite a quantidade de dias alugado: '))
valor_total = (km_percorridos * 0.15) + (qtde_dias_usados * 60.00)
print('Vc percorreu {} KM, por {} dias, o Total a pagra e de R$: {}'.format(km_percorridos, qtde_dias_usados, valor_total))