# -- Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

multi = int(input('Insira o número que deseja multiplicar: '))

# -- Solução com operação simples.

print('Usando cálculo simples:\n\nA tabuada de {} é:'.format(multi))
print('{:2} x {:2} = {:2}'.format(1, multi, (1*multi)))
print('{:2} x {:2} = {:2}'.format(2, multi, (2*multi)))
print('{:2} x {:2} = {:2}'.format(3, multi, (3*multi)))
print('{:2} x {:2} = {:2}'.format(4, multi, (4*multi)))
print('{:2} x {:2} = {:2}'.format(5, multi, (5*multi)))
print('{:2} x {:2} = {:2}'.format(6, multi, (6*multi)))
print('{:2} x {:2} = {:2}'.format(7, multi, (7*multi)))
print('{:2} x {:2} = {:2}'.format(8, multi, (8*multi)))
print('{:2} x {:2} = {:2}'.format(9, multi, (9*multi)))
print('{:2} x {:2} = {:2}'.format(10, multi, (10*multi)))

print('')


# -- Solução com listas e range.

inicio = int(input("Diga de onde quer começar a calcular: "))
fim = int(input("Diga quando quer parar de calcular: "))
passo = 1

multiplos = list(range(inicio,fim,passo))

print('Usando listas:\n\nA tabuada de {} é:'.format(multi))
for item in multiplos:
    result = (item * multi)
    print('{} vezes {} é {}'.format(item, multi, result))

print('Isso é tudo por enquanto.\n----------------')

