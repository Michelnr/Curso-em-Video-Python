# faça um programa que leia um número inteiro e diga se ele é ou não um numero primo.

n1 = int(input('Informe um numero: '))
cont = 0

for n_primo in range(1, n1+1):
    if n1 % n_primo ==0:
        cont += 1
        print(f'\033[32m{n_primo}\033[m ', end='')
    else:
        print(f'\033[31m{n_primo}\033[m ', end='')
print('FIM')
if cont == 2:
    print(f'{n1} É um número primo!')
else:
    print(f'{n1} NÃO é um número primo')
