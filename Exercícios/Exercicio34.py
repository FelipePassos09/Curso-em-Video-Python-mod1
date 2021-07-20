# -- Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento será de 15%.

salario = float(input('Diga qual o salário a ser reajustado: RS '))

if salario >1250:
    print('O colaborador receberá um aumento de R$ {:.2f}, e receberá {:.2f}.'.format((salario*0.1), (salario + (salario*0.1))))
else:
    print('O colaborador receberá um aumento de R$ {:.2f}, e receberá {:.2f}.'.format((salario*0.15), (salario + (salario*0.15))))