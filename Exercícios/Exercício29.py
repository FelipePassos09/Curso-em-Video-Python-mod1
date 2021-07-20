# -- Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$ 7,00 para cada Km acima do limite.

vel = int(input('Qual foi a velocidade do veículo? '))
if vel > 80:
    print('Você foi multado.')
    print('O valor da multa será: R$ {:.2f}'.format((vel - 80)*7))
else:
    print('Ok, está tudo certo com ele.')
    
print('___FIM___')
