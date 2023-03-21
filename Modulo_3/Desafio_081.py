'''Crie um programa que vai ler varios numeros e colocar em uma lista.

depois disso, mostre: 

A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou nao na lista.'''


# lista = []
# while True:

#     lista.append(int(input('Digite um valor: ')))
#     opcao = str(input('Deseja continuar [S/N]: ')).upper()

#     if opcao == 'S':
#         continue

#     else:
#         if 5 in lista: 
#             print('Ha o numero "5" na lista')

#         else:
#             print('Nao ha o numero 5 na lista')
#     break
# print(f'voce digitou {len(lista)} numeros')
# lista.sort(reverse=True)
# print(f'Os valores em ordem decrescente{lista}')
        


'''Resolucao do Professor'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))         # Solicita ao usuario a digitar um numero 
    resp = str(input('Quer continuar? [S/N]: '))            # Solicita ao usuario se ele deseja continuar a digitar 

    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Voce digitou {len(valores)} elementos')             # Utilizou-se (len) para contar quantos numeros foram digitados
valores.sort(reverse=True)                                  # (reverse=True) ira organizar na forma decrescente
print(f'Os valores em ordem decrescente {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista!')



