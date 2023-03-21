'''Faca um programa que leia o ano de um nascimento de um jovem e informe 
de acordo com sua idade

- Se ele ainda vai se alistar ao servico militar
- Se e a hora de se alistar 
- Se ja passou do tempo de alistamento.

Seu programa tambem devera mostrar o tempo que falta ou que passou o prazo.'''

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite sua o ano que vc nasceu: '))
idade = ano_atual - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano_atual))

if idade == 18:
    print('Voce tem que se alistar imediatamente!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento sera em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


