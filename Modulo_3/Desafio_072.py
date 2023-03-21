'''Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero ate vinte.

Seu programa devera ler um numero pelo teclado (entre 0 e 20)
e mostra-lo por extenso.'''


cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco','seis', 'sete','oito','nove', 'dez', 'onze','doze','treze','catorze','quinze', 'dezesseis', 'dezesete','dezoito','dezonove','vinte')
while True:
    escolha = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= escolha <= 20:
        break
    print('Digite novamente.', end='')
print(f'Voce digitou o numero {cont[escolha]}')
