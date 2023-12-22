#Converter temperatura Celsius em Fahrenheit.

tempc = float(input('Qual a temperatura em Celsius? '))

tempf = tempc*1.8+32 #para Fahrenheit multiplique por 1,8 e adicione 32 / para Celsius subtraia 32 e divida por 1,8

print(f'Temperatura:\n'
      f'Temperatura {tempc:.2f}ºC\n'
      f'Temperatura {tempf:.2f}ºF')