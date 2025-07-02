# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunas = []

while True:
    menu = input('Deseja sair? (S/N) ').upper()
    if menu == 'S':
        break
    elif menu != 'N':
        continue

    nome = str(input('Informe o nome do aluno: ')).title()
    nota_1 = int(input('Informe a 1º notas: '))
    nota_2 = int(input('Informe a 2º notas: '))

    aluno = []
    aluno.append(nome)
    aluno.append(nota_1)
    aluno.append(nota_2)
    lista_alunas.append(aluno)

for c in lista_alunas:
    print('---' * 15)
    print(f'Aluno: {c[0]}')
    print(f'Nota 1 = {c[1]}')
    print(f'Nota 2 = {c[2]}')
    print(f'Nota Final = {(c[1]+c[2])/2}')
print('---' * 15)