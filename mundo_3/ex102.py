# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será
# um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opicional) Mostra ou não a conta.
    :Return: O valor do Fatorial de um número n.
    '''
    # Faz o calculo do Fatorial e mostra o mesmo caso solicitado.
    valor = num
    soma = 0
    if valor > 2:
        for passo in range(1, valor):
            if soma == 0:
                soma = valor * (valor-passo)
            else:
                soma = soma * (valor-passo)
            
        if show == True:
            print(20*'=-=')
            print(f'{valor}! -> {valor} X', end=' ')
            for p in range(1, valor):
                print(valor-p, end=' ')
                if p == 1:
                    print('X', end=' ')
            print(f'\n'+20*'=-=')


    if valor < 2:
        soma = 1
        print(20*'=-=')
        print(soma)
        print(20*'=-=')

#while True:
    #valor_calculo = 5 #int(input('informe o valor para calculo de fatorial: '))
    #menu_calculo = 'S' #input('Deseja mostrar o calculo? (S/N) ').upper().strip()
    #if len(menu_calculo) == 1 and 'S' in menu_calculo or len(menu_calculo) == 1 and 'N' in menu_calculo:
    #    if menu_calculo == 'S':
    #        mostrar_calculo = True
    #        break # This line was causing the "expected an indented block" error
    #    break

fatorial(5, True)