# -- Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Qual o preço total do produto? '))
desconto = (preco * (5 / 100))

print('O preço de R$ {:.2f} terá um desconto de 5%, no caso R$ {:.2f}'.format(preco, desconto))
print('O preço com o desconto será R$ {:.2f}'.format(preco - desconto))
