# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#
# -Abaixo de 18.5: Abaixo do Peso:
# -Entre 18.5 e 25: Peso ideal
# -25 e 30: Sobrepeso
# -30 e 40: Obesidade
# -Acima de 40: Obesidade Mórbida

peso = float(input('Quantos quilos você peso? (Kg) '))
altura = float(input('Qual a sua altura? (Cm) '))

imc = peso/((altura/100)**2)

if imc < 16:
    print(f'Magreza Grau 3: IMC: {imc:.1f}')
elif 16 <= imc < 17:
    print(f'Magreza Grau 2: IMC: {imc:.1f}')
elif 17 <= imc < 18.5:
    print(f'Magreza Grau 1: IMC: {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'Saudavel: IMC: {imc:.1f}')
elif 25 <= imc < 30:
    print(f'Sobrepeso: IMC: {imc:.1f}')
elif 30 <= imc < 35:
    print(f'Obesidade Grau 1: IMC: {imc:.1f}')
elif 35 <= imc < 40:
    print(f'Obesidade Grau 2: IMC: {imc:.1f}')
else:
    print(f'Obesidade Grau 3: IMC: {imc:.1f}')
