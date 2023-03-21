'''Crie uma tupla que tenha uma tupla unica com os nomes dos produtos e seus 
respectivos precos, na sequencia. 

No final, mostre uma listagem de precos, organizando os dados em forma de tabular.  '''



listagem = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"Listagem de Preco":^40}')
print('-'*40)

for pos in range(0, len(listagem)): 
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')