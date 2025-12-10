# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

expressao = input(str("Informe uma Expressão: "))
parentese_esq = []
parentese_dir = []

for p in expressao:
    if p == "(":
        parentese_esq.append(p)
    elif p == ")":
        parentese_dir.append(p)

if parentese_esq.count("(") == parentese_dir.count(")"):
    print("Essa expressão É valida!")
else:
    print("Essa expressão NÃO é valida!")
