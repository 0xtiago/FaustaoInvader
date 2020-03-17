import sys
import pygame

def run_game():
    #Inicializa jogo e cria um objeto na tela
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Faustão Invader")

    #Definindo icone da janela
    faustaoIcon = pygame.image.load('images/faustao_icon.png')
    pygame.display.set_icon(faustaoIcon)

    #Definindo cor de fundo
    bg_color = (230,230,230)


    #Inicia laço principal do jogo
    while True:

        #Observa eventos do teclado e do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redesenha a tela a cada passagem pelo laço
        screen.fill(bg_color)

        #Deixa a tela mais recente visível
        pygame.display.flip()

run_game()