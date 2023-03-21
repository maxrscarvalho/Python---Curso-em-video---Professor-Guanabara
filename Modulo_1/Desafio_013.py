# Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
salario_funcionario = float(input('Digite o seu salario R$: '))
novo_salario = (salario_funcionario * 0.15) + salario_funcionario
print('O seu novo salario sera de R$: {:.2f}'.format(novo_salario))