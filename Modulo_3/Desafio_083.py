'''Crie um programa onde o usuario digite uma expressao qualquer que usa parenteses.
Seu aplicatico devera analisar se a expressao passada esta com os parenteses abertos ou fechados na ordem correta.'''

while True:
    expressao = str(input('Digite a expressao: '))
    pilha = []
    for simbolo in expressao:
        if simbolo == '(':
            pilha.append('(')
        elif simbolo == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break 
    if len(pilha) == 0:
        print('Sua expressao esta valida')
    else:
        print('Sua expressao esta errada')