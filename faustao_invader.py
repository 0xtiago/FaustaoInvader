import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    #Cria o botão Play
    play_button = Button(fi_settings, screen, "Play")

    #Definindo icone da janela
    faustao_icon = pygame.image.load(fi_settings.icone_jogo)
    pygame.display.set_icon(faustao_icon)

    #Cria uma instancia para armazena dados estatisticos do jogo e cria painel de pontuação
    stats = GameStats(fi_settings)
    sb = Scoreboard(fi_settings, screen, stats)

    #Cria a espaçonave, um grupo de projeteis e um grupo de alienigenas
    ship = Ship(fi_settings, screen)
    bullets = Group()
    aliens = Group()

    #Cria frota Faustão alienigena
    gf.create_fleet(fi_settings, screen, ship, aliens)
    #Cria um alienigena
    #alien = Alien(fi_settings,screen)

    #Inicia laço principal do jogo
    while True:

        #Responde aos eventos de pressionamento de teclas e de mouse
        gf.check_events(fi_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(fi_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(fi_settings, screen, stats, sb, ship, aliens, bullets)

        #Atualiza as imagens na tela e alterna para a nova tela
        gf.update_screen(fi_settings, screen, stats,sb, ship, aliens, bullets, play_button)

run_game()