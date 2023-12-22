# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()  # 23 caracteres com espaço e 21 sem espaço
nome_separado = nome.split()

print(f'Nome em Maiusculo: {nome.upper()}')
print(f'Nome em Minusculo: {nome.lower()}')
print(f'O nome possui {len(nome) - nome.count(" ")} Letras')
print(f'O primeiro nome possui {len(nome_separado[0])} letras')
#print(nome.find(' ')) Esse tambem funciona