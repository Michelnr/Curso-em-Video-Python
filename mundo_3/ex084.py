#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostra:
#a) Quantas pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) uma listagem com as pessoas mais leves.
#OBS: 100kg ou mais pesado, menos é leve.
def cadastro_peso(nome, peso):
    nome = 'Joao' #input('Nome: ')
    peso = 72.0 #int(input('Peso: '))
    base_nome = []
    base_peso = []
    base_nome.append(nome)
    base_peso.append(peso)
        
while True:
    nome = input('Informe o nome:')
    peso = int(input('Informe o peso: '))
        
print(maior_peso)

print(f'Foram Cadastradas: {len(base_nome)}')