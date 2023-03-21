'''
Faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar
um dicionario com as seguintes informacoes:

- A quantidade de notas
- A maior nota 
- A menor nota 
- A media da turma 
- A situacao (opcional)

Adicione tambem as docstrings da funcao.'''

def notas(*n, sit=False):
    """ Funcao para analisar notas e situacoes de varios alunos. 
        
        parametro n: uma ou mais notas dos alunos (aceita varias).
        Parametro sit: Valor opcional, indicando se deve ou nao adicionar a situacao
        Returna: Dicionario com varias informacoes sobre a situcao da Turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'

        if r['media'] >= 5:
            r['situacao'] = 'Razoavel'

        else:
            r['situacao'] = 'Ruim'

    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)