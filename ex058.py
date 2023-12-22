# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram
# necessarios para vencer.
from random import randint #randrange(1,10) pode utilizar tambem essa biblioteca.

print('Estou pensando em um número entre 1 e 10!')
nu_computador = randint(1,10) #computador cria um n1 aleatorio entre 1 e 5.
nu_usuario = 0
tentativas = 1

while nu_computador is not nu_usuario: #poderia usar tambem !=
    nu_usuario = int(input('Adivinhe quel é: '))  # pergunta um n1 para o usuario.
    if nu_computador == nu_usuario: #compara os numero
        print(f'\033[32mVocê Ganhou\033[m, precisou de {tentativas} tentativa! :-(')
    else:
        print(f'\033[31mERROOOOOO! :-D\033[m')
        tentativas += 1
print('FIM')
