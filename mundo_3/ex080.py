# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tabela.
listanum = []
while len(listanum) != 5:
    num = int(input(f"Informe o {len(listanum)+1}° numero: "))
    if num not in listanum:
        if len(listanum) == 0:
            listanum.append(num)
        else:
            for n in range(len(listanum)):
                if listanum[n] > num:
                    listanum.insert(n, num)
                    break
            else:
                listanum.append(num)
    else:
        print("Esse numero já existe!")
print(f"Os números informados foram: {listanum}")
