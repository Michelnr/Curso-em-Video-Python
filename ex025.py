#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual seu nome? ')).strip()

print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')

#______________________________________
#nome = input('Digite o nome: ').strip()

#nome = nome.upper()
#nome = nome.find('SILVA')
#print(nome)
#if (nome >= 0):
#    print('O nome POSSUI o nome SILVA')
#else:
#    print('NÃO possui o nome SILVA')
