'''F' String - While Interrupcao ]'''


# while True: # Repeticao para sempre

# ''''n = cont = 0
# while n != 999:
#      n = int(input('Digite um numero: '))'''

# n = s = 0


'''Exemplo 2'''

# cont = 1 
# while cont <=  10:
#     print(cont, '', end='')
#     cont += 1
# print('Acabou')

# n = cont = 0 
# while cont < 5:
#     n = int(input('Digite um numero: '))
#     cont += 1
#     break

n = s = 0 
while True: 
    n = int(input('Digite um numero: '))
    if n == 999: 
        break
    s += n
print(f'A soma vale {s}')