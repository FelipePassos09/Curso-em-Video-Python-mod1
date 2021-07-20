# -- Crie um programa que leia a largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la.
# considerando que cada litro de tinta cubra uma área de 2m².

largura = float(input('Diga a largura, em metros, da parede: '))
altura = float(input('Diga a altura, em metros, da parede: '))
area = (altura*largura)
rend = (area/2)

print('Para uma superficie de {:.1f} m de altura e {:.1f} m de largura a área estimada é {:.2f} m².'.format(altura, largura, area))
print('Para pintar a sua parede você vai precisar de {:.1f} litros de tinta.'.format(rend))

print('Isso é tudo por enquanto.\n--------------')