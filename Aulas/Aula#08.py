# -- Aula#08 - Utilizando módulos.

from math import sqrt, ceil, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
