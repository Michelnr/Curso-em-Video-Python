'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contagem(inicio, fim, passo):
    cont = 1
    print('=-='*10)
    print('Contagem de 1 a 10 de 1 em 1')
    while cont <= 10:
        print(cont, end=' ')
        cont += 1
    print('Fim')
    
    cont = 10
    print('=-='*10)
    print('Contagem de 10 a 0 de 2 em 2')
    while cont >= 0:
        print(cont, end=' ')
        cont -= 2
    print('Fim')
    print('=-='*10)
    
    '''# +
    if inicio < fim:
        while inicio < fim:
            print(inicio)
            inicio += passo
    # -
    elif inicio > fim:
        while inicio > fim:
            print(inicio)
            inicio -= passo
'''
contagem(10,20,1)