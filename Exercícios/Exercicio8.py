# -- Escreva um programa que leia um valor de metros e o exiba convertido em centimetros e milimetros.

mt = float(input('Quantos metros quer converter? '))
cent = (mt * 100)
mil = (mt * 1000)

print('{} metros são {} centímetros.'.format(mt, cent))
print('{} metros são {} milimetros.'.format(mt, mil))

