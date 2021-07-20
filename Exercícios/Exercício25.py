# -- Crie um programa que leia o nome de uma pessoa e diga se tem 'silva' no nome .

nome_com = str(input('Diga seu nome completo: '))
name = nome_com.lower()

print('silva' in name)