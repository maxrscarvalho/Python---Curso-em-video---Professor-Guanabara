'''
Faca um programa que leia nome e media de um aluno, guardando
tambem a situacao em um dicionario. No final mostre o conteudo 
da estrutura na tela.  '''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f' - {k} e igual a {v}')

print('-='*30)
print(aluno)