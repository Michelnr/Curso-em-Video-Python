''' Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

cadastro_jogador = list()

while True:
    dados_jogador = dict()
    dados_jogador['Nome'] = input('Informe o nome do jogador: ').title()
    dados_jogador['Partidas'] = int(input('Quantas partidas jogadas: '))
    total_gols = 0
    
    for p in range(1, dados_jogador['Partidas']+1):
        gols = int(input(f'Quantos gols na Partida {p}: '))
        dados_jogador[f'Gols na Partida {p}'] = gols
        total_gols += gols
    dados_jogador['Total de Gols'] = total_gols
    dados_jogador['Aproveitamento'] = total_gols/dados_jogador['Partidas']

    cadastro_jogador.append(dados_jogador)
    
    while True:
        menu_sair = input('Deseja cadastrar outro jogador? (S/N) ').strip().upper()
        if menu_sair in ['N','S']:
            break
        else:
            print("Erro: Por favor, digite apenas S ou N.")

    if menu_sair == 'N':
        for dados in cadastro_jogador:
            print(30*'--')
            print(f'Nome do jogador: {dados['Nome']}')
            print(f'Numero de Partidas: {dados['Partidas']}')
            print(f'Total de Gols: {dados['Total de Gols']}')
            print(f'Aproveitamento: {dados['Aproveitamento']}')
            print(30*'--')
        break