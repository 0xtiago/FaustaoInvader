import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    fi_settings = Settings()

    #Obtendo confs da tela
    screen = pygame.display.set_mode((fi_settings.screen_width,fi_settings.screen_height))

    #Definindo titulo da janela
    pygame.display.set_caption(fi_settings.titulo_jogo)

    #Definindo icone da janela
    faustao_icon = pygame.image.load(fi_settings.icone_jogo)
    pygame.display.set_icon(faustao_icon)

    #Cria a espaçonave
    ship = Ship(screen)

    #Inicia laço principal do jogo
    while True:

        #Observa eventos do teclado e do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redesenha a tela a cada passagem pelo laço
        screen.fill(fi_settings.bg_color)
        ship.blitme()

        #Deixa a tela mais recente visível
        pygame.display.flip()

run_game()