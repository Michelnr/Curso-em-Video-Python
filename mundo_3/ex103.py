# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficheo(jogador, gol):
    print(20*'---')
    print(f'O jogador {jogador} fez {gol} gols(s) no campeonato')
    print(20*'---')

print(20*'---')
nome_jogador = input('Nome do jogador: ').title().strip()
numero_gol = input('Número de gols marcados: ').strip()

if nome_jogador == '':
     nome_jogador = '<Desconhecido>'

if numero_gol.isnumeric():
    numero_gol = int(numero_gol)
else:
     numero_gol = 0

ficheo(nome_jogador, numero_gol)