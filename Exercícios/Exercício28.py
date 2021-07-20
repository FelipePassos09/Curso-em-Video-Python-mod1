# -- Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário para
# o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O computador deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print('-=|' *20)
print('VAMOS BRINCAR!!!')
print('-=|' *20)
chose = int(input('Estou pensando em um número entre 0 e 5, tente adivinhar: '))
print('TÁ OK, \n\nPROCESSANDO...')
sleep(3)

if chose == random.randint(0,5):
    print('\nÉ isso aí, estou pensando em {}.\n'.format(chose))
else:
    print('\nErrou, tente novamente mais tarde.\n')
print(('-=-'*2),'FIM', ('-=-'*2))