# faça um programa que calcule a soma entre todos os numero impares que são multiplos
# de 3 e que se encontram no intervalo de 1 ate 500.
soma = 0
cont_açao = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        cont_açao += 1
        soma += cont
        print(cont)
print(f'A soma dos numeros impares multiplos de 3 entre 1 e 500 é {soma}\n'
      f'Foram necessarios {cont_açao} ações')
