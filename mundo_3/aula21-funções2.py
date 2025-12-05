# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, 
# argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.

def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :parametro i: inicio da contagem
    :parematro f: fim a contagem
    :parametro P: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

def somar(a=0, b=0, c=0):
    '''
    -> Soma até 3 valores e mostra o resultado.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    '''
    s = a + b + c
    print(f'A soma vale {s}')

def soma_r(a=0, b=0, c=0):
    '''
    -> Soma até 3 valores e mostra o resultado.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: com retorno
    '''
    s = a + b + c
    return s

# DEF com HELP descritivo
contador(0, 10, 2)
# help(contador)

# DEF com valores opcionais
somar(3, 2, 5)
# help(somar)

# DEF com return
s1 = soma_r(3, 2, 5)
s2 = soma_r(3, 2)
s3 = soma_r(3)

print(f'Os valores são {s1}, {s2} e {s3}')
