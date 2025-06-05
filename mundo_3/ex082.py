# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores imparesdigitados, respectivamente.
# Ao final podem mostre o conteúdo das três listas geradas

listanum = []

while True:
    num = int(input("Informe um numero: "))
    if num not in listanum:
        listanum.append(num)
    else:
        print(f"Numero {num} já existe na lista!")

    escolha = str(input("Deseja incluir outro número? (S/N) ")).upper()
    if "N" or "S" in escolha:
        if "N" in escolha:
            listanum.sort()
            break
    else:
        print("Por favor, informe apenas S ou N")

listaimpar = []
listapar = []

for n in listanum:
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 == 1:
        listaimpar.append(n)
listapar.sort()
listaimpar.sort()

print(f"Os numeros digitados fora: {listanum}")
print(f"Os numeros pares são: {listapar}")
print(f"os numeros inpares são: {listaimpar}")
