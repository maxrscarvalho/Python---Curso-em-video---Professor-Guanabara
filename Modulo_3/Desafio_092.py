'''
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho 
e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente de Zero
o dicionario recebera tambem o ano de contratacao e o salario. Calcule e acrescente, alem 
da idade quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35)- datetime.now().year)

print('-='*35)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')