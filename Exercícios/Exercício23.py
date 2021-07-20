# -- Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# - Ex. número 1834
# - Unidade: 4
# - Dezena: 3
# - Centena: 8
# - Milhar: 1

num = int(input('Diga um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Neste número a unidade é {}.'.format(u))
print('Neste número a dezena é {}.'.format(d))
print('Neste número a centena é {}.'.format(c))
print('Neste número o milhar é {}.'.format(m))