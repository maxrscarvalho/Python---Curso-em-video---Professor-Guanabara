'''
Faca um programa que tenha uma funcao chamada contador(), que receba tres parametros:
inicio, fim e passo e realize a contagem.

Seu programa tem que realizar tres contagens atraves da funcao criada:

A) De 1 ate 10, de 1 em 1
B) De 10 ate 0, de 2 em 2
C) Uma contagem personaliada'''

from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if p < 0:
       p *= -1
       
    if p == 0:
       p = 1

    if i < f:
      cont = i
      while cont <= f:
          print(f'{cont} ', end='')
          sleep(0.5)
          cont += p
      print('Fim!')
    else:
       cont = i
       while cont >= f:
          print(f'{cont} ', end='')
          sleep(0.5)
          cont -= p
       print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora e sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passe: '))
contador(ini, fim, pas)