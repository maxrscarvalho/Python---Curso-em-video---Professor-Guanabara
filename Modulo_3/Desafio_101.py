''' 
crie um programa que tenha uma funcao chamada votar() que vai receber
como parametro o ano de nascimento de uma pessoa, retornando um valor literal
indicado se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes.'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Nao vota!.'

    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional!.'

    else:
        return f'Com {idade} anos: Voto Obrigatorio!.'
    
nasc = int(input('Em que ano voce nasceu?: '))
print(voto(nasc))
