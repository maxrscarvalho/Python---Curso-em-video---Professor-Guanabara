'''Refaca o Desafio 009, mostrando a tabuada de um numero que o usuario escolher
so que agora utilizando um laco FOR.'''

# num_usuario = int(input('Digite um numero para ver sua tabuada: '))
# print('-'*12)
# print('{} x {:2} = {}'.format(num_usuario, 1, num_usuario * 1))
# print('{} x {:2} = {}'.format(num_usuario, 2, num_usuario * 2))
# print('{} x {:2} = {}'.format(num_usuario, 3, num_usuario * 3))
# print('{} x {:2} = {}'.format(num_usuario, 4, num_usuario * 4))
# print('{} x {:2} = {}'.format(num_usuario, 5, num_usuario * 5))
# print('{} x {:2} = {}'.format(num_usuario, 6, num_usuario * 6))
# print('{} x {:2} = {}'.format(num_usuario, 7, num_usuario * 7))
# print('{} x {:2} = {}'.format(num_usuario, 8, num_usuario * 8))
# print('{} x {:2} = {}'.format(num_usuario, 9, num_usuario * 9))
# print('{} x {:2} = {}'.format(num_usuario, 10, num_usuario * 10))
# print('-'*12)

num_usuario = int(input('Digite um numero para ver sua tabuada: '))
for c in range (0,11):
    print('{} x {:2} = {:2}'.format(num_usuario, c, num_usuario * c))

print('Fim')