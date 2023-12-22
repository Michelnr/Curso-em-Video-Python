# crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos em valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n1 = int(input('Digite um numero [sair=999]: '))
maior = menor = n1
soma = contador = 0

while n1 != 999:
    if n1 != 999:
        soma += n1
        contador += 1
        if maior < n1:
            maior = n1
        if menor > n1:
            menor = n1
    n1 = int(input('Digite um numero [sair=999]: '))

media = soma / contador
print(f'A media dos valores é {media}\n'
      f'Maior número: {maior}\n'
      f'Menor número: {menor}')
