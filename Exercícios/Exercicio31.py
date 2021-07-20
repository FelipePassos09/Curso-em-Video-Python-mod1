# -- Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$ 0,50 por Km para viagens até 200Km e R$ 0,45 para viagens mais longas.

print('''Olá, vai viajar? que maravilha!\n 
Sabia que dependendo da distância você paga menos?\n ''')
dis = float(input('Diga, qual a distância da sua viagem, em Km: '))

print('Legal, agora vamos ver quanto ficará sua viagem.\n...\n...\n...\n...')

if dis <= 200:
    print('Sua viagem ficará R$ {:.2f}.'.format(dis * 0.5))
else:
    print('Sua viagem ficará R$ {:.2f}.'.format(dis * 0.45))
