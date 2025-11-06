'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo.

Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 por 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep

def contagem():
    cont = 1
    print('=-='*10)
    print('Contagem de 1 a 10 de 1 em 1')
    while cont <= 10:
        sleep(0.5)
        print(cont, end=' ', flush=True)
        cont += 1
    print('Fim')
    
    cont = 10
    print('=-='*10)
    print('Contagem de 10 a 0 de 2 em 2')
    while cont >= 0:
        sleep(0.5)
        print(cont, end=' ', flush=True)
        cont -= 2
    print('Fim')
    print('=-='*10)

    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Informe o inicio: '))
    fim = int(input('Informe o fim: '))
    passo = int(input('Informe o passo: '))
    # caso passo seja igual a 0
    if passo == 0:
        passo = 1
    print('=-=' * 10)
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')

    # Contagem progressiva (+)
    if inicio < fim:
        while inicio < fim+1:
            sleep(0.5)
            print(inicio, end=' ', flush=True)
            inicio += passo
        print('Fim')

    # Contagem regressiva (-)
    elif inicio > fim:
        while inicio > fim-1:
            sleep(0.5)
            print(inicio, end=' ', flush=True)
            inicio -= passo
        print('Fim')
    print('=-=' * 10)

contagem()
