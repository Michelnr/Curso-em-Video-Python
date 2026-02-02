def cadastrar():
    try:
        print('Digite 0 para voltar ao MENU PRINCIPAL')
        nome = str(input('Digite o nome do pessoa: '))
        if nome == 0:
            menu()
        idade = int(input('Digite a idade do pessoa: '))
        if idade == 0:
            menu()