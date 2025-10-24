'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. 
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

def mostrarLinha():
    print(10*'---')

def mensagem(msg):
    print(10*'---')
    print({msg})
    print(10*'---')

def soma(a, b):
    s = a + b
    print(f'Soma de A + B = {s}')

def contador(*num):
    print(num, end=' ')
    print('FIM')

mostrarLinha()

mensagem('Sistema de Alunos')

soma(2, 3)
soma(a=2, b=3)

contador(5, 7, 1)
contador(4, 9, 1, 5, 3)
contador(7, 9, 5, 8, 4, 7, 3, 9)