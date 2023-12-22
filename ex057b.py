# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça para digitar novamente ate ter um valor correto.

sexo = str(input('Informe seu sexo por favor: [M/F] ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input(f'\033[31mINFORMAÇÃO INVALIDA\033[m informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} foi registrado com \033[32msucesso\033[m!')
