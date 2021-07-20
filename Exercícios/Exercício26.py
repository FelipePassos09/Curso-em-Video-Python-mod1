# -- Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra 'A'.
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

frase = str(input('Diga alguma coisa: '))
fr_2 = frase.upper()
print('A frase tem {} caracteres.'.format(len(fr_2)))
print('A letra A aparece {} vezes na frase.'.format(fr_2.count('A')))
print('Na frase a letra A aparece primeiro na {} posição.'.format(fr_2.find('A', 0, )+1))
print('Na frase a letra A aparece por último na {} posição.'.format(fr_2.find('A', -1)+1))
