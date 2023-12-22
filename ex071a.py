# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte  ao usuário qual será o valor a ser sacado (número inteiro),
# e o programa vai informar quantas cedulas de cada valor será entregues.
#
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('='*35)
print(f'        Banco Curso em Video')
print('='*35)
saque = int(input('Informe o valor do saque: R$'))
nota200 = nota100 = nota50 = nota20 = nota10 = nota5 = nota1 = 0

while saque != 0:
    if (saque - 200) >= 0:
        saque -= 200
        nota200 += 1
    elif (saque - 100) >= 0:
        saque -= 100
        nota100 += 1
    elif (saque - 50) >= 0:
        saque -= 50
        nota50 += 1
    elif (saque - 20) >= 0:
        saque -= 20
        nota20 += 1
    elif (saque - 10) >= 0:
        saque -= 10
        nota10 += 1
    elif (saque - 5) >= 0:
        saque -= 5
        nota1 += 1
    elif (saque - 1) >= 0:
        saque -= 1
        nota1 += 1

if nota200 > 0:
    print(f'{nota200} notas de R$200')
if nota100 > 0:
    print(f'{nota100} notas de R$100')
if nota50 > 0:
    print(f'{nota50} notas de R$50')
if nota20 > 0:
    print(f'{nota20} notas de R$20')
if nota10 > 0:
    print(f'{nota10} notas de R$10')
if nota5 > 0:
    print(f'{nota5} notas de R$5')
if nota1 > 0:
    print(f'{nota1} notas de R$1')
