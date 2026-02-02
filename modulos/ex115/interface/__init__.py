from modulos.ex115.formatação import *
from modulos.ex115.cadastro import *
from modulos.ex115.listar import *

def interface():
    while True:
        texto('MENU PRINCIPAL')
        print('1 - Cadastre uma pessoa')
        print('2 - Listar pessoas')
        print('3 - Sair do sistema')

        # Opção do menu
        escolha_menu = int(input('Qual a sua escolha? '))
        if escolha_menu not in [1,2,3]:
            print('Informe apenas os números do menu')
            continue
        
        # Cadastrar pessoa
        if escolha_menu == 1: 
            cadastrar()
        # Listar pessoas
        elif escolha_menu == 2: 
            listar()
        # Sair do sistema
        else: 
            texto('Saindo do sistema ... Até logo')
            break
