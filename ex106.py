# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

# Variável global (Cores ANSI - estrutura conforme descrito na aula)
# Esta lista é global (c), permitindo o uso em todo o programa [1].
# Os índices representam: 0=Sem Cores, 1=Vermelho, 2 - Verde, 3 - Amarelo, 4=Azul, 5 - Roxo, 6=Branco,
c = (
    '\033[m',           # 0 - Sem cores
    '\033[0;30;41m',    # 1 - Vermelho
    '\033[0;30;42m',    # 2 - Verde
    '\033[0;30;43m',    # 3 - Amarelo
    '\033[0;30;44m',    # 4 - Azul
    '\033[0;30;45m',    # 5 - Roxo
    '\033[7;30m'        # 6 - Branco
)

# Definição da função AJUDA
# Esta função recebe o comando (com) digitado pelo usuário [8]
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

# Definição da função TÍTULO
# Esta função recebe uma mensagem (msg) e um código de cor opcional (cor=0) [4], [5]
def titulo(msg, cor=0):
    tam = len(msg) + 4
    
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[1], end='')
    sleep(1)

# PROGRAMA PRINCIPAL
comando = ''

# Loop principal para interação [13]
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)  # Exibe o título principal na cor 1 (Vermelho) [7]
    comando = str(input('Função ou Biblioteca > '))  # Lê o comando [14]
    if comando.upper() == 'FIM': # Verifica se o usuário quer sair [14]
        break
    else: # Chama a função de ajuda [8]
        ajuda(comando)
# Mensagem de encerramento [15]
titulo('ATÉ LOGO!', 1)