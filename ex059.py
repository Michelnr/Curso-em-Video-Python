# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] soma
# [2] multiplicação
# [3] maior
# [4] novos números
# [5] sair do programa
#
# seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
menu = 0

while menu != 5:
    menu = int(input(f'[1] soma\n'
                     f'[2] multiplicação\n'
                     f'[3] maior\n'
                     f'[4] novos números\n'
                     f'[5] sair do programa\n'
                     f'Escolha uma opções: '))
    if menu == 1:
        print(n1 + n2)
    elif menu == 2:
        print(n1 * n2)
    elif menu == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os números são iguais!')
    elif menu == 4:
        n1 = int(input('Escolha o primeiro número: '))
        n2 = int(input('Escolha o segundo número: '))
    elif menu == 5:
        print('Saindo')
    else:
        print('Opção INVALIDA tente novamente!')
print('Fim')
