#Faça um programa que leia o ano e diga se ele é um ano bissexto
from datetime import date

print('0 = Ano atual')
ano = int(input(f'Qual o ano deseja verificar? '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é Bissexto!')
else:
    print(f'Ano {ano} não é Bissexto!')