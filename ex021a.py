import pygame

# iniciando mixer
pygame.mixer.init()
# escolhendo a musica
mixer.music.load('ex021.mp3')

print('Sua música vai começar...')

# iniciando a música
mixer.music.play()

# menu de opções
while True:
    print('''\nMenu
[P] Pause
[R] Resume
[S] Stop''')

    userinput = input('Opção: ').upper()

    if userinput == 'P':
        mixer.music.pause()
        print('Música pausada!')
    elif userinput == 'R':
        mixer.music.unpause()
        print('Sua música vai continuar...')
    elif userinput == 'S':
        mixer.music.stop()
        print('Fim do programa.')
        break