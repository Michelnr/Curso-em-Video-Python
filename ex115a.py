# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
# arquivo de texto simples.
# O sistema só vai ter 2 opções:
# 1 - Cadastrar novas pessoas
# 2 - Listar todas as pessoas

from modulos.ex115.formatação import texto

def menu():
    while True:
        texto('MENU PRINCIPAL')
        print('1 - Cadastre uma pessoa')
        print('2 - Listar pessoas')
        print('3 - Sair do sistema')

        escolha_menu = int(input('Qual a sua escolha? '))
        if escolha_menu not in [1,2,3]:
            print('Informe apenas os números do menu')
            continue

        if escolha_menu == 1:
            texto('OPÇÃO 1 - Cadastrar pessoa')
            cadastrar()
        elif escolha_menu == 2:
            texto('OPÇÃO 2 - Listar pessoas')
        else:
            texto('Saindo do sistema ... Até logo')
            break

menu()