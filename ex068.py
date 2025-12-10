# Faça um programa que jogue par ou impar com o computador.
# o jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou  no final do jogo.
from random import randrange
cont = 0

while True:
    compu = randrange(0, 10)
    jogador_escolha = str(input('Escolha Par ou Impar? (P/I) ')).upper().strip()
    jogador_numero = int(input('Escolha seu numero de 0 a 10: '))
    par_impar = (jogador_numero + compu) % 2

    if 'P' in jogador_escolha and par_impar == 0:
        cont += 1
        print(f'GANHOU, o numero é {compu + jogador_numero}\n'
              'Vamos jogar novamente!')
    elif 'I' in jogador_escolha and par_impar == 1:
        cont += 1
        print(f'GANHOU, o numero é {compu + jogador_numero}!\n'
              'Vamos jogar novamente!')
    else:
        print(f'PERDEU, o numero é {compu + jogador_numero}')
        break
print(f'Você ganhou {cont} vezes!')
