#Operações matematicas que podem ser implementadas.
#o comando \n faz com que o resultado que esta na mesma linha seja apresentado na linha a baixo.

n1 = int(input('Qual o primeiro n1? '))
n2 = int(input('Qual o segundo n1? '))

s = n1 + n2 #Soma
m = n1 * n2 #Multiplicação
d = n1 / n2 #Divisão
di = n1 // n2 #Divisão Inteira
pt = n1 ** n2 #Potencia

print(f'Soma = {s}\n'
      f'Multiplicação = {m}\n'
      f'Divisão = {d}\n'
      f'Divisão Inteira = {di}\n'
      f'Potencia = {pt}')
