# Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade:
#
# -Se ele ainda vai se alistar ao serviço militar
# -Se é a hora de se alistar
# -se já passou do tempo de alistamento
#
# Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date

ano_nasci = int(input('Qual seu ano de nascimento? '))

idade = date.today().year-ano_nasci

if idade < 18:
    print(f'Ainda tem {idade} anos e faltam {18-idade} anos para o alistamento militar.')
elif idade > 18:
    print(f'Já tem {idade} anos e já se passaram {idade-18} anos do alistamento militar.')
else:
    print(f'Ele tem {idade} anos e está na época do alistamento militar.')
