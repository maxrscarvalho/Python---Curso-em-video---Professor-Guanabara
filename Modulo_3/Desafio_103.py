'''
Faca um programa que tenha uma funcao chamada ficha(), que receba dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou.

O programa devera ser capaz de mostrar a ficha deo jogador, mesmo que algum dado nao tenha sido 
informado corretamente.'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))

if g.isnumeric():
    g = int(g)

else: 
    g = 0

if  n.strip() == '':
    ficha(gol=g)

else:
    ficha(n, g)