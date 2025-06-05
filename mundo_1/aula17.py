num = [2, 5, 9, 1]
print('1', num)
# Troca o valor da posição indicada
num[2] = 3
print('2', num)
# Adiciona uma posição da lista
num.append(7)
print('3', num)
# coloca a lista em ordem
num.sort(reverse=True) # ordena de forma decrescente num.sort() apenas ordena
print('4', num)
# Adiciona um valor na posição escolhida
num.insert(2, 0)
print('5', num)
# Esse comando exclui apenas 1 valor da lista, informe uma posição nos parenteses para infomrar uma posição.
num.pop()
print('6', num)
# Esse comando remove o primeiro item com o valor informado
num.remove(2)
print('7', num)
print(f'Essa lista tem {len(num)} elementos.')
