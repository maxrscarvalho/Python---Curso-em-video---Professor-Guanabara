'''Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues. 

OBS: Considere que o caixa possui cedulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''


print('='* 30)
print('{:.^30}'.format('Banco DEV'))
print('=' * 30)

valor = int(input('Que valor vc quer sacar? R$ '))

total = valor 
cedula = 50
total_cedulas = 0

while True: 
    if total >= cedula:
        total -= cedula       
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cedulas de R$ {cedula}')
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total_cedulas == 0:
            break 
        
print('='* 30)
print('Volte sempre !')