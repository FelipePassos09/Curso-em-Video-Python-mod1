# -- Operadores aritméticos --

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
exp = n1**n2

print('A soma é {}, a multiplicação {} e a divisão simples {:.3f}'.format(s, m, d,), end=' >> ')
print('A soma é {}, \na multiplicação {} \ne a divisão simples {:.3f}'.format(s, m, d,))
print('Já a divisão inteira {} \ne a potencia {}'.format(di, exp))