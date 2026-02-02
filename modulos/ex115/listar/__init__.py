def listar():
    try:
        texto('OPÇÃO 2 - Listar pessoas')
        arquivo = open('modulos/ex115/cadastro/dados.txt', 'r')
        print(arquivo.read())
        arquivo.close()
    except FileNotFoundError:
        print('Nenhum dado cadastrado ainda.')