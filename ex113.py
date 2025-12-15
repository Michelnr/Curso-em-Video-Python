# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(numero_informado = 5):
    while True:
        try:
            num_str = int(input(f'{numero_informado}'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Os dados informados são invalidos.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO! Usuário interrompeu a operação.\033[0m')
            break
        else:
            return num_str
            break
    
def leiaFloat(numero_informado = 5):
    while True:
        try:
            num_str = float(input(f'{numero_informado}'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Os dados informados são invalidos.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO! Usuário interrompeu a operação.\033[0m')
            break
        else:
            return num_str
            break
numero_inteiro = leiaInt('Digite um numero inteiro: ')
numero_real = leiaFloat('Digite um numero real: ')
print(f'Você digitou o número inteiro {numero_inteiro} e o numero real {numero_real}')