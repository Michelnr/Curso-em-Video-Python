# crie um programa que mostre na tela todos os numero pares que estão no intervalo entre 1 e 50.

for contagem in range(1, 50):
    if contagem%2 == 0:
        print(f'{contagem}')
print('Fim')

#forma mais eficiente.
# for contagem in range(2, 50, 2):
#     print(f'{contagem}')
# print('Fim')