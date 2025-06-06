#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostra:
#a) Quantas pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) uma listagem com as pessoas mais leves.
#OBS: 100kg ou mais pesado, menos é leve.

def cadastro_peso():
    base_nome = []
    base_peso = []
    base_nome.append(nome)
    base_peso.append(peso)

    while True:
        nome_pessoa = input('Informe o nome:')
        peso_pessoa = int(input('Informe o peso: '))
        if nome_pessoa == "sair":
            break

    for nome in base_nome
