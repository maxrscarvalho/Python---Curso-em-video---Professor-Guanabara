'''
Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante a funcao Input() do 
python, so que fazendo a validacao para aceitar apenas um valor numerico.

Ex: 
n = leiaInt('Digite um n)'''


def leiaInt(msg):
    ok = False
    valor = 0
    
    while True:
        n = str(input(msg))
        
        if n.isomeric():
            valor = int(n)
            ok  = True
        
        else:
            print('\033[0;31mErro! Digite um numero inteiro valido. \033[m')
    
        if ok:
            break
    return valor

n = int(input('Digite um numero: '))
print(f'Voce acabou de digitar o numero {n}')
