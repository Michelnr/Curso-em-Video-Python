#Escreva um programa que pergunte o salario de um funcionario e calcule o valor  do seu aumento.
#Para salarios superiores a 1250.00, calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o valor do salário? '))

if salario >= 1250.00:
    print(f'Salário teve um aumento de 10% e agora é R${salario*1.10:.2f}')
else:
    print(f'Salário teve um aumento de 15% e agora é R${salario*1.15:.2f}')
