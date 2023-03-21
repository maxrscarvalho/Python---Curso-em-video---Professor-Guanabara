'''
Crie um programa que leia nome, sexo, idade de varias pessoas, guardando os dados 
de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas.
B) A media de idade do grupo.
C) Uma lista com todas as mulheres. 
D) Uma lista com todas as pessoas com idade acima da media. '''

pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! por favor, digite apenas "M" ou "F".')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas "S" ou "n".')
        if resp == 'N':
            break 

    print('-=-'*30)
    print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
    media = soma/len(galera)
    print(f'A media de idade e de {media:5.2f} anos.')

    for p in galera:
        if p['sexo'] in 'Ff':
            print(f'{p["nome"]} ', end='')

    print()
    print('D) Lista de pessoas que estao acima da media: ', end='')

    for p in galera:
        if p ['idade'] >= media:
            print('   ')
            for k, v in p.items():
                print(f'{k} = {v}', end=' ')
            print()
    print('<< Encerrado >>')