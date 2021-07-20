# -- Escreva um programa que pergunte a quantiadde de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# -- Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e 0.15 por Km rodado.

diarias = int(input('Quantas diárias o veículo ficou alugado? '))
km = float(input('Ao ser entregue, quantos Kilometros foram rodados? '))

val_diarias = (diarias * 60.00)
val_km = (km * 0.15)

print('-' * 12)
print('O valor referente á locação foi R$ {:.2f}.'.format(val_diarias))
print('-' * 12)
print('O valor referente á kilometragem foi R$ {:.2f}.'.format(val_km))
print('-' * 12)
print('O valor total total a pagar é R$ {:.2f}.'.format(val_diarias + val_km))
print('-' * 12)
print('Isso é tudo por enquanto.')