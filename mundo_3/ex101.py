# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime

def voto(ano_nasci):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasci

    if idade <= 15:
        print(f'Com {idade} anos o voto é NEGADO!')
    elif idade in (16, 17,) or idade >= 70:
        print(f'Com {idade} anos o voto é OPICIONAL')
    else:
        print(f'Com {idade} anos o voto é OBRIGATORIO')

nascimento = int(input('Informe seu ano de nascimento: '))

voto(nascimento)