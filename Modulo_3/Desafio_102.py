'''
Crie um programa que tenha uma funcao fatorial() que receba dois parametros,
o primeiro que indique o numero a calcular e o outro chamado SHow, que sera
um valor logico(opcional) indicando se sera mostrado ou nao na tela o processo 
de calculo do fatorial.'''

def fatorial(n, show=False):
    """ Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c >1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)

