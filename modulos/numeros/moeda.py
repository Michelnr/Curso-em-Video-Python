def aumentar10(valor_moeda_def, porcentagem, formato=False):
    '''
    Recebe o valor e retorna o valor com mais 10%
    :return: sim
    '''
    resultado = valor_moeda_def + (valor_moeda_def * (porcentagem/100))

    return resultado if formato is False else formatoMoeda(resultado)

def diminui10(valor_moeda_def, porcentagem, formato=False):
    '''
    Recebe o valor e retorna o valor com menos 10%
    :return: sim
    '''
    multiplicador = 1 - (porcentagem / 100)
    resultado = valor_moeda_def * multiplicador
    
    return resultado if formato is False else formatoMoeda(resultado)

def dobro(valor_moeda_def, formato=False):
    '''
    Recebe o valor e retorna o valor com 2x
    :return: sim
    '''
    resultado = valor_moeda_def * 2

    return resultado if formato is False else formatoMoeda(resultado)

def triplo(n, formato=False):
    '''
    Recebe o valor e retorna o valor com 3
    :return: sim
    '''
    resultado = n * 3

    return resultado if formato is False else formatoMoeda(resultado)

def metade(valor_moeda_def, formato=False):
    '''
    Recebe o valor e retorna o valor com metade
    :return: sim
    '''

    resultado = valor_moeda_def / 2

    return  resultado if formato is False else formatoMoeda(resultado)

def formatoMoeda(valor_moeda_def, moeda='R$'):
    return f'{moeda}{valor_moeda_def:.2f}'.replace('.',',')
