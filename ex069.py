# Crie um programa que leia a idade e o sexo de varias pessoas.
# A cada  pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não  continuar.
#
# No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

sexom = idade18 = idade20 = 0

while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? (M/F) ')).strip().upper()[0]
    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        sexom += 1
    if idade < 20 and sexo == 'F':
        idade20 += 1
    menu = str(input('Quer continuar? (S/N) ')).strip().upper()
    if menu == 'N':
        break
print(f'Pessoas com mais de 18 anos: {idade18}\n'
      f'Quantidade de Homens cadastrados: {sexom}\n'
      f'Quantidade de mulheres com menos de 20 anos: {idade20}')
