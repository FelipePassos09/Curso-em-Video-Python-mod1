# -- Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# -- Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input('Diga o nome do primeiro aluno: '))
n2 = str(input('Diga o nome do segundo aluno: '))
n3 = str(input('Diga o nome do terceiro aluno: '))
n4 = str(input('Diga o nome do quarto aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)

print('A ordem de apresentação será: ')
print(alunos)
