# teste = list()
# teste.append('Max')
# teste.append(30)
# galera = list()
# galera.append(teste[:])
# teste[0]= 'Maria'
# teste[1]= 22
# galera.append(teste[:])
# print(galera)


'''Exemplo 2'''

# galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

'''Exemplo 3'''

galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera: 
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} e menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')