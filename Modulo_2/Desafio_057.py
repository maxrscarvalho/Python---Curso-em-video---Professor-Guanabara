'''Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores "M" ou "F".
caso esteja errado , peca a digitacao novamente ate ter um valor correto.'''


sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))


