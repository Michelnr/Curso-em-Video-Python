# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
# os dicionários em uma lista. 
# No final, mostre: 
#   A) Quantas pessoas foram cadastradas 
#   B) A média de idade 
#   C) Uma lista com as mulheres 
#   D) Uma lista de pessoas com idade acima da média

cadastro_list = []
id_pessoa = 0
escolha = ''

while True:
    id_pessoa += 1
    cadastro_dict = {
    'Id':id_pessoa,
    'Nome':input('Informe o nome: ').title(),
    'Sexo':input('Informe o sexo: (M/F) ').upper(),
    'Idade':int(input('Informe a idade: '))
    }

    cadastro_list.append(cadastro_dict)
    
    escolha = input('deseja cadastrar outra pessoa?(S/N) ').upper()
    if escolha == 'N':
        break

#   A) Quantas pessoas foram cadastradas 
print(30*'-+-')
num_cadastro = len(cadastro_list)
print(f'Cadastro: {num_cadastro}')

#   B) A média de idade 
media_idade = 0
for pessoa in cadastro_list:
    media_idade += pessoa['Idade']
media_idade = media_idade/num_cadastro
print(f'Media de Idade: {media_idade}')

#   C) Uma lista com as mulheres 
print(30*'-+-')
print('Cadastro das mulheres:')
for pessoa in cadastro_list:
    if pessoa['Sexo'] == 'F':
        print(pessoa)

#   D) Uma lista de pessoas com idade acima da média
print(30*'-+-')
print('Pessoas com idade acima da media:')
for pessoa in cadastro_list:
    if pessoa['Idade'] > media_idade:
        print(pessoa)