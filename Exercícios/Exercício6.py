# -- Crie um algoritmo que leia um número e mostre o seu dobro, triplo, quadrado e raiz quadrada.

num = int(input('Diga um número: '))

print(' O dobro de {} é {}. \n O triplo de {} é {}. \n O quadrado de {} é {}. \n E a raiz quadrada de {} é {:.2f}.'.format(num, num*2, num, num*3, num, num**2, num, num**(1/2)))
print('Isso é tudo por enquanto. \n -----')
