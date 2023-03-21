'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos numeros
[ 5 ] sair do programa

Seu programa devera realizar a operacao solicitada em cada caso.'''



n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

opcao = 0
while opcao != 5:

    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')

    opcao = int(input('Qual e a sua opcao? '))

    if opcao == 1:
        soma = n1 + n2
        print('O resultado da soma foi {}'.format(soma))

    elif opcao == 2:
        multiplicar = n1 * n2
        print('O resultado da multiplicação foi {}'.format(multiplicar))
    
    elif opcao == 3:
        if n1 > n2:
            print('O numero {} e maior que {}'.format(n1, n2))
        else:
            print('O numero {} e maior que {}'.format(n2, n1))
    
    elif opcao == 4:
        print('informe os numeros novamente')
        n1 = int(input('Digite novamente o primeiro numero: '))
        n2 = int(input('Digite novamente o segundo numero: '))
    
    elif opcao == 5:
        print('Finalizando')

    else:
        print('Opcao invalida tente novamente')