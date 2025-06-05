# Crie uma tupla preenchida com os 20 primeiros colocados do Campeonato Brasileiro de Futebol,
# na ordem de colocação. depois mostre:
#
# A: Os 5 primeiros times.
# B: Os ultimos 4 colocados.
# C: Times em ordem alfabética
# D: Em que posição está o time do Flamengo

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corintians', 'Flamengo', 'Athletico-PR',
         'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
         'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Lista de times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Flamengo esta na posição: °{times.index("Flamengo")+1} ')
print('-='*30)
