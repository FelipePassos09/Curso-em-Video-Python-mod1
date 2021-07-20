nome = 'Felipe'
cores = {'azul':'\033[0;36m', 
         'verde':'\033[0;32m', 
         'negativovrm':'\033[7;31m', 
         'limpa':'\033[m'}

print('{}Olá,{}{},{} é um prazer te conhecer {}!!!'.format(cores['azul'],cores['negativovrm'],nome,cores['verde'],cores['limpa']))