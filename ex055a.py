# faça um programa que leia o peso de cinco pessoas.
# no final, mostre qual foi o maior e o menor peso lido.

lista_peso = []

for peso in range(1, 6):
    info_peso = float(input(f'Informe o peso (Kg) da {peso}° pessoa: '))
    lista_peso.append(info_peso)

maior_peso = lista_peso[0]
menor_peso = lista_peso[0]

for comp_peso in range(0, 5):
    if maior_peso < lista_peso[comp_peso]:
        maior_peso = lista_peso[comp_peso]
    if menor_peso > lista_peso[comp_peso]:
        menor_peso = lista_peso[comp_peso]

print(f'O maior peso é {maior_peso:.2f}Kg')
print(f'O menor peso é {menor_peso:.2f}Kg')
