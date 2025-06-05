# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade=str(input('Digite o nome da cidade: ')).strip()

print('SANTO' in cidade.split()[0].upper())

#____________________________________________________
#cidade = input('Digite o nome da cidade: ').strip()
#cidade=cidade.upper()
#cidade=cidade.find('SANTO')

#if cidade == 0:
#    print('Possui o nome SANTO no inicio.')
#else:
#    print('NÃO possui o nome SANTO no inicio.')
#______________________________________________________
#Descobre se no nome da cidade possui a palavra SANTO
#cidade = input('Digite o nome da cidade: ')

#cidade=cidade.upper()
#cidade=cidade.find('SANTO')

#if cidade >= 0:
#    print('Possui o nome SANTO.')
#else:
#    print('NÃO possui o nome SANTO.')