# -- Escreva um programa que converta a temperatura digitada em °C para °F:
# -- Fahrenheit -> 0 = 32°
# -- Kelvin -. 0 = 273.15°
# -- C° -> F° ((9 * C)/5) + 32
# -- C° -> K° C + 273

cel = float(input('Qual temperatura em °C? '))
fahr = float ((9 * cel)/5) + 32
kelvin = float(cel + 273.15)

print('A temperatura de {:.1f} °C equivale a:\n {:.1f} °F\n {:.1f} °K'.format(cel, fahr, kelvin))
