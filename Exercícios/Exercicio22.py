# -- Crie um programa que leia o nome completo de uma pessoa e mostre:
#-- O nome com todas as letras maiúsculas.
#-- O nome com todas minúsculas.
#-- Quantas letras ao todo ele tem (sem considerar os espaços).
#-- Quantas letras tem o primeiro nome.

nome = str(input('Diga seu nome completo: ')).strip()
nm = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas fica {}'.format(nome.upper()))
print('Seu nome em minúsculas fica {}'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(len(nm[0])))
# -- Ou: print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))