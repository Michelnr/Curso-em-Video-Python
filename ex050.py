# desenvolva um programa que leia seis numero inteiros e mostre a soma apenas
# daqueles que forem pares. se o valor digitado for impar, desconsidere-o.
soma = 0
for repet in range(1, 7):
    numero = int(input(f'Digite o {repet}° numero: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos numeros pares é igual a {soma}.')
