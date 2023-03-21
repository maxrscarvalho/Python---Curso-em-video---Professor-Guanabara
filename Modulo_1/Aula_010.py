'''Exemplo de uso de comando IF / Else'''
# if carro.esquerda():
#     bloco True
# else:
#     bloco False

# tempo = int(input('Quantos anos vc tem seu carro?')) #todo comando alinhado a esquerda sera executado sempre
# if tempo <=3:                                        #todo comando alinhado a direita (Dentro) sera executado ou nao depende da situacao
#     print('Carro Novo')
# else:
#     print('Carro Velho')
# print('--FIM--')

'''condicao  simplificada'''

# tempo = int(input('Quantos anos vc tem seu carro?'))
# print('Carro Novo' if tempo <=3 else 'Carro velho')
# print('--FIM--')

'''Exemplo 1'''

# nome = str(input('Qual e o seu nome? '))
# if nome == 'Max':
#     print('Que nome lindo vc tem!')
# else:
#     print('Seu nome e tao normal!')
# print('Bom dia, {}'.format(nome))

'''Exemplo 2'''

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2)/2
# print('A sua media foi {:.2f}'.format(m))
# if m >= 6.0:
#     print('A sua media foi boa! Parabens!')
# else:
#     print('Sua media foi ruim! Estude mais!')

'''Exemplo 3'''

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2)/2
# print('A sua media foi {:.1f}'.format(m))
# print('Parabens' if m >= 6 else 'Estude mais!')
