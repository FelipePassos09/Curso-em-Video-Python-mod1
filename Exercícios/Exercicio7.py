# -- Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

mat = float(input('Nota de matemática: '))
por = float(input('Nota de português: '))
média = float((mat + por) / 2)

print('A nota de português foi {} \na de matemática foi {} \ne a média foi {:.1f}'.format(por, mat, média))
