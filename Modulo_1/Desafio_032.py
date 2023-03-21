'''Faca um programa que leia um ano qualquer e mostre se ele e BISSEXTO.'''

from datetime import date
ano = int(input('Qual ano voce quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e Bissexto'.format(ano))

else:
    print('O ano {} NAO e um ano Bissexto'.format(ano))
