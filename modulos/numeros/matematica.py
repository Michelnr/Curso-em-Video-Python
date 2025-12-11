def fatorial(n):
    '''
    recebe o valor e retorna o valor fatorial
    :return: sim
    '''
    f=1
    for c in range(1, n+1):
        f *= c
    return f