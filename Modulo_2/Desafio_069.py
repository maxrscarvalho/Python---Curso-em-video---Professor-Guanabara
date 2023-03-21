'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa
devera perguntar se o usuario quer ou nao continuar . No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantos mulheres tem menos de 20 anos.'''

while True: 
    idade = int(input('Idade: '))
    sexo = ' '
    
    maior_idade = total_homens = total_mulheres = 0
    while sexo not in 'Mf':
        sexo = str(input('sexo [M/F]: ')).strip().upper()[0]
       
        if idade >= 18:
            maior_idade += 1

        if sexo == 'M':
            total_homens += 1

        if sexo == 'F' and idade <= 20:
            total_mulheres += 1

    resp = ' '
    while resp not in 'Sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper() 
    if resp == 'N':
        break      

print(f'O total de pessoas com mais de 18 anos: {maior_idade}')
print(f'O total de homens {total_homens} cadastrados')
print(f'Total de mulheres com menos de 20 {total_mulheres} cadastrados')