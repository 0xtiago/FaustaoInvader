import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

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
    ship = Ship(fi_settings,screen)

    #Cria um grupo onde serão armazenados os projeteis
    bullets = Group()

    #Inicia laço principal do jogo
    while True:

        #Responde aos eventos de pressionamento de teclas e de mouse
        gf.check_events(fi_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        #Atualiza as imagens na tela e alterna para a nova tela
        gf.update_screen(fi_settings, screen, ship, bullets)

run_game()