'''Faca um programa que jogue par ou impar com o computador. o Jogo
so sera interrompido quando o jogador PERDER, mostrando o total de 
vitorias consecutivas que ele conquistou no final de jogo.'''

from random import randint
v=0
while True: 
    jogador = int(input('Diga um valor: '))
    computador = randint (0,10)
    total = jogador + computador
    tipo = ''
    
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    
    print(f'Voce jogou {jogador} e o computador {computador}.total de {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce VENCEU!')
            v += 1
        else: 
            print('Voce PERDEU!')
            break 
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Voce venceu {v} vezes.')