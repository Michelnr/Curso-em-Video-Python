'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

# Inicializa um dicionário vazio para armazenar os dados do jogador
jogador = dict()

# Inicializa uma lista vazia para armazenar os gols por partida
partidas = list()

# 1. Pede o nome do jogador e armazena na chave 'nome' do dicionário
jogador['nome'] = str(input('Nome do Jogador: '))

# 2. Pede o total de partidas jogadas, convertendo para inteiro
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# 3. Loop para pedir os gols de cada partida
for c in range(0, tot):
    # Pede os gols da partida 'c' e adiciona à lista 'partidas'
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? '))) # Adicionei + 1 para o usuário ver a partida 1, 2, 3...

# 4. Adiciona a lista de gols ao dicionário
jogador['gols'] = partidas[:] # [:] cria uma cópia da lista

# 5. Calcula o total de gols e armazena no dicionário
jogador['total'] = sum(partidas)

# --- Exibição dos Dados ---
print('=' * 30)

# Exibe o dicionário completo (para fins de debug/visualização)
print(jogador)

print('=' * 30)

# Exibe os dados chave por chave
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=' * 30)

# Exibe um resumo formatado
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

# Exibe os gols feitos em cada partida
# 'enumerate' é ótimo para saber a posição (índice) e o valor (gol)
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.') # Novamente, i + 1 para melhor leitura

# Exibe o total geral
print(f'Foi um total de {jogador["total"]} gols.')