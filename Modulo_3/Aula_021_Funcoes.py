'''Interactive help'''

# print('Ola, mundo')
# help(print)

# print(input.__doc__)

'''Docstrings'''

# from time import sleep

# def contador(i, f, p):
#     """Faz uma contagem e mostra na tela.
#     ;param i: _Inicio da contagem_
#     ;param f: _fim da contagem_
#     ;return: _sem retorno_
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#         sleep(0.3) 
#     print('Fim')

# contador(2, 10, 2)
# help(contador)

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma {s}')

# somar(b=4, c=2)

'''Escopo de Variaveis '''

# def teste():
#     print(f'Na funcao teste, n vale {n}')
#     print(f'Na funcao teste, n vale {x}')3

# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, n vale {x}')

# def teste(b):
#     b += 4
#     c = 2
#     a = 8
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')

# n1 = 2

'''Exemplo '''

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n}  e igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2} e {f3}')

'''Exemplo '''

# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# num = int(input('Digite um numero: '))
# if par(num):
#     print('E par!')
# else:
#     print('Nao e par!')