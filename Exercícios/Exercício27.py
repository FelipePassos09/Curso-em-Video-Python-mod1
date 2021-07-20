# -- Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nomes dela, separadamente.

nome = str(input('Diga seu nome completo: '))
nome_lista = nome.split()


print('Seu primeiro nome é {}'.format((nome_lista[0])))
print('Seu último nome é {}'.format((nome_lista[-1])))
