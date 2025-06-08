#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostra:
#a) Quantas pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) uma listagem com as pessoas mais leves.
#OBS: 100kg ou mais pesado, menos é leve.

base_nome_peso = {}

while True:
    print('Para finalizar digite "sair"')
    nome_pessoa = input('Informe o nome: ').title()
    if nome_pessoa == "S":
        break
    peso_pessoa = float(input('Informe o peso: '))

    base_nome_peso[nome_pessoa] = peso_pessoa

print(f'\nForam cadastradas {len(base_nome_peso)} pessoas:')
print(f'Pessoas com mais de 100kg:')
for cadastro in base_nome_peso: #Pessoas mais pesadas
    if base_nome_peso.get(cadastro) >= 100:
        print(f'{cadastro} - {base_nome_peso.get(cadastro)}Kg')
print(f'\nPessoas com menos de 100kg:')
for cadastro in base_nome_peso:  # Pessoas menos pesadas
    if base_nome_peso.get(cadastro) < 100:
        print(f'{cadastro} - {base_nome_peso.get(cadastro)}Kg')