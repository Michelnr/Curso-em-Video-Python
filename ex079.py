# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente.
listanum = []
while True:
    num = int(input("Informe qual numero deseja adicionar: "))
    if listanum.count(num) == 0:
        listanum.append(num)
    else:
        print("numero já existe!")
    escolha = input("Deseja inserir mais um valor? S/N ").upper()
    if escolha in "N":
        listanum.sort()
        break
print(f"\nOs numeros informados foram: {listanum}")
