# Crie um programa que vai ler varios numero e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente
# C) Se a valor 5 foi digitado e está ou não na lista.

listanum = []

num = int(input("Informe um numero: "))
listanum.append(num)

while True:
    pergunta = str(input("Deseja informar outro numero S/N? ").upper())
    if "S" in pergunta:
        num = int(input("Informe o próximo numero: "))
        listanum.append(num)
    else:
        break
print(f"\nQuantos numeros foram digitados: {len(listanum)}")
listanum.sort(reverse=True)
print(f"lista de valores decrescente: {listanum}")
if 5 in listanum:
    print("Numero 5 esta na lista")
else:
    print("Numero 5 não esta na lista")
