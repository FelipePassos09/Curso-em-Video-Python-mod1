# -- Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

nmr = int(input('Diga um número: '))

if nmr % 2 == 0:
    print('O número {} é par!'.format(nmr))
else:
    print('Shi, o número é impar.')
print('___FIM___')