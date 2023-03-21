'''Crie um programa que leia o nome de varias produtos.
O programa devera perguntar se o usuario vai continuar
No final, mostre: 

A) Qual e o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual e o nome do produto mais barato.'''

print('--'*15)
print('Supermercado Bem Barato')
print('--'*15)

total = total_mil = contador = 0
barato = ' '
while True: 
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco R$: '))
    contador += 1
    total += preco
    
    if preco > 1000:
        total_mil += 1

    if contador == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break 

print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {total_mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} custa R$ {menor}')
