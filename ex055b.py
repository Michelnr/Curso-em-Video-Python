# faça um programa que leia o peso de cinco pessoas.
# no final, mostre qual foi o maior e o menor peso lido.
maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f'Informe o peso (Kg) da {p}° pessoa: '))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
        if menor_peso > peso:
            menor_peso = peso

print(f'O maior peso é {maior_peso:.2f}Kg')
print(f'O menor peso é {menor_peso:.2f}Kg')
