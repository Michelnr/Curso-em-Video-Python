# Faça um programa que leia 3 numero e diga qual o maior e qual o menos
n1 = int(input('Informe o primeiro n1: '))
n2 = int(input('Informe o segundo n1: '))
n3 = int(input('Informe o terceiro n1: '))

maior = n1  # testa o maior n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1  # testa o menor n1
if n2 < n1 and n2 < n3:
    manor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'Maior n1: {maior}')
print(f'Menor n1: {menor}')
