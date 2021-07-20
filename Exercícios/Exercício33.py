# -- Faça um programa que leia tres números e mostre qual é o maior e qual é o menor.

nm1 = int(input('Diga um número: '))
nm2 = int(input('Diga outro número: '))
nm3 = int(input('Diga mais um número: '))

num = [nm1, nm2, nm3]

print('Destes números, o maior número é {}'.format(max(num)))
print('Destes números, o menor deles é {}'.format(min(num)))

print('-='*20)

# Para calcular o menor:
menor = nm1
if nm2 < nm1 and nm2 < nm3:
    menor = nm2
if nm3 < nm1 and nm3 < nm2:
    menor = nm3 

# Para calcular o maior:
maior = nm1
if nm2 > nm1 and nm2 > nm3:
    maior = nm2
if nm3 > nm1 and nm3 > nm2:
    maior = nm3
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))