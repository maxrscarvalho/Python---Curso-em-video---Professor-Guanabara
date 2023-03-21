'''Crie um programa que leia duas notas de um aluno e calcule
sua media, mostrando uma mensagem no final, de acordo com sua media atingida

- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO 
- Media 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 5:
    print('A media foi {}, voce foi REPROVADO!'.format(media))

elif media <= 6.9:
    print('Sua media foi {}, voce esta em RECUPERACAO!'.format(media))

else: 
    print('sua media foi {}, Parabens voce foi APROVADO!'.format(media))
    print('Ola como vc esta ?')
    