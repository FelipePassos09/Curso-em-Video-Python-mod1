# -- faça um programa que leia o comprimento do cateto oposto e do cateto adjacente, calcule e mostre o comprimento da hipotenusa:
# -- h² = c1² + c2²

import math

c1 = float(input('Digite o comprimento do cateto 1: '))
c2 = float(input('Digite o comprimento do cateto 2: '))
hip = math.sqrt(pow(c1,2) + pow(c2,2) )

print('Para os catetos de comprimento {:.2f} e {:.2f} a hipotenusa será {:.2f}'.format(c1, c2, hip))
print('Para os catetos de comprimento {:.2f} e {:.2f} a hipotenusa será {:.2f}'.format(c1, c2, math.hypot(c1, c2)))
