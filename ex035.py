# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triângulo

a = float(input('Informe o primeiro lado: '))
b = float(input('INforme o segundo lado: '))
c = float(input('Informe o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
            print(f'Esses valores criam um triangulo!.\n'
                  f'O lado "a" tem o tamanho {a}\n'
                  f'O lado "b" tem o tamanho {b}\n'
                  f'O lado "c" tem o tamanho {c}')
else:
    print('Esses valores não formam um triangulo!')
