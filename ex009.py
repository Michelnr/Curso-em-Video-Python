#Foi utilizado o comando While para criar um loop e fazer uma taboada.

n1 = int(input('Digite um n1 para tabuada: '))
n2 = 1

while n2 <= 10: #verifica a condição
    print(f'{n1}x{n2}={n1*n2}') #o corpo, a ação
    n2 += 1 #o passo de "incremento"