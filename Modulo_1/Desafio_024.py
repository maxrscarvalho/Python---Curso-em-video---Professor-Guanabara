# crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO"
# print(cidade.find('Santo'))

cidade = str(input('Em que cidade vc nasceu: ').strip())
print(cidade[:5].upper == 'Santo')