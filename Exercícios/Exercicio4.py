# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possiveis sobre ele:

valor = input('Digite alguma coisa: ')

print('veja se acertei: ')
print('{} é do tipo: {}'.format(valor, type(valor)))
print('{} é um número? {}'.format(valor, valor.isnumeric()))
print('{} é somente texto? {}'.format(valor, valor.isalpha()))
print('{} é somente em caixa alta? {}'.format(valor, valor.isupper()))
print('{} é todo em minúsculas? {}'.format(valor, valor.islower()))
print('{} é alfanumérico? {}'.format(valor, valor.isalnum()))
print('{} possui casas decimais? {}'.format(valor, valor.isdecimal()))
print('{} começa com maiúscula? {} '.format(valor, valor.istitle()))
print('{} é imprimivel? {} '.format(valor, valor.isprintable()))
print("  ")
print('Isso é tudo por enquanto.')
