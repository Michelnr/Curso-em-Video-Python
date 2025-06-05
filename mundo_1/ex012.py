#Esse Script da um desconto de 5% no valor do produto.
preço = float(input('Coloque o preço do produto: '))

print(f'Preço do produto esta com disconto de 5%!\n'
      f'Preço do produto: R${preço:.2f}\n'
      f'Preço com desconto: R${preço*0.95:.2f}')