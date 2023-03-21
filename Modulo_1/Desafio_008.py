# Escreva um programa que leia um valor em metros e a exiba convertida em centimetros e milimetros.
num_metros = float(input('Digite o medida em metros: '))

print('A medida digitada em metros corresponde a {:.0f} cm, {:.0f} mm'.format(num_metros*100, num_metros*1000))