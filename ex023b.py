# Faça um programa que leia um número de 0 a 9999 e mostre no tela cada um dos resultados.
#
# Ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um n1 de ate 4 digitos: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Milhar: {milhar}\n'
      f'Centena: {centena}\n'
      f'Dezena: {dezena}\n'
      f'Unidade: {unidade}\n')
