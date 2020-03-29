import sys
import pygame
from settings import Settings
from ship import Ship
from faustao import Alien
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

    #Cria a espaçonave, um grupo de projeteis e um grupo de alienigenas
    ship = Ship(fi_settings, screen)
    bullets = Group()
    aliens = Group()

    #Cria frota Faustão alienigena
    gf.create_fleet(fi_settings, screen, aliens)
    #Cria um alienigena
    #alien = Alien(fi_settings,screen)

    #Inicia laço principal do jogo
    while True:

        #Responde aos eventos de pressionamento de teclas e de mouse
        gf.check_events(fi_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        #Atualiza as imagens na tela e alterna para a nova tela
        gf.update_screen(fi_settings, screen, ship, aliens, bullets)

run_game()