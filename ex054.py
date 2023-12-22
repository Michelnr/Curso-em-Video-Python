# crie um programa que leia o ano de nascimento de sete pessoas. no final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# (Considere maior idade 21 anos)
from datetime import date

ano_atual = date.today().year
idade_menor = 0
idade_maior = 0

for pessoas in range(1,8):
    ano_nasci = int(input(f'Informe o ano de nascimento da {pessoas}° pessoa: '))
    if ano_atual-ano_nasci >= 21:
        idade_maior += 1
    else:
        idade_menor += 1

print(f'São {idade_maior} pessoas maiores de idade\n'
      f'São {idade_menor} pessoas menores de idade')
