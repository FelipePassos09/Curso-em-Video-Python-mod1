# -- Um professor quer sortear um dos seus quatrp alunos para apagar o quadro.
# -- Faça um programa que leia o nome deles e escreva o nome do escolhido.

import random

al_1 = str(input('Diga no nome do primeiro aluno: '))
al_2 = str(input('Diga o nome do segundo: '))
al_3 = str(input('DIga o nome do terceiro: '))
al_4 = str(input('Agora o quarto: '))
alunos = [al_1, al_2, al_3, al_4]
sorteio = (random.choice(alunos))
print('O escolhido foi {}!'.format(sorteio))

