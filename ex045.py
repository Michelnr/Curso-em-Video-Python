# Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel e Tesoura) com você.
from random import choice

computador = choice(['pedra','papel','tesoura']).upper()

print(f'Vamos jogar, escolha entre Pedra, Papel e Tesoura!')
jogador = str(input('Escolha um opção: ')).upper().strip()

if jogador == 'PEDRA':
    if computador == 'PEDRA':
        print(f'Empate: {jogador} = {computador}!')
    elif computador == 'PAPEL':
        print(f'COMPUTADOR Ganhou! {computador} ganha de {jogador}!')
    elif computador == 'TESOURA':
        print(f'VOCÊ Ganhou! {jogador} ganha de {computador}!')

elif jogador == 'PAPEL':
    if computador == 'PEDRA':
        print(f'VOCÊ Ganhou! {jogador} ganha de {computador}!')
    elif computador == 'PAPEL':
        print(f'Empate: {jogador} = {computador}!')
    elif computador == 'TESOURA':
        print(f'COMPUTADOR Ganhou! {computador} ganha de {jogador}!')

elif jogador == 'TESOURA':
    if computador == 'PEDRA':
        print(f'COMPUTADOR Ganhou! {computador} ganha de {jogador}!')
    elif computador == 'PAPEL':
        print(f'VOCÊ Ganhou! {jogador} ganha de {computador}!')
    elif computador == 'TESOURA':
        print(f'Empate: {jogador} = {computador}!')
else:
    print('Jogada invalida!')
print(jogador)
print(computador)