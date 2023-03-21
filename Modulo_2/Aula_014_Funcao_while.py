'''Exemplo 1'''

# for c in range(1,10): # utilizado quando sei o limite 
#     print(c)
# print('fim')

'''Exemplo com while'''  # Utilizando para o infinito quando nao sei o limite

# r = 'S'
# while r == 'S' : 
#     n = int(input('Digite um valor: '))
#     r  = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else: 
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} numeros impares!') 



