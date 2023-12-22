# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
#
# -EQUILÁTERO: Todos os lados iguais
# -ISÓSCELES: Dois lados iguais
# -ESCALENO: Todos os lados diferentes

lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print(f'Esses valores criam um triangulo!.\n'
          f'O lado "Lado 1" tem o tamanho {lado1}\n'
          f'O lado "Lado 2" tem o tamanho {lado2}\n'
          f'O lado "Lado 3" tem o tamanho {lado3}')
    if lado1 == lado2 == lado3:
        print(f'Os lados são iguais, então eles é um triângulo EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Dois lados são iguais, então é um triângulo ISÓSCELES.')
    else:
        print('Todos os lados são diferentes, então é um triângulo ESCALENO.')
else:
    print('Esses valores não formam um triângulo.')
