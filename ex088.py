# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos numero_jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

lista_jogos = []

numero_jogos = int(input('Quantos numero_jogos de seja jogar? '))

while True:
    jogo = []
    while len(jogo) < 6:
        sorteio = randint(1,60)
        if sorteio not in jogo:
            jogo.append(sorteio)
    jogo.sort()
    lista_jogos.append(jogo)
    if len(lista_jogos) == numero_jogos:
        break

for l in range(0, len(lista_jogos)):
    print(f'Jogo {l+1} {lista_jogos[l]}')