# Aula de listas dentro de listas

#Exemplo 1
galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Marcia", 45],]

#Exemplo 2
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #importane criar uma esse comando para criar uma copia e não espelhar para os dados.
    dado.clear()

print(galera)
