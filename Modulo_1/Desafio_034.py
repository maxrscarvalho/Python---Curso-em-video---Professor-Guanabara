'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.

Para salarios superiores a R$1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento e de 15%.'''

salario = float(input('Digite o valor do seu salario R$: '))


if salario <= 1250.00:
    novo_salario = (salario * 0.15) + salario
    print('O seu salario de R$ {:.2f} aumentara e passara a custar R$ {:.2f}'.format(salario, novo_salario))

else:
    novo_salario = (salario * 0.10) + salario
    print('O seu salario de R$ {:.2f} passara a custar R$ {:.2f}'. format(salario, novo_salario))