#--Aula 6 - Tipos Primitivos--


# exercicio 1
variavel1 = int(input('Diga um número'))
variavel2 = int(input('Diga outro número'))
soma = variavel1 + variavel2
print('A soma vale', soma)

# print('A soma entre' , variavel1 , 'e' , variavel2 , 'vale' , soma , '.')

print('A soma entre {} e {} vale {}.'.format(variavel1, variavel2, soma))

# exercicio 2

n = input('Digite um valor: ')
print(n.isnumeric())