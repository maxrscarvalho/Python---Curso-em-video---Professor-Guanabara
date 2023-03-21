'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
da casa, o salario do comprador e em quantos anos ele vai pagar.

calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.'''
casa = (float(input('Digite o valor da casa R$: ')))
salario = (float(input('Digite o seu salario R$: ')))
anos = (int(input('Digite em quantos anos sera o financiamento: ')))
prest_mensal = casa / (anos * 12)
minimo = salario * 0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos))
print('A prestacao da sua casa sera de R$ {:.2f}'.format(prest_mensal))

if prest_mensal > minimo:
    print('O emprestimo foi NEGADO!')

else:
    print('O emprestimo foi APROVADO!')