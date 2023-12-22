#Esse script escolhe uma das opções de forma aleatoria.
from random import choice

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))

lista = (aluno1,aluno2,aluno3,aluno4)
escolhido = choice(lista)

print(f'O aluno escolhido é: {escolhido}')
