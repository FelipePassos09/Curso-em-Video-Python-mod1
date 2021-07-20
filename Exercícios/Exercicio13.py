# -- Faça um algoritmo que leia o salario de funcionario e mostre o novo salário com 15% de aumento.


salario = float(input('Diga o valor, em R$, do salárioa  ser ajustado: '))
ajuste = (salario*(15/100))

print('O reajuste do funcionário com salário de R$ {:.2f} será equivalente a R$ {:.2f}.'.format(salario,ajuste))
print('O salário reajustado será R$ {:.2f}.'.format(salario+ajuste))
