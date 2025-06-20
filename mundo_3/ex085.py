"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

lista_numero = [[], []] #0 = PAR, 1 = IMPAR
cont = 0
while True:
    if cont == 7:
        break
    numero = int(input(f"Informe o numero {cont+1}º número: "))
    #numero = (randint(1, 100))
    if numero % 2 == 0:
        lista_numero[0].append(numero)
    else:
        lista_numero[1].append(numero)
    cont += 1
print(f'Números pares -----> {sorted(lista_numero[0])}')
print(f'Números Impares ---> {sorted(lista_numero[1])}')