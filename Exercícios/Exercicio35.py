# -- Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem formar um triângulo.

l1 = float(input('Diga o tamanho de uma reta: '))
l2 = float(input('Diga o tamanho de ourta reta: '))
l3 = float(input('Diga o tamanho da terceira reta: '))

print('-='*20)

if ((l3 + l1) > l2) and ((l2 + l3) > l1) and ((l1 + l2) > l3):
    print('Com essas retas conseguimos criar um triângulo.')
else:
    print ('Não conseguimos formar um triangulo.')