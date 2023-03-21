'''A confederacao Nacional de natacao precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade:

- Ate 9 anos: Mirim
- Ate 14 anos: Infantil
- Ate 19 anos: Junior
- Ate 20 anos: Senior
- Acima: Master'''

from datetime import date
ano_atual = date.today().year
ano_nasc_usuario = int(input('Digite sua o ano que vc nasceu: '))
idade = ano_atual - ano_nasc_usuario
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Voce esta na Categoria Mirim')

elif idade > 9 and idade <= 14:
    print('Classificacao: Infantil')

elif idade > 14 and idade <= 19:
    print('Classificacao: Junior')

elif idade > 19 and idade <= 20:
    print('Classificacao: Senior')

elif idade > 20: 
    print('Classificacao: Master')