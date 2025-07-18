# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
nome_jogador = str(input('Informe o nome do jogador: '))
numero_partidas = int(input('Informe o número de partidas: '))
numero_gols = int(input('informe o número de gols: '))

jogadores = dict()


# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.