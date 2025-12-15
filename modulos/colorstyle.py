# Modulo para facilitar a mudança de cores e edição de strings.
def colorStyle(texto, style='reset', color='reset'):
    '''
    Esse modulo visa facilitar a mudança de cores e estilos de textos no terminal.
    
    :param texto: Ira receber o texto a ser estilizado
    :param style: utilize os seguintes estilos: negrito, sublinhado, inverter
    :param color: utilize as seguintes cores: preto, vermelho, verde, amarelo, azul, roxo, ciano, branco
    :return: Retorna o texto estilizado com as cores e estilos escolhidos.
    '''
    if type(texto) != str:
        texto = str(texto)
    if type(style) != str:
        style = str(style)
    if type(color) != str:
        color = str(color)

    comando = '\033['
    final = '\033[0;0m'

    texto_dict = {'reset':'0;', 
                  'negrito':'1;', 
                  'sublinhado':'4;', 
                  'inverter':'7;'}

    color_dict = {'reset':'0m', 
                  'preto':'30m', 
                  'vermelho':'31m', 
                  'verde':'32m',
                  'amarelo':'33m',
                  'azul':'34m',
                  'roxo':'35m',
                  'ciano':'36m',
                  'branco':'37m',}

    estilo_texto = texto_dict.get(style, '0;')
    cor_texto = color_dict.get(color, '0m')

    return f"{comando}{estilo_texto}{cor_texto}{texto}{final}"