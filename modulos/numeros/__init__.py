from mundo_3.ex108 import valor_moeda


def aumentar10(valor_moeda_def):
    '''
    -- Recebe o valor e retorna o valor com mais 10%
    :return: sim
    '''
    return valor_moeda_def * 1.10

def diminui10(valor_moeda_def):
    '''
    Recebe o valor e retorna o valor com menos 10%
    :return: sim
    '''
    return valor_moeda_def * 0.9

def dobro(valor_moeda_def):
    '''
    Recebe o valor e retorna o valor com 2x
    :return: sim
    '''
    return valor_moeda_def * 2

def triplo(n):
    '''
    Recebe o valor e retorna o valor com 3
    :return: sim
    '''
    return n * 3

def metade(valor_moeda_def):
    '''
    Recebe o valor e retorna o valor com metade
    :return: sim
    '''
    return valor_moeda_def / 2

def fatorial(n):
    '''
    recebe o valor e retorna o valor fatorial
    :return: sim
    '''
    f=1
    for c in range(1, n+1):
        f *= c
    return f

def formatoMoeda(valor_moeda_def, moeda='R$'):
    return f'{moeda}{valor_moeda_def}:.2f'.replace('.',',')
