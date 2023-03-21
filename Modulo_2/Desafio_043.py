'''DEsenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu 
status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida'''

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = (peso / altura**2)
print('O IMC dessa pessoa e {:.2f}'.format(imc))

if imc <= 18.5: 
    print('Voce esta abaixo do peso')

elif imc > 18.5 and imc <= 25:
    print('Voce esta no peso ideal')

elif imc > 25 and imc <= 30:
    print('Voce esta com sobrepeso')

elif imc > 30 and imc <= 40:
    print('Voce esta com obesidade')

else: 
    print('Voce esta com Obesidade Morbida')