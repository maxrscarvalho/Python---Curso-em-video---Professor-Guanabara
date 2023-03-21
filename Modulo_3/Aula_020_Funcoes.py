'''Exemplo 1'''


# def mostralinha():
#     print('---------------------------')

# mostralinha()
# print('Ola como vai vc ?')
# mostralinha()
# print('Cadastro de Funcionarios')
# mostralinha()

'''Exemplo 2 '''

# def lin():
#     print('-'*30)

# print('Ola mundo')
# lin()
# print('Vamos aprender Python')
# lin()
# print('Como vc esta hoje ?')

'''Exemplo 3'''

# def mensagem(msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)

# mensagem('Sistema de Alunos')
# mensagem('Sistema Unitario')

# '''Exemplo 4'''

# def titulo(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)

# titulo(' Curso em video ')
# titulo(' Python e muito bom') 
# titulo('OI') 

'''Exemplo 5'''

# def soma(a, b):
#     print(f'A = {a} ')
#     s = a + b
#     print(s)

# soma(4, 5)
# soma(8, 9)
# soma(2, 1)
# soma(4, 0)


'''Exemplo 6'''

# def contador(* num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e sao ao todo {tam} numeros.')

# contador(2, 1, 7)
# contador (8, 0)
# contador(4, 4, 7, 6, 2)


'''Exemplo 7'''


# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] += 2
#         pos += 1


# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)


'''Exemplo 8'''

# def soma(* valores):
#     s = 0 
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}')

# soma(5, 2)
# soma(2, 9, 4)