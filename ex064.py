# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, qie é a condição da parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)
n1 = 0
contador = 0
soma = 0

while n1 != 999:
    n1 = int(input('Digite um numero [999=sair]: '))
    if n1 != 999:
        soma += n1
        contador += 1
    else:
        print(f'Foram digitados {contador} números e a soma é {soma}')
