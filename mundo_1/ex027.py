#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Ultimo = Souza

nome = str(input('Escreva o nome: ')).strip() #Ana Maria de Souza
nome = nome.split()

primeiro_nome = nome[0]
segundo_nome = nome[(len(nome)-1)]

print(f'Primeiro Nome: {primeiro_nome}\n'
      f'fSegundo Nome: {segundo_nome}')
