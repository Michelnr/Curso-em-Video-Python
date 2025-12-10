# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

notas = {}

while True:
    print('DESEJA SAIR? escreva "S" no lugar do nome.')
    nome = str(input('Informe o nome do aluno: ')).title()
    
    if nome == 'S':
        break
    
    nota_1 = int(input('Informe a 1º notas: '))
    nota_2 = int(input('Informe a 2º notas: '))

    def media(n1, n2):
        return (n1 + n2) / 2

    notas[nome] = media(nota_1, nota_2)

print('---' * 15)
for n in notas:
    if notas[n] > 7:
        print(f'Nome: {n} ----> Nota: {notas[n]:.2f} ----> APROVADO')
    elif 5 < notas[n] < 7:
        print(f'Nome: {n} ----> Nota: {notas[n]:.2f} ----> RECUPERAÇÃO')
    else:
        print(f'Nome: {n} ----> Nota: {notas[n]:.2f} ----> REPROVADO')
print('---' * 15)