# -- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# -- Considere o dolar: US$ 1.00 == R$ 3.27


cart = float(input('Quanto você tem na carteira? '))
dolar = float(3.27)

print('Você pode comprar {:.2f} dolares com os R$ {} que tem na carteira.'.format((cart/dolar), cart))
print('Isso é tudo por enquanto.\n-----------------')