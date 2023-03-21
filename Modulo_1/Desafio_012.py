# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco com  5% de desconto.
preco_produto = float(input('Digite o preco do produto R$: '))
novo_preco_produto = (preco_produto * 0.05) + preco_produto
print('O novo preco do produto e R$ {:.2f}'.format(novo_preco_produto))