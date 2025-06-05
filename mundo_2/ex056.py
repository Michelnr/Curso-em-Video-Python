# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# - a media de idade.
# - qual o nome do homem mais velho
# - quantas mulheres têm menos de 20 anos
soma_idade = 0
homem_maior_idade = 0
homem_maior_idade_nome = ''
mulher_menor_idade = 0
quant_mulher_nova = 0

for cadastro in range(1,5):
    print(f'========== Informe o {cadastro}° cadastro ==========')
    nome = str(input('Informe o nome: ')).strip().upper()
    idade = int(input('Informe a idade: '))
    sexo = str(input('informe o sexo [M/F]')).strip().upper()
    soma_idade += idade
    if cadastro == 1 and sexo in 'M':
        homem_maior_idade = idade
        homem_maior_idade_nome = nome
    if homem_maior_idade < idade and sexo in 'M':
        homem_maior_idade = idade
        homem_maior_idade_nome = nome
    if idade < 20 and sexo in 'F':
        quant_mulher_nova += 1

print(f'A media da idade é {soma_idade/4}\n'
      f'O nome do homem mais velho é {homem_maior_idade_nome} e a idade é {homem_maior_idade}\n'
      f'Temos {quant_mulher_nova} mulheres menores de 20 anos')

