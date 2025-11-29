# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.
def voto(ano_nasci):
    from datetime import date
    '''
    -> Recebe o ano de nascimento e calcula a idade junto
    com o ano atual para saber a idade e informa as 
    seguintes possibilidades    
    :NEGADO: 15 anos ou menos não votam
    :OPICIONAL: 16 anos, 17 anos e a partir dos 70 anos
    :OBRIGATORIO: entre 18 anos e 69 o voto é obrigatorio
    '''
    ano_atual = date.today().year
    idade = ano_atual - ano_nasci
    print(15*'=-=' + f'\n')
    if idade <= 15:
        print(f'Com {idade} anos o voto é NEGADO!')
    elif idade in (16, 17,) or idade >= 70:
        print(f'Com {idade} anos o voto é OPICIONAL')
    else:
        print(f'Com {idade} anos o voto é OBRIGATORIO')
    print(f'\n' + 15*'=-=')

# programa principal
nascimento = int(input('Informe seu ano de nascimento: '))
voto(nascimento)