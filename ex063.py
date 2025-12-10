# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequência de fibonacci.
#
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('='*22)
print('Sequencia de FIBONÁCI')
print('='*22)
termos = int(input('Quantos termos deseja mostrar: '))
contador = 3
n1 = 0
n2 = 1

print('0 -> ', end='')
print('1 -> ', end='')

while contador != termos:
    n3 = n1 + n2
    print(f'{n3} -> ', end='')
    n1 = n2
    n2 = n3
    contador += 1
print('FIM')
