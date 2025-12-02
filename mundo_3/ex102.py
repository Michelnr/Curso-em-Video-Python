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
            print(f'Fatorial de {valor}! -> {valor} X', end=' ')
            for p in range(1, valor):
                print(valor-p, end=' ')
                if valor-p != 1:
                    print('X', end=' ')
            print(f'= {soma}')
            print(20*'=-=')


    if valor < 2:
        print(20*'=-=')
        print(f'Fatorial de {valor}! -> 1')
        print(20*'=-=')

while True:
    valor_calculo = int(input('informe o valor para calculo de fatorial: '))
    if valor_calculo != int:
        print('Por Favor, informe um valor válido.')
        continue
    mostrar_calculo = input('Deseja mostrar o calculo? (S/N) ').upper().strip()
    if mostrar_calculo not in 'SN' or len(mostrar_calculo) > 1:
        print('Por Favor, informe uma opção válida. (S/N)')
        continue
    if mostrar_calculo == 'S':
        mostrar_calculo = True    

fatorial(valor_calculo, mostrar_calculo)