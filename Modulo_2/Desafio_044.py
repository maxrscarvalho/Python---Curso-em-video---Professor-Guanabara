'''Elabore um programa que calcule o valor a ser pago por um produto,
cosiderando o seu preco normal e condicao de pagamento:

- A vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- Em ate 2x no cartao: preco normal 
- 3x ou mais no cartao: 20% de juros'''

print("="*20)
print("MERCADO CARVALHO")
print("="*20)
preco = float(input('Digite o valor do produto R$: '))

print('''Escolha uma das bases para conversao:
[ 1 ] - A vista dinheiro/cheque: 10% de desconto
[ 2 ] - A vista no cartao: 5% de desconto
[ 3 ] - 2x no cartao: preco normal 
[ 4 ] - 3x ou mais no cartao: 20% de juros''')

opcao = int(input('Qual e a sua opcao: '))

if opcao == 1:
    total = preco - (preco * 0.10) 

elif opcao == 2:
    total = preco - (preco * 0.05) 

elif opcao == 3: 
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em {}X de R$ {}'.format(total, parcela))

elif opcao == 4: 
    total = preco + (preco *0.20)
    total_parc = int(input('Quantas parcelas? ')) 
    parecela = total / total_parc
    print('Sua compra sera parcelada em {}X de R$ {:.2f} no final.'.format(preco, total))

print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))  
    