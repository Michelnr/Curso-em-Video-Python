#Faça um programa que leia uma frase pelo teclado e mostre
# -> Quantas vezes aparece a letra "A"
# -> Em que posição ela aparece a primeira vez
# -> Em que posição ela apare a ultima vez

frase = str(input('Escreva uma frase: ')).strip().upper()

print(f'A letra A aparece {frase.count("A")} vezes\n'
      f'Aparece a primeira vez na posição {frase.find("A")+1}\n'
      f'Aparece pela ultima vez na posição {frase.rfind("A")+1}')
