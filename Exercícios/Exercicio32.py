# -- Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

import calendar
from datetime import date

ano = int(input('Diga o ano que quer analisar. Caso seja o ano atual digite 0: '))


if ano == 0:
    year = int(date.today().year)
else:
    year = ano    
 
fev = calendar.monthcalendar(year, 2)

if 29 in (fev[-1]):
    print('O ano de {} é bissexto.'.format(year))
else:
    print('O ano {} não é um ano bisexto.'.format(year))