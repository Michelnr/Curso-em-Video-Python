obj1 = input('Escreva algo: ')
print(f'O tipo primitivo é {type(obj1)}') #appresenta o tipo primitivo
print(f'Só tem espaço? {obj1.isspace()}') #apenas espaços
print(f'É um numero? {obj1.isnumeric()}') #apenas numero
print(f'É alfabetico? {obj1.isalpha()}') #apenas letras
print(f'Esta em maiuscula? {obj1.isupper()}') # Letras Maiusculas
print(f'Esta em minuscula? {obj1.islower()}') #Letras minusculas
print(f'Esta captalizada? {obj1.istitle()}') #Letras MAIUSCULAS e minusculas