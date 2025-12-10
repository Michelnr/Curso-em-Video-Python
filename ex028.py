#Escreva um programa que faça o computador pensar em um n1 inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o n1 escolhido pelo computador.
#O programadeverá escrever na tela se o usuarío venceu ou perdeu.

from random import randint #randrange(1,6) pode utilizar tambem essa biblioteca.

print('Estou pensando em um n1 entre 1 e 5!')
nu_inf = int(input('Adivinhe quel é: ')) #pergunta um n1 para o usuario.
nu_ale = randint(1,5) #computador cria um n1 aleatorio entre 1 e 5.

if nu_inf == nu_ale: #compara os numero
    print('Você Ganhou! :-(')
else:
    print(f'EU GANHEI, o n1 é {nu_ale}! :-D')
