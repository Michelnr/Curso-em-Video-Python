# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opicional) Mostra ou não a conta.
    :Return: O valor do Fatorial de um número n.
    '''
    valor = num
    soma = 0
    for n in range(num-1, 0, -1):
        if soma == 0:
            soma = valor * valor-1
        else:
            soma = soma * n
        print(soma)
    

#while True:
    #valor_calculo = 5 #int(input('informe o valor para calculo de fatorial: '))
    #menu_calculo = 'S' #input('Deseja mostrar o calculo? (S/N) ').upper().strip()
    #if len(menu_calculo) == 1 and 'S' in menu_calculo or len(menu_calculo) == 1 and 'N' in menu_calculo:
    #    if menu_calculo == 'S':
    #        mostrar_calculo = True
    #        break
    #    break

fatorial(5, True)