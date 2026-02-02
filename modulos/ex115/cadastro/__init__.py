from modulos.ex115.interface import *
from modulos.ex115.formatação import *
from os import *

def cadastrar(nome=0, idade=0):
    try:
        texto('OPÇÃO 1 - Cadastrar pessoa')
        nome = str(input('Digite o nome do pessoa: '))
        if nome == 0:
            interface()
        idade = int(input('Digite a idade do pessoa: '))
        if idade == 0:
            interface()

        arquivo = open('modulos/ex115/dados.txt', 'a')
        arquivo.write(f'{nome};{idade}\n')
        arquivo.close()
    except TypeError:
        print('Informe a informação correspondente.')
        