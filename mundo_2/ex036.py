# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exercer 30% do salário
# ou então o emprestimo será negado.

val_casa = float(input('Qual o valor da casa? R$'))
val_salario = float(input('Qual o valor da sua renda? R$'))
tempo = int(input('Qualtos anos será financiado? '))

parc_finan = val_casa/(tempo*12)
limite_renda = val_salario*0.30

if parc_finan < limite_renda:
    print('\033[32mPARABÉNS\033[m seu financioamento foi \033[32maprovado!\033[m')
    print(f'Sua parcela será de \033[32mR${parc_finan:.2f}\033[m')
else:
    print('Infelismente seu financiamento foi \033[31mreprovado\033[m.')