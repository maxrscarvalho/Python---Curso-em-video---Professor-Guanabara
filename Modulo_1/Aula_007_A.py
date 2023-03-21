# ordem de procedencia 
#  1 - ()
#  2 - **
#  3 - * / // %
#  4 - +  -
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {}, a multiplicao e {}, e a divisao e {:.3f}'.format(s, m, d))
print('A divisao inteira e {} e a exponenciacao e {}'.format(di, e))

