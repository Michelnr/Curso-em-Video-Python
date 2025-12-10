# Modulo para facilitar a mudança de cores e edição de strings.
teste = 'Texto teste'

comando = '\033['
final = '\033[0;0m'

texto = {'reset':'0;', 
         'negrito':'1;', 
         'sublinhado':'4;', 
         'inverter':'7;'}

color = {'reset':'0m', 
         'preto':'30m', 
         'vermelho':'31m', 
         'verde':'32m',
         'amarelo':'33m',
         'azul':'34m',
         'roxo':'35m',
         'ciano':'36m',
         'branco':'37m',}

print(color['verde']+'teste 1'+color['reset']+' teste 2')