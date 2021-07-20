# -- Faça um programa que leia um angulo qualquer que mostre na tela o valor do seno, cosseno e tangente.

import math

ang = float(input('Informe o angulo a ser calculado: '))
seno = math.sin(ang)
cosseno = math.cos(ang)
tangente = math.tan(ang)

print('O seno de {:.2f}° é {:.2f}.'.format(ang, seno))
print('O cosseno de {:.2f}° é {:.2f}.'.format(ang, cosseno))
print('E a tangente de {:.2f}° é {:.2f}.'.format(ang, tangente))
