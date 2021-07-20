# -- Crie um programa que leia o nome de uam cidade e diga se ela começa com a palavra 'SANTO'.

city = str(input('Diga o nome da sua cidade: '))

cidade = city.upper()

if ('SANTO' in cidade) == True:
    print('Existe a palavra SANTO no nome da cidade.')
else:
    print('Não há a palavra SANTO no nome da cidade.')

city_1 = cidade.split()

if city_1[0] == 'SANTO':
    print('O nome da cidade começa com SANTO')
else:
    print('O nome da cidade não começa com SANTO')
